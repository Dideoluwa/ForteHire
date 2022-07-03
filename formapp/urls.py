from django.urls import path
from formapp import views

urlpatterns=[
    path('edit-job/', views.addJobView, name='edit-job')
]