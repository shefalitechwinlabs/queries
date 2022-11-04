from django.db.models.signals import post_save
from django.dispatch import receiver
from authentication.models import Profile
from .models import ExtendUser


@receiver(post_save, sender=ExtendUser)
def profile(sender, instance, created, **kwrgs):
    if created:
        Profile.objects.create(name=instance)
