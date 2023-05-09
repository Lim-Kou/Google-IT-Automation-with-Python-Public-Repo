from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from fruits import views

urlpatterns = [
    path('fruits/', views.fruits_list),
    path('upload/', views.upload_images),
    path('', views.fruits_view),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)