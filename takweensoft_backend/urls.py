"""
URL configuration for takweensoft_backend project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('content_management.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Customize admin site headers
admin.site.site_header = "Takween Soft Admin"
admin.site.site_title = "Takween Soft Admin Portal"
admin.site.index_title = "Welcome to Takween Soft Administration"
