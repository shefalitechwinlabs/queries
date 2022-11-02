from django import template
from crud_app.models import *
from authentication.models import ExtendUser
from time import strftime  

register = template.Library()


@register.simple_tag()
def blog_count(value):
    blog = Blog.objects.filter(created_by=value)
    return blog.count()

register.filter('blog_count', blog_count)

@register.inclusion_tag('main/index.html')
def show_latest_blog(user,number=1):
    blog_obj = Blog.objects.filter(created_by=user).order_by('-id')[:number]
    entry_obj= Entry.objects.filter(blog=blog_obj).order_by('-id')[:number]
    context = {'blog_obj': blog_obj, 'entry_obj':entry_obj}
    return context