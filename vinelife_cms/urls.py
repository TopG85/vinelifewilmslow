"""
URL configuration for vinelife_cms project with Wagtail CMS.
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    
    # Wagtail pages (must be last)
    re_path(r'', include(wagtail_urls)),
]

# Serve media and static files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Serve from STATICFILES_DIRS (assets folder)
    for directory in settings.STATICFILES_DIRS:
        urlpatterns += static(settings.STATIC_URL, document_root=directory)
    # Fallback to STATIC_ROOT
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
