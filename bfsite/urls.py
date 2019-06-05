from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect


def index(req):
    return redirect('Blog:index')

urlpatterns = [
    path('', index, name="index"),
    path('blog/', include('bfblog.urls' , namespace="Blog")),
    path('paste/', include('bfpaste.urls', namespace="Paste")),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)