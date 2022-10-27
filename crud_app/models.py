from datetime import date
from authentication.models import ExtendUser
from django.db import models
from .validators import *

class Author(models.Model):
    author_name = models.CharField(max_length=30)
    email = models.EmailField(validators =[validate_google_mail])
    created_by = models.ForeignKey(ExtendUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.author_name


class Blog(models.Model):
    blog_name = models.CharField(max_length=100, blank=True, null=True)
    tagline = models.TextField(null=True)
    created_by = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.blog_name
    
class ThemeBlog(Blog):
    theme = models.CharField(max_length=200, null=True)

class Entry(models.Model):
    blog = models.ForeignKey(ThemeBlog, on_delete=models.CASCADE,null=True)
    headline = models.CharField(max_length=255, null=True)
    body_text = models.TextField(null=True)
    pub_date = models.DateField(blank=True, null=True)
    mod_date = models.DateField(blank=True, null=True)
    authors = models.ManyToManyField(Author, related_name='entry')
    number_of_comments = models.IntegerField(default=0, null=True)
    number_of_pingbacks = models.IntegerField(default=0, null=True)
    rating = models.IntegerField(default=0, null=True)
    created_by = models.ForeignKey(ExtendUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.headline

class Test(Entry):
    pass
