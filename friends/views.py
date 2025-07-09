from django.views.generic import View, FormView
from django.shortcuts import redirect, HttpResponseRedirect
from django.urls import reverse

from asgiref.sync import async_to_sync
#from channels.layers import get_channel_layer

from accounts.models import User
from .forms import FriendRequestForm
from .models import FriendList, FriendRequest


class FriendRequestView(FormView):
    form_class = FriendRequestForm

    def form_valid(self, form):
        form.init(self.request.user)
        """
        channel_layer = get_channel_layer()
        if friend_request:
            async_to_sync(channel_layer.group_send)(f'friends_{friend_request.receiver.username}',{
                "type": "friend_request",
                "sender_hash": friend_request.sender.hash,
                "sender_username": friend_request.sender.username,
                "sender_email": friend_request.sender.email,
                "sender_image": friend_request.sender.photo.url,
                "receiver_email": friend_request.receiver.email,
                "receiver_image": friend_request.receiver.photo.url
            })
        """
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class FriendRequestAcceptView(View):
    
    def get(self, request, id):
        #channel_layer = get_channel_layer()
        friend = User.objects.filter(id=id).first()
        if friend:
            friend_request = FriendRequest.objects.filter(sender=friend, receiver=request.user).first()
            if friend_request:
                friend_request.accept()
                """
                async_to_sync(channel_layer.group_send)(f'friends_{friend_request.sender.username}',{
                    "type": "friend_accept",
                    "email": friend_request.receiver.email,
                    "username": friend_request.receiver.username
                })
                """
        try:
            return redirect(request.META.get('HTTP_REFERER'))
        except:
            return HttpResponseRedirect(reverse('main'))


class FriendRequestCancelView(View):
    
    def get(self, request, id):
        #channel_layer = get_channel_layer()
        friend = User.objects.filter(id=id).first()
        if friend:
            friend_request = FriendRequest.objects.filter(sender=request.user, receiver=friend).first()
            if friend_request:
                friend_request.cancel()
                """
                async_to_sync(channel_layer.group_send)(f'friends_{friend_request.receiver.username}',{
                    "type": "friend_cancel",
                    "email": friend_request.sender.email,
                    "username": friend_request.sender.username
                })
                """
        try:
            return redirect(request.META.get('HTTP_REFERER'))
        except:
            return HttpResponseRedirect(reverse('main'))


class FriendRequestDeclineView(View):
    
    def get(self, request, id):
        #channel_layer = get_channel_layer()
        friend = User.objects.filter(id=id).first()
        if friend:
            friend_request = FriendRequest.objects.filter(sender=friend, receiver=request.user).first()
            if friend_request:
                friend_request.decline()
                """
                async_to_sync(channel_layer.group_send)(f'friends_{friend_request.sender.username}',{
                    "type": "friend_decline",
                    "email": friend_request.receiver.email,
                    "username": friend_request.receiver.username
                })
                """
        try:
            return redirect(request.META.get('HTTP_REFERER'))
        except:
            return HttpResponseRedirect(reverse('main'))