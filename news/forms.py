from django import forms

class ContactForm(forms.Form):
	field = forms.CharField(max_length=255)

class TopicForm(forms.Form):
	name = forms.CharField(max_length=255)