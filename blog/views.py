import operator
from django.db.models import Q
from django.views.generic import dates
from blog.models import Entry

class BlogMixin(object):
    """
    To be subclassed by date generic views
     * Add default params to the generic views for displaying blog entries
     * Allow entry lists to be further filtered by tags
    """
    date_field = 'pub_date'
    paginate_by = 10
    allow_empty = True
    allow_future = True
    queryset = Entry.objects.all()
    month_format = "%m"
    template_name = 'blog/list_all.html'
    context_object_name = 'object_list'
    
    def dispatch(self, request, *args, **kwargs):
        """
        Get any tags that might have been provided in the GET so they can be filtered later
        """
        kwargs['taglist'] = request.GET.getlist('tag', [])
        return super(BlogMixin, self).dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        """
        Filter the queryset by the specified tags. Can use to specify multiple
        tags, eg: /blog?tag=tag1&tag=tag2
        """
        tags = self.kwargs.get('taglist', [])
        if len(tags) > 0:
            f = reduce(operator.and_, (Q(tags__icontains=t) for t in tags))
            return super(BlogMixin, self).get_queryset().filter(f)
        return super(BlogMixin, self).get_queryset()
    

class IndexView(BlogMixin, dates.ArchiveIndexView):
    pass


class MonthArchiveView(BlogMixin, dates.MonthArchiveView):
    pass


class DayArchiveView(BlogMixin, dates.DayArchiveView):
    pass


class DetailsView(BlogMixin, dates.DateDetailView):
    template_name = 'blog/detail.html'
    context_object_name = "object"

