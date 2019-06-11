from django.shortcuts import render
from django.views import generic
from .models import BlogPost, BlogTags


class TagSender:
    def get_context_data(self, **kwargs):
        cd = super().get_context_data(**kwargs)
        cd['tags'] = {tag: tag.blogpost_set.all().count() for tag in BlogTags.objects.order_by('slug')}
        return cd

class PostListView(TagSender, generic.ListView):
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'bfblog/index.html'
    context_object_name = 'posts'



class PostDetailView(TagSender, generic.DetailView):
    model = BlogPost
    template_name = 'bfblog/one_post.html'
    context_object_name = 'post'
    

