from django.conf import settings
from django.conf.urls.static import static 
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include("posts.urls", namespace='posts')),
    url(r'^',include("personal.urls", namespace='personal')),
    url(r'^',include("mlworkshop.urls", namespace='mlworkshop')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)