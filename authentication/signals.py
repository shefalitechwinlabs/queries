from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from authentication.models import Profile
import django.dispatch
from .models import ExtendUser


# def save_post(sender, instance, **kwargs):
#     print("save is working")

# post_save.connect(save_post, sender=Author)

#mysignal = django.dispatch.Signal()

# @receiver(mysignal)
# def func(sender, **kwargs):
#     print("\nhello\n", kwargs)

@receiver(post_save, sender=ExtendUser)
def profile(sender, instance, created, **kwrgs):
    if created:
        Profile.objects.create(name=instance)

