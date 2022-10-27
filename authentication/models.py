from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Max, F


class ExtendUser(AbstractUser):
    bio_desc = models.TextField()
    #password = forms.CharField(widget=forms.PasswordInput)
    #image = models.ImageField(null=True)

    def __str__(self):
        return self.username

class Profile(models.Model):
    name = models.OneToOneField(ExtendUser,on_delete=models.CASCADE, null=True)


    def save(self, *args, **kwargs):
        if not self.pk:
            max = Profile.objects.aggregate(max=Max(F('id')))['max']
            self.id = max + 1 if max else 1
        super().save(*args, **kwargs)
        