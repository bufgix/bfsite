from django.db import models
from django.utils import timezone

from .utils import SUPPORT_LANGS

import secrets


class Paste(models.Model):
    class Meta:
        verbose_name = 'Paste'

    paste_id = models.CharField(unique=True, max_length=30)
    author = models.CharField(max_length=100, default="Anonymous")
    content = models.TextField()
    pub_date = models.DateTimeField('Publising date', default=timezone.now())
    lang = models.CharField(choices=SUPPORT_LANGS, max_length=100,
                            default=SUPPORT_LANGS[0], verbose_name="Language")

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.paste_id:
            self.paste_id = secrets.token_hex(10)
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def __str__(self):
        return f"{self.author}"
