from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [
    path(
        "dm/<friend_hash>/",
        login_required(views.DirectMessageView.as_view()),
        name="dm",
    ),
    path(
        "send_message/",
        login_required(views.SendMessageView.as_view()),
        name="send_message",
    ),
]
