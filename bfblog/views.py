from django.shortcuts import render
from django.views import generic
from .models import BlogPost


class PostListView(generic.ListView):
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'bfblog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        tag = self.request.GET.get('tag')
        if tag:
            qs = BlogPost.objects.filter(
                tags__slug=tag).order_by('-created_on')
        return qs


class PostDetailView(generic.DetailView):
    model = BlogPost
    template_name = 'bfblog/one_post.html'
    context_object_name = 'post'
