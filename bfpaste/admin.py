from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse

from .models import Paste


class PasteAdmin(admin.ModelAdmin):
    def view_paste(self):
        return mark_safe(f"<a href='{reverse('bfpaste:show_paste', kwargs={'paste_id': self.paste_id})}'>View</a>")
    view_paste.short_description = 'Page'

    list_display = ('author', 'pub_date', view_paste)
    readonly_fields = ('paste_id', 'pub_date')


admin.site.register(Paste, PasteAdmin)
