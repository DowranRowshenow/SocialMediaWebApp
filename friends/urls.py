from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('friend_request/', views.FriendRequestView.as_view(), name="friend_request"),
    path('friend_request_accept/<int:id>/', views.FriendRequestAcceptView.as_view(), name="friend_request_accept"),
    path('friend_request_cancel/<int:id>/', views.FriendRequestCancelView.as_view(), name="friend_request_cancel"),
    path('friend_request_decline/<int:id>/', views.FriendRequestDeclineView.as_view(), name="friend_request_decline"),
]