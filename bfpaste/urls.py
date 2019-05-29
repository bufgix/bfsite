from django.urls import path

from .views import index, show_paste


app_name = "bfpaste"
urlpatterns = [
    path('', index, name='index'),
    path('<str:paste_id>/', show_paste, name="show_paste"),
]
