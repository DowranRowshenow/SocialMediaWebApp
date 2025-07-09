from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [
    path("", views.MainView.as_view(), name="index"),
    path(
        "profile/", login_required(views.UserProfileView.as_view()), name="user_profile"
    ),
    path(
        "<int:pk>/profiles/",
        login_required(views.ProfileView.as_view()),
        name="profile",
    ),
]
