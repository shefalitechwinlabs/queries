from django.shortcuts import render, redirect
from django.http import HttpResponse
from crud_app.models import *
from authentication.models import Profile, ExtendUser
from django.shortcuts import get_object_or_404,render,HttpResponseRedirect
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def home(request):
    if 'username' in request.session:
        user = request.user
        name = user.first_name+' '+user.last_name
        user = request.user
        return render(request, 'main/home.html', {'name':name, 'user': user})
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
                messages.success(request, 'Blog created successfully')
                return render(request, 'form/blogform.html', context)
            else:
                context['blog'] = blog_form
                messages.error(request, 'Blog not created')
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
    paginator = Paginator(entry,15)
    page_number = request.GET.get('page')
    print(page_number)
    try:
        page_obj = paginator.get_page(page_number)
    except:
        page_obj = paginator.page(1)
    context = { 'page_obj': page_obj}
    return render(request, 'main/table.html', context)

def delete(request,id):
    obj = get_object_or_404(Entry, id = id)
    object = obj.blog.delete()
    messages.success(request, 'Blog deleted successfully')
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
        messages.success(request, 'Blog updated successfully')
        return HttpResponseRedirect("/home/table/")
    data = {}
    data = {"dataset":object}
    # print(object.body_text)
    return render(request, "main/update.html", data)
