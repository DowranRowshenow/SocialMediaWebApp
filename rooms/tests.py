# type: ignore
from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User
from .models import Room, Message
from .forms import MessageForm

# Create your tests here.


class RoomModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username="user1",
            email="user1@example.com",
            password="pass",
            auth_token="token1",
            hash="hash1",
        )
        self.user2 = User.objects.create_user(
            username="user2",
            email="user2@example.com",
            password="pass",
            auth_token="token2",
            hash="hash2",
        )
        self.room = Room.objects.create(
            user1=self.user1, user2=self.user2, token="token123"
        )

    def test_str(self):
        self.assertEqual(str(self.room), "token123")


class MessageModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username="user1",
            email="user1@example.com",
            password="pass",
            auth_token="token3",
            hash="hash3",
        )
        self.user2 = User.objects.create_user(
            username="user2",
            email="user2@example.com",
            password="pass",
            auth_token="token4",
            hash="hash4",
        )
        self.room = Room.objects.create(
            user1=self.user1, user2=self.user2, token="token123"
        )
        self.message = Message.objects.create(
            room=self.room, sender=self.user1, content="Hello!"
        )

    def test_str(self):
        self.assertEqual(str(self.message), self.user1.email)


class MessageFormTest(TestCase):
    def test_form_fields(self):
        form = MessageForm()
        self.assertIn("content", form.fields)
        self.assertIn("roomToken", form.fields)


class RoomsViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(
            username="user1",
            email="user1@example.com",
            password="pass",
            is_active=True,
            auth_token="token5",
            hash="hash5",
        )
        self.user2 = User.objects.create_user(
            username="user2",
            email="user2@example.com",
            password="pass",
            is_active=True,
            auth_token="token6",
            hash="hash6",
        )
        self.client.login(username="user1", password="pass")

    def test_direct_message_view(self):
        url = reverse("dm", args=[self.user2.hash])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "rooms/room.html")
