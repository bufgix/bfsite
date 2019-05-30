from django.shortcuts import render

def blog_index(request):
    return render(request, 'bfblog/index.html')

def blog_new(request):
    pass