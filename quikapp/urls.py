from django.urls import path 
from quikapp import views
urlpatterns = [
   
    path('', views.LoginView , name= 'login'),
    path('home/', views.homepage, name='homepage'),
    path('signup', views.SignUpView, name='signup')
]