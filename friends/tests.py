# type: ignore
from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User
from .models import FriendList, FriendRequest
from .forms import FriendRequestForm


class FriendListModelTest(TestCase):
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
        self.friend_list = FriendList.objects.create(user=self.user1)

    def test_add_and_remove_friend(self):
        self.friend_list.add_friend(self.user2)
        self.assertIn(self.user2, self.friend_list.friends.all())
        self.friend_list.remove_friend(self.user2)
        self.assertNotIn(self.user2, self.friend_list.friends.all())

    def test_is_mutual_friend(self):
        self.friend_list.add_friend(self.user2)
        self.assertTrue(self.friend_list.is_mutual_friend(self.user2))


class FriendRequestModelTest(TestCase):
    def setUp(self):
        self.sender = User.objects.create_user(
            username="sender",
            email="sender@example.com",
            password="pass",
            auth_token="token3",
            hash="hash3",
        )
        self.receiver = User.objects.create_user(
            username="receiver",
            email="receiver@example.com",
            password="pass",
            auth_token="token4",
            hash="hash4",
        )
        self.friend_request = FriendRequest.objects.create(
            sender=self.sender, receiver=self.receiver
        )

    def test_accept(self):
        self.friend_request.accept()
        self.assertFalse(self.friend_request.is_active)
        self.assertTrue(
            FriendList.objects.get(user=self.sender).is_mutual_friend(self.receiver)
        )

    def test_decline(self):
        self.friend_request.decline()
        self.assertFalse(
            FriendRequest.objects.filter(pk=self.friend_request.pk).exists()
        )

    def test_cancel(self):
        self.friend_request.cancel()
        self.assertFalse(
            FriendRequest.objects.filter(pk=self.friend_request.pk).exists()
        )


class FriendRequestFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="user",
            email="user@example.com",
            password="pass",
            auth_token="token5",
            hash="hash5",
        )
        self.friend = User.objects.create_user(
            username="friend",
            email="friend@example.com",
            password="pass",
            auth_token="token6",
            hash="hash6",
        )

    def test_valid_friend_request(self):
        form = FriendRequestForm(data={"email": "friend@example.com"})
        form.is_valid()
        form.init(self.user)
        self.assertTrue(
            FriendRequest.objects.filter(
                sender=self.user, receiver=self.friend
            ).exists()
        )

    def test_cannot_send_to_self(self):
        form = FriendRequestForm(data={"email": "user@example.com"})
        form.is_valid()
        form.init(self.user)
        self.assertIn("email", form.errors)


class FriendsViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="user",
            email="user@example.com",
            password="pass",
            is_active=True,
            auth_token="token7",
            hash="hash7",
        )
        self.friend = User.objects.create_user(
            username="friend",
            email="friend@example.com",
            password="pass",
            is_active=True,
            auth_token="token8",
            hash="hash8",
        )
        self.client.login(username="user", password="pass")
        self.friend_request = FriendRequest.objects.create(
            sender=self.friend, receiver=self.user
        )

    def test_friend_request_accept_view(self):
        url = reverse("friend_request_accept", args=[self.friend.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_friend_request_cancel_view(self):
        FriendRequest.objects.create(sender=self.user, receiver=self.friend)
        url = reverse("friend_request_cancel", args=[self.friend.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_friend_request_decline_view(self):
        url = reverse("friend_request_decline", args=[self.friend.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
