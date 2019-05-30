from django.urls import path

from .views import blog_index, blog_new

app_name = "bfblog"
urlpatterns = [
    path('', blog_index, name="index"),
    path('new/', blog_new, name="new")
]