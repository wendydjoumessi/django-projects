from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import member

# Create your views here.

def index(request):
   members = member.objects.all()
   return render(request, 'index.html', {'members' : members } )


def counter(request):
    posts = [1, 2, 3, 4, 5, 'tim', 'tom', 'john']
    return render(request, 'counter.html', {'posts' : posts})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password Not thesame')
            return redirect('register')
    else: 
        return render(request, 'register.html')   
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'credentials Invalid')
            return redirect('login')
        
    else:    
        return render(request, 'login.html')

        
    
def logout(request):
    auth.logout(request)
    return redirect('/')



def post(request, pk):
    return render(request, 'post.html', {'pk' : pk})

        
                


    
    