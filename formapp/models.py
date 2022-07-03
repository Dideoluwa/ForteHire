from distutils.command.upload import upload
from django.db import models
from quikapp.models import User
# Create your models here.
class addJob(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=290)
    description =models.TextField()
    image= models.ImageField(upload_to='jobimages', blank=True)
    active=models.BooleanField(default=True)

    def __str__(self):
       return self.owner.email
