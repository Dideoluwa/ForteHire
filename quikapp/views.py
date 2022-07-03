from django.shortcuts import redirect, render
from django.contrib import messages

from django.contrib.auth  import get_user_model, authenticate, login
from django.contrib.auth.decorators import login_required
from quikapp.models import UserProfile

User = get_user_model()
# Create your views here.
def LoginView(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']

        user=authenticate(email=email, password=password)
        
        if user is not None:
            login(request, user)
            redirect('home/')
        else:
            messages.error(request,"Please Sign up, you have no account")
            redirect('login')
    return render(request, 'login.html')

def SignUpView(request):

    if request.method == "POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        user_location=request.POST['countries']
        
        if password != password2:
            messages.info(request, "Password don't match")
            redirect('.')
        else:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                redirect('.')
            else:
                user=User.objects.create_user(username=firstname, last_name=lastname, email=email, password=password,first_name=user_location)
                user.save()
                login(request, user)

                user_model=User.objects.get(username=firstname)
                new_user= UserProfile.objects.create(user=user_model, id_user=user_model.id)
                new_user.save()
                redirect('home/')
    else:
        return render(request, 'signup.html')

@login_required(login_url='login')
def homepage(request):
    
    return render(request, 'homepage.html')