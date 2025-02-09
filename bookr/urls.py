import reviews.views
from reviews.admin import admin
from django.urls import include, path
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", reviews.views.index),
    path("book-search/", reviews.views.book_search, name="book_search"),
    path("", include("reviews.urls")),
]