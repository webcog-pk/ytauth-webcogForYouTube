from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomProfiles(AbstractUser):
    phone = models.CharField(max_length=15, null=True,blank=True)
    cnic = models.CharField(max_length=15, null=True,blank=True)