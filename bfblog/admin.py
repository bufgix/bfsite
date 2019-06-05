from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from .models import BlogPost, SuperUser, BloTags
from .forms import SuperUserChangeForm, SuperUserCreationForm, BlogPostForm


class BlogPostAdmin(admin.ModelAdmin):
    def get_page(self):
        return mark_safe(f'<a target="_blank" href="{self.absolute_url()}">Show Post</a>')
    def get_preview(self):
        return mark_safe(f'<a target="_blank" href="{self.preview_url()}">Preview</a>')
    get_page.short_description = "Page"
    get_preview.short_description = "Preview"

    list_display = ('title', 'created_on', 'update_on', 'status', get_page)
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    form = BlogPostForm
    readonly_fields = (get_preview, )
class BlogTagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class SuperUserAdmin(UserAdmin):
    add_form = SuperUserCreationForm
    form = SuperUserChangeForm
    model = SuperUser
    list_display = ['username', 'email', 'first_name', 'last_name']


    def get_fieldsets(self, request, obj=None):
        fs = super().get_fieldsets(request, obj=obj)
        fs = (('General', {'fields': ('username', 'password', 'user_image')}),
              ('Personel Information', {
               'fields': ('first_name', 'last_name', 'email')}),
              ('Permission',
               {'fields': ('is_active',
                           'is_staff',
                           'is_superuser',
                           'groups',
                           'user_permissions')}),
              ('Important Dates', {'fields': ('last_login', 'date_joined')}))
        return fs


admin.site.register(BloTags, BlogTagsAdmin)
admin.site.register(SuperUser, SuperUserAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
