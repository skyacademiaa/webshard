"""
URL Configuration for Tech Service project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from apps.seo.sitemaps import sitemaps_dict

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Apps
    path('', include('apps.core.urls')),
    path('services/', include('apps.services.urls')),
    path('portfolio/', include('apps.portfolio.urls')),
    path('pricing/', include('apps.pricing.urls')),
    path('blog/', include('apps.blog.urls')),
    path('about/', include('apps.about.urls')),
    path('contact/', include('apps.contact.urls')),
    path('quote/', include('apps.quote.urls')),

    # SEO
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps_dict}, name='django.contrib.sitemaps.views.sitemap'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
