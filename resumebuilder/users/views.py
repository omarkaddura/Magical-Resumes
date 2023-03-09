from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.



def landing_page(request):
    return render(request, 'landing.html')


def register (request): #This handles the user registration/ login

    if request.method == "POST":

        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your Account has beem created!")
        return redirect('')



    return render(request, 'register.html')