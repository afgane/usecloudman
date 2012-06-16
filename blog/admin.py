from django.contrib import admin
from blog.models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date','enable_comments', 'status')
    search_fields = ['title', 'body_markdown']
    list_filter = ('pub_date', 'enable_comments', 'status')
    prepopulated_fields = {"slug": ('title',)}
    fieldsets = (
        (None, {'fields': (('title', 'status'), 'body_markdown', ('pub_date', 'enable_comments'), 'tags', 'slug')}),
    )
    class Media:
        js = ('/static/js/jquery-1.7.2.min.js',
              '/static/js/tiny_mce/tiny_mce.js',
              '/static/js/tiny_mce/textareas.js',)

admin.site.register(Entry, EntryAdmin)
