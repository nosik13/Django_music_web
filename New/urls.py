"""Здесь происходит оглавление url страниц New"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('see_app.urls'), name='see_app'),
]
