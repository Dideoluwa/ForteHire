from django import forms
from . models import addJob

class addJobForm(forms.ModelForm):
    class Meta:
        model=addJob
        fields=['title', 'description', 'image', 'active']
        