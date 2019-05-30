from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Title")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Slug")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    update_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0, verbose_name="Status")

    class Meta:
        verbose_name = "Blog Post"
        ordering = ['-created_on']

    def __str__(self):
        return self.title.title()