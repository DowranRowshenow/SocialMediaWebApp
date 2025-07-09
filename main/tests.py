# type: ignore
from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User

# Create your tests here.


class MainViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass",
            is_active=True,
            auth_token="token1",
            hash="hash1",
        )

    def test_main_view_redirects(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("index"), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/posts.html")

    def test_user_profile_view(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("user_profile"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/profile.html")

    def test_profile_view(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("profile", args=[self.user.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/profile.html")
