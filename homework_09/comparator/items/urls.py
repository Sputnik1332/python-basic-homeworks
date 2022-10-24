from django.urls import path

from .views import (
    ItemsListView,
    ItemDetailView,
    ItemCreateView
)

app_name = "items"

urlpatterns = [
    path("", ItemsListView.as_view(), name="index"),
    path("create/", ItemCreateView.as_view(), name="create"),
    path("<int:pk>/", ItemDetailView.as_view(), name="details"),
]
