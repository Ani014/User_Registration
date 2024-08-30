from django.shortcuts import render
from .forms import CreateUserForm 
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):  
    return render(request,"home.html")
def register(request):
    if request.method=='POST':
        name=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        User = get_user_model()
        
        if User.objects.filter(username=name).exists():
            messages.error(request, 'Username already taken')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already taken')
        elif password1 != password2:
            messages.warning(request, 'Passwords do not match!')
        else:
            user = User.objects.create_user(username=name, email=email, password=password1)
            user.is_staff=True
            user.is_superuser=True
            user.save()  
            messages.success(request, 'Your account has been created. You are now able to log in')
            return redirect('Login')
        
        return redirect('Register')

    else:   
        form = CreateUserForm()
        return render(request, "register.html", {'form1': form})
@login_required
def profile(request):
    return render(request,"profile.html")
