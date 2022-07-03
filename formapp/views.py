from django.shortcuts import redirect, render
from .forms import addJobForm
# Create your views here.

def addJobView(request):
    jobform=addJobForm()
    if request.method=="POST":
        jobform=addJobForm(request.POST)
        if jobform.is_valid():
            job = jobform.save(commit=False)
            job.owner = request.user
            job.save()
            redirect('home')
    return render(request, 'editjob.html',{'jobform':jobform})



    