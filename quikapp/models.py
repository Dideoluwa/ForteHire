from django.db import models
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField




User=get_user_model()

class UserProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.EmailField()
    id_user=models.IntegerField()
    user_image=models.ImageField(upload_to='user_images')
    user_bio=models.TextField(blank=True)
    user_location= CountryField(blank_label='Select Country')
    years_of_experience=models.CharField(max_length=12)
    resume_upload=models.FileField(upload_to='users_resume')
    
    def __str__(self):
        return self.user.email