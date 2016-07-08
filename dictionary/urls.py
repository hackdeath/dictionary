from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.detailWord, name='index'),
	url(r'^(?P<word>[a-z]+)/$', views.detailWord, name='detailWord')
]