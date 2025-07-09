# type: ignore
from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User
from .models import Post, PostComment
from .forms import CreatePostForm

# Create your tests here.


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass",
            auth_token="token1",
            hash="hash1",
        )
        self.post = Post.objects.create(
            user=self.user, hash="hash2", content="Hello world"
        )

    def test_str(self):
        self.assertEqual(str(self.post), self.user.email)

    def test_add_comment(self):
        comment = PostComment.objects.create(user=self.user, content="Nice post!")
        self.post.add_comment(comment)
        self.assertIn(comment, self.post.comments.all())

    def test_add_liked_user(self):
        self.post.add_liked_user(self.user)
        self.assertIn(self.user, self.post.liked_users.all())

    def test_add_disliked_user(self):
        self.post.add_disliked_user(self.user)
        self.assertIn(self.user, self.post.disliked_users.all())


class CreatePostFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass",
            auth_token="token3",
            hash="hash3",
        )

    def test_form_valid_without_image(self):
        form = CreatePostForm(data={"content": "Test post"})
        self.assertTrue(form.is_valid())


class PostsViewsTest(TestCase):
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
        self.client.login(username="testuser", password="testpass")
        self.post = Post.objects.create(
            user=self.user, hash="hash5", content="Hello world"
        )

    def test_posts_list_view(self):
        response = self.client.get(reverse("posts"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/posts.html")

    def test_post_detail_view(self):
        response = self.client.get(reverse("post_detail", args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/post_detail.html")
