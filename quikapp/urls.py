from django.urls import path 
from quikapp import views
urlpatterns = [
   
    path('', views.landingpage, name= 'land'),
    path('login/', views.LoginView, name='login'),
    path('profile/', views.profile, name= 'profile'),
    path('home/', views.homepage, name='home'),
    path('signup/', views.SignUpView, name='signup')
]