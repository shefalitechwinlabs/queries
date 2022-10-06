from django.shortcuts import render
from django.http import HttpResponse
from crud_app.models import Practice
from django.shortcuts import get_object_or_404,render,HttpResponseRedirect
from django.template import loader

def home(request):
    if 'username' in request.session:
        return render(request, 'home.html')
    else:
        return HttpResponseRedirect('/')


def form(request):
    if 'username' in request.session:
        if request.method=="POST":
            name = request.POST["name"]
            phone = request.POST["phone"]
            address = request.POST["address"]
            zipcode = request.POST["zipcode"]
            p = Practice(fullname=name,phonenumber=phone,address=address,zipcode=zipcode)
            p.save()
        return render(request, 'form.html')
    else:
        return HttpResponseRedirect('/')



def table(request):
    if "username" in request.session:
        context ={}
        context["dataset"] = Practice.objects.all()

        return render(request, 'table.html', context)
    else:
        return HttpResponseRedirect('/')




def delete(request,id):
    
    if "username" in request.session:
        obj = get_object_or_404(Practice, id = id)
        
        if request.method =="POST":
            # delete object
            obj.delete()
            return HttpResponseRedirect("/table/")
        
        return render(request, "delete.html")
    else:
        return HttpResponseRedirect('/')



def update_table(request, id):
    
    if "username" in request.session:
        objects = get_object_or_404(Practice,id=id) 

        if request.method=="POST":
            name = request.POST["name"]
            phone = request.POST["phone"]
            address = request.POST["address"]
            zipcode = request.POST["zipcode"]
            objects.fullname = name
            objects.phonenumber = phone
            objects.address = address
            objects.zipcode = zipcode
            objects.save()
            return HttpResponseRedirect("/table/")
        
        data = {}
        data["dataset"] = Practice.objects.all().filter(id=id)
        
        return render(request, "update.html", data)
    else:
        return HttpResponseRedirect('/')