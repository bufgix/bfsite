from django.contrib import admin

from .models import Paste


class PasteAdmin(admin.ModelAdmin):
    list_display = ('author', 'pub_date', 'paste_id')
    readonly_fields = ('paste_id', 'pub_date')


admin.site.register(Paste, PasteAdmin)
