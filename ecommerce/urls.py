from django.contrib import admin
from django.urls import path

from core.views import frontpage, about


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('about', about, name='about'),
]
