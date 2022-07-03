import email
from django.shortcuts import redirect, render
from django.contrib import messages

from django.contrib.auth  import get_user_model, authenticate, login
from django.contrib.auth.decorators import login_required
from quikapp.forms import ProfileForm
from quikapp.models import UserProfile

User = get_user_model()
# Create your views here.
def LoginView(request):
    if request.method=="POST":    
        email=request.POST['email']
        password=request.POST['password']

        user=authenticate(username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            #messages.error(request,"Please Sign up, you have no account")
            return redirect('signup')
    else:
        return render(request, 'login.html')
 
def SignUpView(request):
    if request.method == "POST":
        firstname=request.POST.get('username')
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        #user_location=request.POST['countries'] first_name=user_location
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('.')
            else:
                user=User.objects.create_user(username=email, last_name=lastname, first_name=firstname, password=password,)
                user.save()
                login(request, user)
        

                user_model=User.objects.get(username=email)
                new_user= UserProfile.objects.create(user=user_model, id_user=user_model.id)
                new_user.save()
                return redirect('profile')
        else:
            messages.info(request, "Password don't match")
            return redirect('.')
    else:
        return render(request, 'signup.html')


def homepage(request):
    user_object=User.objects.get(username=request.user.username)
    user_profile=UserProfile.objects.get(user=user_object) 
    return render(request, 'homepage.html',{'user_profile':user_profile})

def landingpage(request):
    return render(request, 'landing.html')

def profile(request):
    form=ProfileForm()
    if request.method=='POST':
        form=ProfileForm(request.POST)
        if form.is_valid():
            profile_form=form.save()
            profile_form.user=request.user
            profile_form.save()
            redirect('.')

    return render(request, 'profile.html',{'form':form})

