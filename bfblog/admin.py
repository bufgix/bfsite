from django.contrib import admin

from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'update_on', 'status')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    

admin.site.register(BlogPost, BlogPostAdmin)
