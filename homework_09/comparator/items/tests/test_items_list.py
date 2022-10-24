from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse_lazy

from items.models import Item


class ItemsListTestCase(TestCase):

    fixtures = [
        "items.fixture.json",
    ]

    url = reverse_lazy("items:index")

    def test_list_items(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, HTTPStatus.OK)

        items = (
            Item
            .objects
            # .select_related("market")
            # .prefetch_related("label")
            .order_by("pk")
        .all()
        )

        items_in_context = response.context["items"]
        self.assertEqual(len(items), len(items_in_context))
        for i1, i2 in zip(items, items_in_context):
            self.assertEqual(i1.pk, i2.pk)

    def test_anonymous_access(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.context["user"].is_anonymous)
