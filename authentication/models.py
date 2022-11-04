from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Max, F


class ExtendUser(AbstractUser):
    bio_desc = models.TextField()

    def __str__(self):
        return self.username

class Profile(models.Model):
    name = models.OneToOneField(ExtendUser,on_delete=models.CASCADE, null=True)

    def __str__(self):
        fullname = self.name.first_name + self.name.last_name
        return fullname
