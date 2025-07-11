from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings

# from django.conf.urls import url
from django.conf.urls.static import static
from main import views

urlpatterns = (
    [
        # url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
        # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
        path("", include("main.urls")),
        path("mod/", admin.site.urls),
        path("accounts/", include("accounts.urls")),
        path("posts/", include("posts.urls")),
        path("friends/", include("friends.urls")),
        path("rooms/", include("rooms.urls")),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + [
        re_path(r"^(?P<path>.*)$", views.redirect_unknown_url),
    ]
)
