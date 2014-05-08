from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import minitwitter.app.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'minitwitter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', minitwitter.app.views.index, name='index'),
    url(r'^tweets/(\d+)/$', minitwitter.app.views.show, name='show'),
    url(r'^admin/', include(admin.site.urls)),
)
