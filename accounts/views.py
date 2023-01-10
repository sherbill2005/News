from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView


# Create your views here.
class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")
    template_name = "registration/signup.html"


class PasswordchangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "registration/passwordchange.html"
    success_url = reverse_lazy("passdone")


class PasswordDone(PasswordChangeDoneView):
    template_name = "registration/passdone.html"
    success_url = "/"

