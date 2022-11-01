from django.db.models.signals import post_save
from django.dispatch import receiver
from crud_app.models import Entry, Blog
from authentication.models import ExtendUser

@receiver(post_save, sender=Blog)
def entry(sender, instance, created, **kwrgs):
    if created:
        user = instance.created_by
        Entry.objects.create(blog=instance, created_by=user)


