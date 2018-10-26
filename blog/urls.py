
from django.conf.urls import url

from . import views

app_name = "blog"

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    url(r'^create/$', views.create_page, name='create_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page, name='edit_page'),
    url(r'^create/action$', views.create_action, name='create_action'),
    url(r'^edit/action$', views.edit_action, name='edit_action'),
    url(r'^delete/(?P<article_id>[0-9]+)$', views.delete_action, name='article_delete'),

]
