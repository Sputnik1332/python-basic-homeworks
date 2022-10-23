from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)

from .forms import ItemCreateForm
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


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemCreateForm

    def get_success_url(self):
        return reverse("items:details", kwargs={"pk": self.object.pk})


class ItemDetailView(DetailView):
    template_name = "items/details.html"
    context_object_name = "item"
    queryset = (
        Item
        .objects
        # .select_related("market")
        # .prefetch_related("label")
    )
