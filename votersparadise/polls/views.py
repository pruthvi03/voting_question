from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import HttpResponse,redirect
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    return render(request,'index.html')

def passreset(request):
    return render(request,'passreset.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['susername']
        firstname = request.POST['sfirstname']
        lastname =request.POST['slastname']
        email =request.POST['semail']
        password =request.POST['spassword']

        # add parameters checking prog   

        # make user 
        myuser = User.objects.create_user(username ,email ,password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request , "account is created!")
        return HttpResponse("thank you!")
    else:
        return HttpResponse("Error 404")
        
        

        
        