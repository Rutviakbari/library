from django import views
from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User

def index(request):
    if request.method == "POST":
     Email=request.POST['email']
     password=request.POST['password']

     myuser=User.objects.create_user(Email,password)
     myuser.save()

    return render(request,'index.html')

    
def about(request):
    return render(request,'about.html')

    
def books(request):
    return render(request,'books.html')

    


