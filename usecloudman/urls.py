from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'usecloudman.views.home', name='home'),
    # Point to the 'old' static templates
    url(r'^$', direct_to_template, {'template': 'index.html'}, "home"),
    url(r'^publications$', direct_to_template, {'template': 'publications.html'}, "publications"),
    url(r'^screencasts$', direct_to_template, {'template': 'screencasts.html'}, "screencasts"),
    # Point to 'enis' part of the page (also reuse the old static pages)
    url(r'^enis/$', direct_to_template, {'template': 'enis/index.html'}, "enis_home"),
    url(r'^enis/index.html$', direct_to_template, {'template': 'enis/index.html'}, "enis_home"),
    url(r'^enis/publications/$', direct_to_template,
        {'template': 'enis/publications.html'}, "enis_publications"),
    url(r'^enis/projects/$', direct_to_template,
        {'template': 'enis/projects.html'}, "enis_projects"),
    url(r'^enis/contact/$', direct_to_template,
        {'template': 'enis/contact.html'}, "enis_contact"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^blog/', include('blog.urls')),
)
