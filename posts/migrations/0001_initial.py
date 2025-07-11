# Generated by Django 3.2.15 on 2022-10-14 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="PostComment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField(max_length=250)),
                ("likes", models.IntegerField(default=0)),
                ("dislikes", models.IntegerField(default=0)),
                ("sent_date_time", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post_comment_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("hash", models.CharField(max_length=36, unique=True)),
                ("content", models.TextField(blank=True, max_length=250)),
                ("image", models.ImageField(blank=True, upload_to="uploads/posts/")),
                ("update_date_time", models.DateTimeField(auto_now=True)),
                ("created_date_time", models.DateTimeField(auto_now_add=True)),
                (
                    "comments",
                    models.ManyToManyField(
                        blank=True, related_name="comments", to="posts.PostComment"
                    ),
                ),
                (
                    "disliked_users",
                    models.ManyToManyField(
                        related_name="post_disliked_user", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "liked_users",
                    models.ManyToManyField(
                        related_name="post_liked_user", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
