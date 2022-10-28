from datetime import date
from authentication.models import ExtendUser
from django.db import models
from .validators import *

class Blog(models.Model):
    blog_name = models.CharField(max_length=100, blank=True, null=True)
    headline = models.CharField(max_length=255, null=True)
    body_text = models.TextField(null=True)
    created_by = models.ForeignKey(ExtendUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.blog_name

class Entry(models.Model):
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE,null=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    mod_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.blog
