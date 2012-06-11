from django.conf.urls.defaults import *
from blog.models import Entry
# from django.views.generic import dates
from blog.views import *
# from tagging.views import tagged_object_list

# info_dict = {
#     'queryset': Entry.objects.filter(status=1),
#     'date_field': 'pub_date',
#     # 'month_format': '%m',
# }

urlpatterns = patterns('django.views.generic.date_based',
    # (r'(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
    #     'object_detail', dict(info_dict, template_name='blog/detail.html')),
    url(r'(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
        DetailsView.as_view()),
    url(r'(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{1,2})/$',
        DayArchiveView.as_view()),
    url(r'(?P<year>\d{4})/(?P<month>\d{2})/$',
        MonthArchiveView.as_view()),
    url(r'(?P<year>\d{4})/$',
        IndexView.as_view()),
    url(r'^$', IndexView.as_view()),
    # url(r'^all/$', ArchiveView.as_view()),
    
    # (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
    #     'object_detail', dict(info_dict, template_name='blog/list.html')),
    # (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{1,2})/$', 'archive_day',
    #     dict(info_dict, template_name='blog/list.html')),
    # (r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'archive_month',
    #     dict(info_dict, template_name='blog/list.html')),
    # (r'^(?P<year>\d{4})/$', 'archive_year', dict(info_dict, template_name='blog/list.html',
    #     make_object_list=True)),
    # (r'^$', 'archive_index', dict(info_dict, template_name='blog/list.html',
    #     template_object_name='object_list')),
    # (r'^all/$', 'archive_index', dict(info_dict, template_name='blog/list_all.html',
    #     template_object_name='object_list')),
)