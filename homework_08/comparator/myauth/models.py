from typing import TYPE_CHECKING

from django.contrib.auth import get_user_model
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


UserModel: AbstractUser = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name="profile")
    email = models.TextField(blank=True)

    if TYPE_CHECKING:
        objects: models.Manager


@receiver(signal=post_save, sender=UserModel)
def user_saved_hadler(instance: UserModel, created: bool, **kwargs):
    if not created:
        return

    UserProfile.objects.create(user=instance)
