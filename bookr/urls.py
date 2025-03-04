from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin, auth
from django.urls import include, path
import reviews.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        "accounts/", include(("django.contrib.auth.urls", "auth"), namespace="accounts")
    ),
    path(
        "accounts/password_reset/done/",
        auth.views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "accounts/reset/done/",
        auth.views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("", reviews.views.index),
    path("book-search/", reviews.views.book_search, name="book_search"),
    path("", include("reviews.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
