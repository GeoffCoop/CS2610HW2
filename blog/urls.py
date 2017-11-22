from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.indexView.as_view(), name='index'),
    url(r'^archive/$', views.archiveView.as_view(), name='archive'),
    url(r'^(?P<pk>[0-9]+)/$', views.detailView.as_view(), name='blog'),
    url(r'^(?P<pk>[0-9]+)/comment/$', views.post, name='post'),
]