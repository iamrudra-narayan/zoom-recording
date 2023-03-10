from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login 
from django.contrib.auth import authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import RecordedCall

# Create your views here.
def register(request):
    if request.user.is_authenticated:
      return redirect("/")
    if request.method == "POST":
        try:
            email = request.POST['email']
            User.objects.get(username = request.POST['email'])
            messages.error(request, f"The Email {email} is already taken. Try a unique Email.")
            return redirect ('/myaccount/register/')
        except User.DoesNotExist:
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User(username=email, first_name=fname, last_name=lname)
            user.set_password(password)
            user.save()
            messages.success(request, f"Registration Successful. Welcome {fname} {lname}. Please Login to Proceed.")
            return redirect('/myaccount/login/') 
    else:
        return render(request,'register.html')
       

def login(request):
    if request.user.is_authenticated:
      return redirect("/")
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request,user)
            messages.success(request, f"Welcome back {user.username}.")
            return redirect('/myaccount/profile/')
        else:
            messages.error(request, f"Invalid Credentials. Login again.")
            return redirect('/myaccount/login/')
    else:               
        return render(request, "login.html")
    
def logout_user(request):
	logout(request)
	return redirect("/myaccount/login/")

@login_required(login_url='login')
def profile(request):
    user_id = request.user.id
    user=User.objects.filter(id=user_id).first()
    return render(request, "profile.html",{'user':user,})

@login_required(login_url='login')
def recordings(request):
    user_id = request.user.id
    data = RecordedCall.objects.filter(user = user_id)
    return render(request, "recordings.html",{'data':data,})     
