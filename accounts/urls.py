from django.urls import path
from .views import SignupView, PasswordchangeView, PasswordDone
urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("password/", PasswordchangeView.as_view(), name="password_change"),
    path("passdone/", PasswordDone.as_view(), name="passdone"),

]