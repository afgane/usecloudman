from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'usecloudman.views.home', name='home'),
    url(r'^$', direct_to_template, {'template': 'index.html'}, "home"),
    # url(r'^usecloudman/', include('usecloudman.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^blog/', include('blog.urls')),
)
