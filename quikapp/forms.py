from django import forms
from . models import UserProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['user_bio', 'user_image','skills', 'resume_upload'
        ,'user_location','portfolio_link']