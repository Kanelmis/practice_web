""" learning_logs"""

from django.urls import path,re_path

from . import views

urlpatterns = [
    #homepage
    path('',views.index, name='index'),

    #reveal all topics
    re_path('topics/$', views.topics, name='topics'),

    #specific theme page
    re_path('^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
] 
