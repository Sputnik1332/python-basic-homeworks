from django.views.generic import ListView, DetailView

from .models import Item
# from .tasks import parse


class ItemsListView(ListView):
    template_name = "items/index.html"
    context_object_name = "items"
    queryset = (
        Item
        .objects
        # .select_related("market")
        # .prefetch_related("label")
        .order_by("pk")
        .all()
    )


class ItemDetailView(DetailView):
    template_name = "items/details.html"
    context_object_name = "item"
    queryset = (
        Item
        .objects
        # .select_related("market")
        # .prefetch_related("label")
    )
