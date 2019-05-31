from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

import pathlib
import secrets
import os

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


def path_and_rename(path):
    def wrapper(instance, filename):
        ext = pathlib.Path(filename).suffix
        filename = f"{secrets.token_urlsafe(10) + ext}"
        return os.path.join(path, filename)
    return wrapper


class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Title")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Slug")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    update_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(
        choices=STATUS, default=0, verbose_name="Status")
    banner_image = models.ImageField(upload_to=path_and_rename(
        'postimages'), verbose_name="Post image")

    class Meta:
        verbose_name = "Blog Post"
        ordering = ['-created_on']

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        try:
            this = BlogPost.objects.get(id=self.id)
            if this.banner_image != self.banner_image:
                this.banner_image.delete()
        except:
            pass
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def absolute_url(self):
        return reverse('bfblog:single_post', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title.title()
