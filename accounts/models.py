from django.db import models
from django.contrib.auth.models import AbstractUser

from cloudinary.models import CloudinaryField


MALE = "MALE"
FEMALE = "FEMALE"
NONE = "NONE"

GENDER_CHOICES = ((MALE, "Male"), (FEMALE, "Female"), (NONE, "None"))


class User(AbstractUser):
    email = models.EmailField(("email address"), unique=True)
    auth_token = models.CharField(max_length=100, unique=True)
    hash = models.CharField(max_length=36, unique=True)
    # image = models.ImageField(upload_to="uploads/profile/", default="profile.jpg")
    image = CloudinaryField("image", folder="uploads/profile/", default="profile.jpg")
    """
    photo = models.ImageField(
       upload_to="uploads/profile/compressed/", default="profile.jpg"
    )
    """
    photo = CloudinaryField(
        "image", folder="uploads/profile/compressed/", default="profile.jpg"
    )
    is_online = models.BooleanField(default=False)  # type: ignore
    bio = models.TextField(max_length=250, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, default=NONE)
    location = models.CharField(max_length=50, blank=True)

    REQUIRED_FIELDS = [
        "email",
    ]

    def __str__(self):
        return self.email
