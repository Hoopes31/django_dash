from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import *

# Set up login permissions by default
# Set up Decrypt
# Check encryption
# Check login 
# Fix SignUp CSS

# Static Views
def login_page(request):
    form = LoginForm()
    return render(request, 'login/login.html', {'form':form})

def welcome(request, name):
    return render(request, 'login/welcome.html', {'name':name})

def sign_up(request):
    form = UserForm()
    return render(request, 'login/sign_up.html', {'form':form})

def logout(request):
    return redirect('login:login')

# Action Views
def create_user(request):
    # Get form data
    form = UserForm(request.POST)

    # Clean form, Create User, Hash Password, Save Data
    if form.is_valid():
        form = form.cleaned_data
        user = User.objects.create(username=form['username'].lower(), first_name=form['first_name'].lower(), last_name=form['last_name'].lower(), 
        email=form['email'].lower())
        user.set_password(form['password'])
        if user.id == 1:
            user.is_staff = True
        user.save()
        return redirect('login:welcome', name = form['first_name'])
    
    else:
        return render(request, 'login/sign_up.html', {'form':form})

def auth(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = request.POST['username'].lower()
        password = request.POST['password'].lower()
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login:welcome', name = username)
    
    messages.error(request, 'Login Invalid')
    
    return redirect('login:login')

