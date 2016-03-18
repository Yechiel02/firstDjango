from django.conf.urls import url
from django.conf.urls import patterns
from . import views

urlpatterns = patterns(
               '',
               url(r'^$', views.IndexView.get_queryset, name='index'),
               # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
               # url(r'^(?P<question_id>[0-9]+)/results$', views.results, name='results'),
               # url(r'^(?P<question_id>[0-9]+)/votes$', views.vote, name='vote'),
               # (r'^$', 'polls.views.index', {'templates': 'index.html'}),
)
