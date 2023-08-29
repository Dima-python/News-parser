from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'home'),
    path('news/', views.topic, name	= 'news'),
    path('news/text/', views.text, name	= 'text')
]
