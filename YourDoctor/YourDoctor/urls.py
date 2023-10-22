from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('medicalapp.urls')),
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(settings.BASE_DIR, 'static_root')
