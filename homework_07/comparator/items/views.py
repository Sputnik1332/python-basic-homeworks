from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from .models import Item
# from .tasks import parse


def index(request: HttpRequest):
    context = {
        "items": Item.objects.order_by("pk").all()
    }
    return render(request=request, template_name="items/index.html", context=context)


def details(request: HttpRequest, pk: int):
    context = {
        "item": get_object_or_404(Item, pk=pk),
    }

    price = parse.delay(Item.url)

    return render(request=request, template_name="items/details.html", context=context)
