from http import HTTPStatus
from random import choices
from string import ascii_lowercase, ascii_letters, digits

from django.test import TestCase
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import AbstractUser

from myauth.models import UserModel


class LoginTestCase(TestCase):
    url = reverse_lazy("myauth:login")
    only_auth_url = reverse_lazy("items:create")

    def setUp(self) -> None:
        password = "".join(choices(ascii_letters + digits, k=10))
        username = "".join(choices(ascii_lowercase, k=8))
        user: AbstractUser = UserModel.objects.create_user(username=username, password=password)
        self.user = user
        self.password = password

    def test_login(self):
        resp_auth = self.client.post(
            self.url,
            {
                "username": self.user.username,
                "password": self.password,
            },
        )

        self.assertEqual(resp_auth.url, reverse("myauth:me"))
        response_page = self.client.get(resp_auth.url)
        user = response_page.context["user"]
        self.assertFalse(user.is_anonymous)
        self.assertEqual(user.username, self.user.username)

    def test_anon_access_to_only_auth_page_is_restricted(self):
        response = self.client.get(self.only_auth_url)
        self.assertNotEqual(response.status_code, HTTPStatus.OK)

    def test_authorized_access_to_only_auth_page(self):
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.get(self.only_auth_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
