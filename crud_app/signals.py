from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Entry, Blog

@receiver(post_save, sender=Blog)
def entry(sender, instance, created, **kwrgs):
    print('working')
    #if created:
        
        #Entry.objects.create(blog=instance)

