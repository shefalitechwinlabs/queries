# CRUD_operation
## Used code
  -HTML
  -Bootstrap - form class
  -Django Database to save data of form
  
## Code
  In url of page when we add 'admin' in browser then it redirects to portal admin page where we need to sign in with username and password.
  In terminal we need to create username and passowd by using cmd 'django-admin createsuperuser' then it will ask username and password.
  
  ## models.py
  In models.py we will create the forms data 
  
  # code
  from django.db import models
  class crud(models.Model):
    fullname = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    zipcode = models.TextField(max_length=10)
  
  This is the table we have created. By using the cmd 'python manage.py makemigrations' and then 'python manage.py migrate' we can make an instance 
  of the model with this command.
  
  ## CRUD
  ### Create 
  create data in table in database.  
  ### code<--
  Post means to save or create or put something in table post is method to post some data
  
  def form(request):

    if request.method=="POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        zipcode = request.POST["zipcode"]
        p = crud(fullname=name,phonenumber=phone,address=address,zipcode=zipcode)
        p.save()

    return render(request, 'form.html')
  ### --
  
  ### Retrieve 
  get the data from table. We use GET method to retrieve the data
  ### code<--
  def table(request):

    context ={}
    context["dataset"] = crud.objects.all()

    return render(request, 'table.html', context)
  ### --
  
  ### Update 
  changes in existing data in table
  ### code<--
  def update_table(request, id):
    
    objects = get_object_or_404(crud,id=id) 

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
    data["dataset"] = crud.objects.all().filter(id=id)
    
    return render(request, "update.html", data)
  ### -->
  
  ### Delete 
  delete the existing data in table
  ### code<--
  def delete(request,id):
   
    obj = get_object_or_404(crud, id = id)
    
    if request.method =="POST":
        # delete object
        obj.delete()
        return HttpResponseRedirect("/table/")
    
    return render(request, "delete.html")
  ### -->
