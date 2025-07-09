from django import forms
from django.utils.translation import gettext as _

from .models import Message


class MessageForm(forms.ModelForm):
    roomToken = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Message
        fields = ("content",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].widget.attrs.update(
            {
                "class": "sender_input cur_text font_light",
                "placeholder": _("Type a message"),
            }
        )
