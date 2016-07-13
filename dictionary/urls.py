from django.conf.urls import url

from . import views

app_name = 'dictionary'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^word/(?P<word>[A-Za-z\W]+)/', views.detailWord, name='detailWord')
]
