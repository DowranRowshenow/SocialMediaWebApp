from django.urls import path

import posts.consumers
import friends.consumers
import rooms.consumers


websocket_urlpatterns = [
    path('ws/rooms/<str:room_name>/', rooms.consumers.ChatConsumer.as_asgi()),
    path('ws/friends/<str:room_name>/', friends.consumers.FriendConsumer.as_asgi()),
    path('ws/posts/<str:room_name>/', posts.consumers.PostCommentConsumer.as_asgi()),
]