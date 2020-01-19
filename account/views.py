from django.shortcuts import render , redirect
from django.contrib.auth.models import User,auth

# Create your views here.

def login(request):
    if request.method == "POST":
       username = request.POST['username']
       password = request.POST['password']

       user = auth.authenticate(username=username,password=password)
       auth.login(request, user)
       return redirect("/") 
    else:
         return render(request,'login.html')

def register(request):
    if request.method == "POST":
       username = request.POST['username'] 
       email = request.POST['email']
       password = request.POST['password']
       password_confirm = request.POST['password_confirm']

       user = User.objects.create_user(username=username, password=password, email=email)
       user.save();
       print('user created')
       return redirect('register')

    else:
         return render(request,'register.html')
