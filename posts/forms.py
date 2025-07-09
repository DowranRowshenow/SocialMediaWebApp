import uuid
import os

from django import forms
from django.utils.translation import gettext as _

from socialmedia import settings
from .models import Post, PostComment


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('content', 'image')

    def init(self, user): 
        image = self.cleaned_data.get("image")
        if not image:
            self.add_error("image", _("This field is required."))
        elif image.size > 4*1024*1024:
            self.add_error("image", _("Uploading files more than 4MB is not allowed."))
        else: 
            self.instance.user = user
            self.instance.hash = uuid.uuid4()
            image.name = f"{self.instance.hash}.png"
            self.instance.image = image


class EditPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('content', 'image')

    def init(self, post): 
        image = self.cleaned_data.get("image")
        postModel = Post.objects.filter(hash=post.hash).first()
        if image == postModel.image: 
            pass
        elif image.size > 4*1024*1024:
            self.add_error("image", _("Uploading files more than 4MB is not allowed."))
        else:
            try: os.remove(f"{settings.MEDIA_ROOT}\\uploads\\posts\\{post.hash}.png")
            except Exception as e: print("ERROR: ", e)
            image.name = f"{post.hash}.png"
            self.instance.image = image

class CommentForm(forms.ModelForm):

    class Meta:
        model = PostComment
        fields = ('content',)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({
            'class': 'sender_input cur_text font_light',
            'placeholder': _('Type a message')
        })