from django.conf.urls import url

from . import views

app_name = 'dictionary'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^letter/(?P<lang>[A-Za-z-]+)/$', views.letter, name='letter'),
    url(r'^word/(?P<word>.+)/', views.detailWord, name='detailWord'),
    url(r'^submit/(?P<id_word>[0-9]+)/$', views.submitWord, name='submitWord'),
    url(r'^stage/$', views.stagearea, name='stagearea'),
    url(r'^accept/(?P<id>\d+)/$', views.accept, name='accept'),
    url(r'^refuse/(?P<id>\d+)/(?P<redirect>[A-Za-z-]+)/$', views.refuse, name='refuse'),
]
