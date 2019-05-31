from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    def get_page(self):
        return mark_safe(f'<a target="_blank" href="{self.absolute_url()}">Show Post</a>')
    get_page.short_description = "Page"

    list_display = ('title', 'created_on', 'update_on', 'status', get_page)
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(BlogPost, BlogPostAdmin)
