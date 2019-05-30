from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('blog/', include('bfblog.urls')),
    path('paste/', include('bfpaste.urls')),
    path('admin/', admin.site.urls),
]
