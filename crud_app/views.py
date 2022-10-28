from django.shortcuts import render, redirect
from django.http import HttpResponse
#from crud_app.models import *
from authentication.models import Profile, ExtendUser
from django.shortcuts import get_object_or_404,render,HttpResponseRedirect
from django.template import loader
from .forms import *
from .validators import validate_google_mail


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def home(request):
    if 'username' in request.session:
        return render(request, 'main/home.html')
    else:
        return redirect('/')

def profile(request):
    if 'username' in request.session:
        context = {}
        profile = Profile.objects.get(name=request.user)
        fullname = profile.name.first_name +' '+ profile.name.last_name
        context = {'dataset': profile, 'fullname': fullname}
        return render(request, 'main/profile.html', context)

# def authorform(request):
#     if 'username' in request.session:
#         context = {}
#         context = {'author': AuthorForm}
#         if request.method == 'POST':
#             author_form = AuthorForm(request.POST)
#             if author_form.is_valid():
#                 author = author_form.save(commit=False)
#                 author.created_by = request.user
#                 author.save()
#                 return render(request, 'form/authorform.html', context)
#             else:
#                 context['author'] = author_form
#             return render(request, 'form/authorform.html', context)
#         return render(request, 'form/authorform.html', context)
#     else:
#         return redirect('/')

# def entryform(request):
#     if 'username' in request.session:
#         context = {}
#         context = {'entry': EntryForm}
#         if request.method == 'POST':
#             entry_form = EntryForm(request.POST)
#             if entry_form.is_valid():
#                 entry = entry_form.save(commit=False)
#                 entry.save()
#                 return render(request, 'form/entryform.html', context)
#             else:
#                 context['entry'] = entry_form
#             return render(request, 'form/entryform.html', context)
#         return render(request, 'form/entryform.html', context)
#     else:
#         return redirect('/')

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

# def authorform(request):
#     if 'username' in request.session:
#         if request.method=="POST":
#             #author_name = request.POST.get("author_name")
#             blog_name = request.POST.get("blog_name",'test')
#             tagline = request.POST.get("tagline", 'test')
#             theme = request.POST.get("theme", 'test')
#             email = request.POST.get("email", 'test@gmail.com')
#             headline = request.POST.get("headline", 'test')
#             body_text = request.POST.get("body_text",'test')
#             mod_date = request.POST.get("mod_date",'2022-10-27')
#             number_of_comments = request.POST.get("number_of_comments",4)
#             pub_date = request.POST.get("pub_date", '2022-10-05')
#             number_of_pingbacks = request.POST.get("number_of_pingbacks", 2)
#             rating = request.POST.get("rating", 5)
#             created_by = request.user
            
#             A = Author(email=email,created_by=created_by)
#             A.save()
#             TB = ThemeBlog(blog_name=blog_name,tagline=tagline,theme=theme,created_by=A)
#             TB.save()
#             E = Entry(blog=TB,headline=headline,body_text=body_text,mod_date=mod_date,rating=rating,created_by=created_by,number_of_comments=number_of_comments,pub_date=pub_date,number_of_pingbacks=number_of_pingbacks)
#             E.save()
#             E.authors.add(A)
#             E.save()
#         context = {'entry': EntryForm, 'author': AuthorForm}
#         return render(request, 'main/form.html', context)

#     else:
#         return redirect('/')

def article(request):
    user =  request.user
    article =  Blog.objects.get(created_by=user)
    context = {'article':article}
    return render(request, 'main/article.html', context)

def table(request):
    user = request.user
    blog = Blog.objects.get(created_by=user)
    entry = Entry.objects.get(blog=blog)  
    print(entry)
    context = {'entry':entry,'data':[]}

    return render(request, 'main/table.html', context)

def delete(request,id):
   
    obj = get_object_or_404(Blog, id = id)
    obj.delete()
    return redirect("/home/table/")


def update_table(request, id):
    
    objects = get_object_or_404(Blog,id=id) 
    

    if request.method=="POST":
        #author_name = request.POST["author_name"]
        blog_name = request.POST["blog_name"]
        tagline = request.POST["tagline"]
        email = request.POST["email"]
        headline = request.POST["headline"]
        body_text = request.POST["body_text"]
        mod_date = request.POST["mod_date"]
        number_of_comments = request.POST["number_of_comments"]
        pub_date = request.POST["pub_date"]
        number_of_pingbacks = request.POST["number_of_pingbacks"]
        #objects.author_name = author_name
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