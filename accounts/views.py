from django.views.generic import View
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse

from accounts.models import User
from accounts.forms import SingUpForm, LogInForm
from .forms import EditProfileForm

        
class CustomLoginView(LoginView):
    form_class = LogInForm
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse('index')


class CustomSignupView(CreateView):
    form_class = SingUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('token')

    def get_success_url(self):
        link = self.request.build_absolute_uri(reverse('verify', args=(self.object.auth_token, )))
        if not send_verification_mail(self.object, link): 
            return HttpResponseRedirect(reverse('signup'))
        return super().get_success_url()
        

def send_verification_mail(user, link):
    subject = 'Your accounts need to be verified'
    message = f"Hi click the link to verify your account {link}"
    sender = settings.EMAIL_HOST_USER
    receiver = [user.email]
    try: send_mail(subject, message, sender, receiver)
    except Exception as e: 
        print(e)

        return False
    return True

class VerifyView(View):

    def get(self, request, token):
        try:
            user = User.objects.filter(auth_token = token).first()
            if user:
                user.is_active = True
                user.save()
                messages.success(request, "Your account is verified.")
                return HttpResponseRedirect(reverse('login'))
        except Exception as e: print(e)
        return HttpResponseRedirect(reverse('error'))


class EditProfileView(UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = 'accounts/edit_profile.html'

    def form_valid(self, form):
        form.init(self.request.user)
        try: self.object = form.save()
        except: return super().form_invalid(form)
        return HttpResponseRedirect(reverse('user_profile'))


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))