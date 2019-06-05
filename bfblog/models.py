from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, AbstractUser
from django.utils.deconstruct import deconstructible

import pathlib
import secrets
import os

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


@deconstructible
class PathandRename:
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = pathlib.Path(filename).suffix
        filename = f"{secrets.token_urlsafe(10) + ext}"
        return os.path.join(self.path, filename)


path_and_rename = PathandRename


class SuperUser(AbstractUser):
    user_image = models.ImageField(upload_to=path_and_rename(
        'profile_pics'), verbose_name="User Image")

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        try:
            this = SuperUser.objects.get(id=self.id)
            if this.user_image != self.user_image:
                this.user_image.delete()
        except:
            pass
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def __str__(self):
        return self.username


class BlogTags(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Tags"
        verbose_name_plural = "Tags"
    
    def __str__(self):
        return f"{self.name}"

class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Title")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Slug")
    author = models.ForeignKey(
        SuperUser, on_delete=models.CASCADE, related_name="blog_posts")
    update_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(
        choices=STATUS, default=0, verbose_name="Status")
    tags = models.ManyToManyField(BlogTags)
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
