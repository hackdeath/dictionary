from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^word/(?P<word>[A-Za-z]+)/', views.detailWord, name='detailWord')
]
