from django.shortcuts import render, redirect
from django.http import HttpResponse
from crud_app.models import *
from django.shortcuts import get_object_or_404,render,HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User



def home(request):
    if 'username' in request.session:
        return render(request, 'main/home.html')
    else:
        return redirect('/')

def form(request):
    if 'username' in request.session:
        if request.method=="POST":
            #author_name = request.POST.get("author_name")
            blog_name = request.POST["blog_name"]
            tagline = request.POST["tagline"]
            theme = request.POST["theme"]
            email = request.POST["email"]
            headline = request.POST["headline"]
            body_text = request.POST["body_text"]
            mod_date = request.POST["mod_date"]
            number_of_comments = request.POST["number_of_comments"]
            pub_date = request.POST["pub_date"]
            number_of_pingbacks = request.POST["number_of_pingbacks"]
            rating = request.POST["rating"]
            created_by = request.user
            
            A = Author(email=email,created_by=created_by)
            A.save()
            TB = ThemeBlog(blog_name=blog_name,tagline=tagline,theme=theme,created_by=A)
            TB.save()
            E = Entry(blog=TB,headline=headline,body_text=body_text,mod_date=mod_date,rating=rating,created_by=created_by,number_of_comments=number_of_comments,pub_date=pub_date,number_of_pingbacks=number_of_pingbacks)
            E.save()
            E.authors.add(A)
            E.save()
        return render(request, 'main/form.html')
    else:
        return redirect('/')



def table(request):
    user = request.user
    entry = Entry.objects.filter(created_by=user)
    for i in entry:
        print(i.authors)
        
    context = {'entry':entry}

    return render(request, 'main/table.html', context)

def delete(request,id):
   
    obj = get_object_or_404(Entry, id = id)
    obj.delete()
    return redirect("/home/table/")


def update_table(request, id):
    
    objects = get_object_or_404(Entry,id=id) 
    

    if request.method=="POST":
        author_name = request.POST["author_name"]
        blog_name = request.POST["blog_name"]
        tagline = request.POST["tagline"]
        email = request.POST["email"]
        headline = request.POST["headline"]
        body_text = request.POST["body_text"]
        mod_date = request.POST["mod_date"]
        number_of_comments = request.POST["number_of_comments"]
        pub_date = request.POST["pub_date"]
        number_of_pingbacks = request.POST["number_of_pingbacks"]
        objects.author_name = author_name
        objects.blog_name = blog_name
        objects.tagline = tagline
        objects.email = email
        objects.headline = headline
        objects.body_text = body_text
        objects.mod_date = mod_date
        objects.number_of_comments = number_of_comments
        objects.pub_date = pub_date
        objects.number_of_pingbacks = number_of_pingbacks
        objects.save()
        return HttpResponseRedirect("/home/table")
    
    data = {}
    data["dataset"] = objects
    
    return render(request, "main/update.html", data)