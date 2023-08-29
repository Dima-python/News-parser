from django.shortcuts import render, redirect
from .models import Category, Topic, Choice
from .forms import ContactForm, TopicForm
from bs4 import BeautifulSoup
import requests

# Create your views here.
def index(request):
	global form
	category = Category.objects.all()
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
		return redirect("news/")
	else:
		form = ContactForm()

	return render(request, 'news/index.html', {'category': category, 'form': form})

def topic(request):
	global form
	global business_url
	subject = form.cleaned_data.get("field")

	if request.method == 'POST':
		res = TopicForm(request.POST)
		if res.is_valid():
			print(res.cleaned_data)
		return redirect('text/')
	else:
		res = TopicForm()

	url = "https://newsmiass.ru/"
	page = requests.get(url)
	soup = BeautifulSoup(page.text, "html.parser")
	business = soup.find('a',title = subject).get('href')
	business_url = requests.get(f"https://newsmiass.ru/{business}")

	soup_2 = BeautifulSoup(business_url.text, "html.parser")
	if Topic.objects.all().exists() == True:
			Topic.objects.all().delete()

	for i in soup_2.findAll('a', class_= 'title'):
		Topic.objects.create(name_topic = i.text).save()

	return render(request, 'news/topic.html', {'themes': Topic.objects.all(), 'res': res})


def text(request):
	global business_url
	script = []
	if request.method == 'POST':
		res = TopicForm(request.POST)
		if res.is_valid():
			print(res.cleaned_data)
			res = res.cleaned_data.get('name')
	else:
		res = TopicForm()

	soup_2 = BeautifulSoup(business_url.text, "html.parser")
	for i in soup_2.findAll('a', class_= 'title'):
		if i.get_text() == res:
			topic = i.get('href')
			topic_url = requests.get(f"https://newsmiass.ru{topic}")
	
	text_topic = BeautifulSoup(topic_url.text, "html.parser")
	for k in text_topic.findAll('p'):
		script.append(k.text)
	return render(request, 'news/text.html', {'script': script})
	
