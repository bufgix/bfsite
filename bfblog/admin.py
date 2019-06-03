from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from .models import BlogPost, SuperUser
from .forms import CustomUserChangeForm, CustomUserCreationForm


class BlogPostAdmin(admin.ModelAdmin):
    def get_page(self):
        return mark_safe(f'<a target="_blank" href="{self.absolute_url()}">Show Post</a>')
    get_page.short_description = "Page"

    list_display = ('title', 'created_on', 'update_on', 'status', get_page)
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class SuperUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = SuperUser
    list_display = ['email', 'username', 'nick']

    def get_fieldsets(self, request, obj=None):
        fs = super().get_fieldsets(request, obj=obj)
        fs[0][1]['fields'] = fs[0][1]['fields'] + ('nick',)
        __import__('pprint').pprint(fs)
        return fs


admin.site.register(SuperUser, SuperUserAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
