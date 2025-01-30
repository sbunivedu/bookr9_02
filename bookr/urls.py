from django.contrib import admin
from reviews.admin import admin_site
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookradmin/', admin_site.urls),
]