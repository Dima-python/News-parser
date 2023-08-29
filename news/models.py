from django.db import models
from django.forms import ModelForm

# Create your models here.

class Category(models.Model): 
	input_text = models.CharField(max_length=200, help_text = "Номер рубрики")
	all_category = models.TextField(null=True)

	def __str__(self):
		return self.all_category

	class Meta:
		verbose_name = 'Рубрика'
		verbose_name_plural = 'Рубрики'


class Topic(models.Model):
	name_topic = models.CharField(max_length=255)

	def __str__(self):
		return self.name_topic

class Choice(ModelForm):
	class Meta:
		model = Topic
		fields = ['name_topic']
