from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# from .models import CustomUser  # Import the CustomUser model


# Create your views here.

def index(request):
    return render(request, 'includes/index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')



def indexx(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('dash')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('indexx')
    else:
        return render(request, 'indexx.html')

def program(request):
    return render(request, 'program.html')

def dash(request):
    return render(request, 'dash.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # date_of_birth = request.POST.get('date_of_birth')  
        # place_of_birth = request.POST.get('place_of_birth') 
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                
                
                messages.success(request, "Registration successful! You can now log in.")
                return redirect('indexx')
        else:
            messages.info(request, 'Password do not match')
            return redirect('register')
    
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def reset(request):
    return render(request, 'reset.html')