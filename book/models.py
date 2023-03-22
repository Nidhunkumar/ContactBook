from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Contact_details(models.Model):
    name=models.CharField(max_length=20,null=False,blank=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)
    number=models.IntegerField(null=False,blank=False)
