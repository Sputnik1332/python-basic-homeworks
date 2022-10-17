from django.urls import path

from .views import (
    ItemsListView,
    ItemDetailView,
)

app_name = "items"

urlpatterns = [
    path("", ItemsListView.as_view(), name="index"),
    path("<int:pk>/", ItemDetailView.as_view(), name="details"),
]