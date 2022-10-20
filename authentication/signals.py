from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from crud_app.models import Author
import django.dispatch
from django.core.signals import request_finished
from django.contrib.auth.models import User
from django.dispatch import receiver


def save_post(sender, instance, **kwargs):
    print("save is working")

post_save.connect(save_post, sender=Author)

mysignal = django.dispatch.Signal()

@receiver(mysignal)
def func(sender, **kwargs):
    print("\nhello\n", kwargs)

@receiver(post_save, sender=User)
def profile(sender, instance, created, **kwrgs):
    if created:
        Author.objects.create(author_name=instance)