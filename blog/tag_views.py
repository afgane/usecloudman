from django.views.generic.list_detail import object_list
from tagging.models import Tag,TaggedItem
from blog.models import Entry

def tag_detail(request, slug):
    unslug = slug.replace('-', ' ')
    tag = Tag.objects.get(name=unslug)
    qs = TaggedItem.objects.get_by_model(Entry, tag)
    return object_list(request, queryset=qs, extra_context={'tag':slug}, template_name='tags/list.html')

