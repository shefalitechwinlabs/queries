from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
#from .signals import mysignal
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = SignupForm()
    #mysignal.send(sender=SignupForm)
    context = {'form': form}
    return render(request, 'authentication/signup.html', context)

def login(request):
    if "username" in request.session:
        return redirect('home/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            request.session['username'] = username
            return redirect('home')
        else:
            context = {'error':'Username or password is incorrect!'}
            return render (request,'authentication/login.html', context)
    else:
        return render(request,'authentication/login.html')
  
  

def logout(request):
    auth.logout(request)
    username = request.session.get('username')
    del username
    return render (request, 'authentication/logout.html')
