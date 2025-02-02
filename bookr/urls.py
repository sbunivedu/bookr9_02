from reviews.admin import admin
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
   # path('bookradmin/', admin.site.urls),
]