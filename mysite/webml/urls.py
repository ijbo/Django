from . import views 
from django.urls import path,include
from django.conf.urls import url,include
from django.conf import settings

urlpatterns = [
	url(r'^$', views.index, name='index'),
]
