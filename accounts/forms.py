# type: ignore
import uuid
import os
from PIL import Image
from io import BytesIO

from django.core.files.uploadedfile import SimpleUploadedFile
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext as _
import cloudinary.uploader

from socialmedia import settings
from accounts.models import User


class SingUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.auth_token = str(uuid.uuid4())
        user.hash = str(uuid.uuid4())
        user.is_active = False

        if commit:
            user.save()

        return user


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            "image",
            "photo",
            "first_name",
            "last_name",
            "bio",
            "location",
            "gender",
            "birth_date",
        )

    def cloudinaryCheck(self, image, user):
        try:
            # Thumbnail
            THUMBNAIL_SIZE = (160, 160)  # dimensions
            picture = Image.open(image)
            # Convert to RGB if necessary
            if picture.mode not in ("L", "RGB"):
                picture = picture.convert("RGB")
            # Create a thumbnail and use antialiasing for a smoother thumbnail
            try:
                picture.thumbnail(THUMBNAIL_SIZE, Image.Resampling.LANCZOS)
            except Exception as e:
                print("ERROR:", e)
            # Fetch image into memory
            temp_handle = BytesIO()
            picture.save(temp_handle, "png")
            temp_handle.seek(0)
            # Remove old image from Cloudinary if not default
            if hasattr(user.image, "public_id") and user.image.public_id != "profile":
                try:
                    cloudinary.uploader.destroy(user.image.public_id)
                except Exception as e:
                    print("ERROR:", e)
            if hasattr(user.photo, "public_id") and user.photo.public_id != "profile":
                try:
                    cloudinary.uploader.destroy(user.photo.public_id)
                except Exception as e:
                    print("ERROR:", e)
            # Rename new image
            image.name = f"{user.username}.png"
            # Save new image
            file_name, file_ext = os.path.splitext(image.name)
            suf = SimpleUploadedFile(
                file_name + file_ext, temp_handle.read(), content_type="image/png"
            )
            self.instance.photo = suf
            self.instance.image = image
        except Exception as e:
            print(e)
            self.add_error(
                "image", _("Could not create thumbnail. Is the file type valid?")
            )

    def localCheck(self, image, user):
        try:
            # Thumbnail
            THUMBNAIL_SIZE = (160, 160)  # dimensions
            picture = Image.open(image)
            # Convert to RGB if necessary
            if picture.mode not in ("L", "RGB"):
                picture = picture.convert("RGB")
            # Create a thumbnail and use antialiasing for a smoother thumbnail
            try:
                picture.thumbnail(THUMBNAIL_SIZE, Image.Resampling.LANCZOS)
            except Exception as e:
                print("ERROR:", e)
            # Fetch image into memory
            temp_handle = BytesIO()
            picture.save(temp_handle, "png")
            temp_handle.seek(0)
            # Remove old image
            if user.image.name != "profile.png":
                try:
                    os.remove(user.image.path)
                except Exception as e:
                    print("ERROR:", e)
            if user.photo.name != "profile.png":
                try:
                    os.remove(user.photo.path)
                except Exception as e:
                    print("ERROR:", e)
            # Rename new image
            try:
                os.remove(
                    f"{settings.MEDIA_ROOT}\\uploads\\profile\\{user.username}.png"
                )
            except Exception as e:
                print("ERROR:", e)
            image.name = f"{user.username}.png"
            # Save new image
            file_name, file_ext = os.path.splitext(image.name)
            suf = SimpleUploadedFile(
                file_name + file_ext, temp_handle.read(), content_type="image/png"
            )
            self.instance.photo = suf
            self.instance.image = image
        except Exception as e:
            print(e)
            self.add_error(
                "image", _("Could not create thumbnail. Is the file type valid?")
            )

    def init(self, user):
        image = self.cleaned_data.get("image")
        if image == user.image:
            pass
        elif image.size > 4 * 1024 * 1024:
            self.add_error("image", _("Uploading files more than 4MB is not allowed."))
        else:
            # TODO: Switch if you are in Local
            # self.localCheck(image, user)
            self.cloudinaryCheck(image, user)


class LogInForm(AuthenticationForm):

    def confirm_login_allowed(self, user):
        if not user.is_active:
            self.add_error("username", _("Please verify your email!"))

        return super().confirm_login_allowed(user)
