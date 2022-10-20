from datetime import date
from django.contrib.auth.models import User
from django.db import models

class Author(models.Model):
    author_name = models.CharField(max_length=200)
    email = models.EmailField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.author_name


class Blog(models.Model):
    blog_name = models.CharField(max_length=100)
    tagline = models.TextField()
    created_by = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.blog_name
    
class ThemeBlog(Blog):
    theme = models.CharField(max_length=200)

class Entry(models.Model):
    blog = models.ForeignKey(ThemeBlog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField(blank=True, null=True)
    mod_date = models.DateField(blank=True, null=True)
    authors = models.ManyToManyField(Author, related_name='entry')
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.headline

class Test(Entry):
    pass
