from django.shortcuts import render

from django.contrib.auth.views import (
    LoginView as LoginViewGeneric,
    LogoutView as LogoutViewGeneric,
)
from django.views.generic import TemplateView
from django.urls import reverse_lazy


class MeView(TemplateView):
    template_name = "myauth/me.html"


class LoginView(LoginViewGeneric):
    next_page = reverse_lazy("myauth:me")


class LogoutView(LogoutViewGeneric):
    next_page = reverse_lazy("myauth:me")
