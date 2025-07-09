# type: ignore
from django.views.generic import ListView, FormView
from django.db.models import Q
from django.shortcuts import redirect
from django.contrib import messages
import uuid

from accounts.models import User
from main.views import context
from rooms.models import Message, Room
from rooms.forms import MessageForm


class DirectMessageView(ListView):
    template_name = "rooms/room.html"
    context_object_name = "messages"
    paginate_by = 100
    roomToken = None

    def get_queryset(self):
        friend = User.objects.filter(hash=self.kwargs["friend_hash"]).first()

        if not friend:
            # Friend doesn't exist
            return Message.objects.none()

        # Check if room exists
        room = Room.objects.filter(
            Q(user1=self.request.user, user2=friend)
            | Q(user1=friend, user2=self.request.user)
        ).first()

        if room:
            self.roomToken = room.token
        else:
            # Create a new room if it doesn't exist
            # This assumes friend requests are already accepted
            room = Room.objects.create(
                user1=self.request.user, user2=friend, token=str(uuid.uuid4())
            )
            self.roomToken = room.token

        return Message.objects.filter(room=room).order_by("id")

    def get_context_data(self, **kwargs):
        ctx = context(self, super().get_context_data(**kwargs))
        print(f"roomToken: {self.roomToken}")
        ctx["roomToken"] = self.roomToken
        return ctx


class SendMessageView(FormView):
    form_class = MessageForm
    template_name = "rooms/room.html"

    def form_valid(self, form):
        try:
            # Get the room token from form data
            room_token = form.cleaned_data.get("roomToken")
            content = form.cleaned_data.get("content")

            if not room_token:
                messages.error(self.request, "Room token is missing")
                return redirect(self.request.META.get("HTTP_REFERER"))

            # Get the room
            room = Room.objects.get(token=room_token)

            # Create the message
            Message.objects.create(room=room, sender=self.request.user, content=content)

            return redirect(self.request.META.get("HTTP_REFERER"))
        except Room.DoesNotExist:
            messages.error(self.request, "Room not found")
            return redirect(self.request.META.get("HTTP_REFERER"))
        except Exception as e:
            messages.error(self.request, f"Error sending message: {str(e)}")
            return redirect(self.request.META.get("HTTP_REFERER"))
