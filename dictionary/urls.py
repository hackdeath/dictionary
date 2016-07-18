from django.conf.urls import url

from . import views

app_name = 'dictionary'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^letter/(?P<lang>[A-Za-z-]+)/(?P<letter>.)/', views.letter, name='letter'),
	url(r'^word/(?P<word>[A-Za-z\W]+)/', views.detailWord, name='detailWord')
]
