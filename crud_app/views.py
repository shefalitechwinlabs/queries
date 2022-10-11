from django.shortcuts import render
from django.http import HttpResponse
from crud_app.models import Entry,Blog,Author
from django.shortcuts import get_object_or_404,render,HttpResponseRedirect
from django.template import loader

def home(request):
    return render(request, 'home.html')


def form(request):

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
        ratings = request.POST["ratings"]
        B = Blog(name=blog_name,tagline=tagline)
        B.save()
        A = Author(name=author_name,email=email)
        A.save()
        E = Entry(blog=B,headline=headline,body_text=body_text,mod_date=mod_date,number_of_comments=number_of_comments,pub_date=pub_date,number_of_pingbacks=number_of_pingbacks)
        E.save()
        E.authors.add(A)
        E.save()
    return render(request, 'form.html')



def table(request):
    context ={}
    context["Entry"] = Entry.objects.all()
    context["Blog"] = Blog.objects.all()
    context["Author"] = Author.objects.all()
    
    return render(request, 'table.html', context)




def delete(request,id):
   
    obj = get_object_or_404(Entry, id = id)
    
    if request.method =="POST":
        # delete object
        obj.delete()
        return HttpResponseRedirect("/table/")
    
    return render(request, "delete.html")



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
        return HttpResponseRedirect("/table/")
    
    data = {}
    data["dataset"] = Entry.objects.all().filter(id=id)
    
    return render(request, "update.html", data)