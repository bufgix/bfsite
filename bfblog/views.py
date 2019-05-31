from django.shortcuts import render

from .models import BlogPost

def blog_index(request):
    posts = BlogPost.objects.filter(status=1).order_by("-created_on")

    return render(request, 'bfblog/index.html', context= {'posts': posts})

def blog_new(request):
    pass