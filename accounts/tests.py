# type: ignore
from django.urls import reverse
from django.test import TestCase, Client
from .models import User
from .forms import SingUpForm, LogInForm, EditProfileForm


class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass",
            auth_token="token1",
            hash="hash1",
        )
        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("testpass"))
        self.assertEqual(str(user), "test@example.com")


class SignupFormTest(TestCase):
    def test_signup_form_valid(self):
        form = SingUpForm(
            data={
                "username": "testuser",
                "email": "test@example.com",
                "password1": "testpass123",
                "password2": "testpass123",
            }
        )
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertFalse(user.is_active)
        self.assertIsNotNone(user.auth_token)

    def test_signup_form_password_mismatch(self):
        form = SingUpForm(
            data={
                "username": "testuser",
                "email": "test@example.com",
                "password1": "testpass123",
                "password2": "wrongpass",
            }
        )
        self.assertFalse(form.is_valid())


class LoginFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass",
            is_active=True,
            auth_token="token2",
            hash="hash2",
        )

    def test_login_form_valid(self):
        form = LogInForm(data={"username": "testuser", "password": "testpass"})
        self.assertTrue(form.is_valid())


class EditProfileFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass",
            auth_token="token3",
            hash="hash3",
        )

    def test_edit_profile_form_valid(self):
        form = EditProfileForm(
            data={
                "first_name": "Test",
                "last_name": "User",
                "bio": "Hello",
                "location": "World",
                "gender": "NONE",
            },
            instance=self.user,
        )
        self.assertTrue(form.is_valid())


class AccountsViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass",
            is_active=True,
            auth_token="token4",
            hash="hash4",
        )

    def test_login_view_get(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_signup_view_get(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("logout"), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login.html")
