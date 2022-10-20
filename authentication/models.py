from django.db import models


class Signup(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    bio_desc = models.TextField()
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name