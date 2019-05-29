from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('paste/', include('bfpaste.urls')),
    path('admin/', admin.site.urls),
]
