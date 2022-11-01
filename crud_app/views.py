from django.shortcuts import render, redirect
from django.http import HttpResponse
from crud_app.models import *
from authentication.models import Profile, ExtendUser
from django.shortcuts import get_object_or_404,render,HttpResponseRedirect
from .forms import *

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def home(request):
    if 'username' in request.session:
        user = request.user
        name = user.first_name+' '+user.last_name
        blog = Blog.objects.filter(created_by=user)
        data = blog.values()[3]
        print(type(data['blog_name']))
        return render(request, 'main/home.html', {'name':name, 'value':data['blog_name']})
    else:
        return redirect('/')

def profile(request):
    if 'username' in request.session:
        context = {}
        profile = Profile.objects.get(name=request.user)
        fullname = profile.name.first_name +' '+ profile.name.last_name
        context = {'dataset': profile, 'fullname': fullname}
        return render(request, 'main/profile.html', context)

def blogform(request):
    if 'username' in request.session:
        context = {}
        context = {'blog': BlogForm}
        if request.method == 'POST':
            blog_form = BlogForm(request.POST)
            if blog_form.is_valid():
                blog = blog_form.save(commit=False)
                blog.created_by = request.user
                blog.save()
                return render(request, 'form/blogform.html', context)
            else:
                context['blog'] = blog_form
            return render(request, 'form/blogform.html', context)
        return render(request, 'form/blogform.html', context)
    else:
        return redirect('/')

def article(request, blog_name):
    user =  request.user
    article =  Blog.objects.filter(blog_name=blog_name)
    context = {'article':article}
    return render(request, 'main/article.html', context)

def table(request):
    user = request.user
    entry = Entry.objects.filter(created_by=user)
    #blog = Blog.objects.filter(created_by=user)
    #data = blog, entry
    context = {'data':entry}
    return render(request, 'main/table.html', context)

def delete(request,id):
    obj = get_object_or_404(Entry, id = id)
    object = obj.blog.delete()
    return redirect("/home/table/")

def update_table(request, id):
    objects = get_object_or_404(Entry,id=id) 
    object = objects.blog
    if request.method=="POST":
        blog_name = request.POST["blog_name"]
        headline = request.POST["headline"]
        body_text = request.POST["body_text"]
        object.blog_name = blog_name
        object.headline = headline
        object.body_text = body_text
        object.save()
        return HttpResponseRedirect("/home/table/")
    data = {}
    data = {"dataset":object}
    # print(object.body_text)
    return render(request, "main/update.html", data)
