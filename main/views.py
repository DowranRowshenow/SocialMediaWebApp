# type: ignore
from django.views.generic import TemplateView, DetailView, View
from django.shortcuts import HttpResponseRedirect, redirect
from django.urls import reverse

from accounts.models import User
from friends.models import FriendList, FriendRequest


def redirect_unknown_url(request, path=None):
    """
    Redirects any unknown URL to the homepage.
    """
    return redirect(
        reverse("posts")
    )  # Replace 'home_page_name' with the actual name of your homepage URL pattern
    # Or, to redirect to a specific static URL:
    # return redirect('/')


def context(self, context):
    try:
        context["friends"] = (
            FriendList.objects.filter(user=self.request.user).first().friends.all()
        )
    except Exception:
        context["friends"] = list()
    context["friend_requests"] = FriendRequest.objects.filter(
        receiver=self.request.user, is_active=True
    ).order_by("sender__username")
    context["requested_friends"] = FriendRequest.objects.filter(
        sender=self.request.user, is_active=True
    ).order_by("sender__username")
    return context


class MainView(View):

    def get(self, request):
        return HttpResponseRedirect(reverse("posts"))


class UserProfileView(TemplateView):
    template_name = "main/profile.html"
    context_object_name = "user"

    def get_queryset(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        return context(self, super().get_context_data(**kwargs))


class ProfileView(DetailView):
    model = User
    template_name = "main/profile.html"
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        return context(self, super().get_context_data(**kwargs))
