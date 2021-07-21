from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate as django_auth
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from blog.models import Author



@login_required()
def logout(request):
    if request.method == "POST":
        django_logout(request)
        return redirect("blog:home")    


def signup(request):

    if request.method == "GET":
        return render(request, 'users/signup.html')
    else: 
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], '', request.POST['password1'])
                user.save()

                author = Author(name=user.username)
                
                author.save()
                django_login(request, user)

                return redirect('blog:home')

            except IntegrityError:
                return render(request, 'users/signup.html', {'error': 'User is already taken, choose another one.'})

        else: 
            
            return render(request, 'users/signup.html', {'error': 'Passwords did not match. Try again!'})
    

def login(request):
    
    if request.method == "GET":
        return render(request, 'users/login.html')
    else:
        
        user = django_auth(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            django_login(request, user)
            return redirect('blog:home')
        else:
           return render(request, 'users/login.html',
                    {'error': 'User or Password incorrect. Try again!'})
        

