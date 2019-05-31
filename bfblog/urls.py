from django.urls import path

from .views import PostListView, PostDetailView

app_name = "bfblog"
urlpatterns = [
    path('', PostListView.as_view(), name="index"),
    path('<slug:slug>', PostDetailView.as_view(), name="single_post"),
]