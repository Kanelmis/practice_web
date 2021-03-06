""" learning_logs"""

from django.urls import path,re_path

from . import views

urlpatterns = [
    #homepage
    path('',views.index, name='index'),

    #reveal all topics
    re_path('topics/$', views.topics, name='topics'),

    #specific theme page
    re_path(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),

    #new topics
    re_path(r'^new_topic/$', views.new_topic, name = 'new_topic'),

    #new entry
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry,name='new_entry'),

    #edit entry
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry, name='edit_entry'),
] 
