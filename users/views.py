from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import *
# Create your views here.
app_name = "users"



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')

        return render(request, 'users/register.html', {'form': form})

    else:
        form = UserCreationForm()
        return render(request, 'users/register.html', {'form': form})



def login_view(request):
    if not request.user.is_authenticated:
        user = authenticate(request,username=request.POST.get('username'),password=request.POST.get('password'))
        if user is not None:
            login(request,user)
            return redirect("users:index",user.id)
        else:
            forms = LoginForm(request.POST)
            return render(request,'users/login.html', {'forms' : forms})
        
    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('users:login')



def profile(request,user_id):
    if request.user.is_authenticated:
        user  = User.objects.get(id=user_id)
        if user is not None:
            profile = Profile.objects.get(user=user).pk
