from django.conf.urls import patterns, include, url
from stories import views

urlpatterns = patterns('',
    '''
    #  below moved to ../urls.py for now

    # first step, user picks a story by title
    url(r'^$', views.index),

    # user enters token replacements
    url(r'^story/', views.answers_form),

    # user sees story w/tokens replaced with answers
    url(r'^done/', views.print_story),
    '''
)