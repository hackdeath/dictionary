from django.conf.urls import url

from . import views

app_name = 'dictionary'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^letter/(?P<lang>[A-Za-z-]+)/(?P<letter>.)/', views.letter, name='letter'),
    url(r'^word/(?P<word>.+)/', views.detailWord, name='detailWord'),
    url(r'^submit/(?P<id_word>[0-9]+)/$', views.submitWord, name='submitWord'),
    url(r'^stage/$', views.stagearea, name='stagearea'),
    url(r'^accept/(?P<language>[A-Za-z-]+)/(?P<id_word>[0-9]+)/$', views.accept, name='accept'),
    url(r'^refuse/(?P<language>[A-Za-z-]+)/(?P<id_word>[0-9]+)/$', views.refuse, name='refuse'),
]
