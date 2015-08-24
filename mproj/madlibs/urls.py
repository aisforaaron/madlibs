from django.conf.urls import patterns, include, url
from django.contrib import admin
from stories import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #url(r'', include('stories.urls')), # send all requests to stories app urls.py
    #url(r'^$', include('stories.urls')),

    # from stories/urls.py ------ //
    # first step, user picks a story by title
    url(r'^$', views.index),

    # user enters token replacements
    url(r'^story/', views.answers_form),

    # user sees story w/tokens replaced with answers
    url(r'^done/', views.print_story),    
)

# to get admin static assets working
import settings
urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
)