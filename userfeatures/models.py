from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class User(AbstractUser):
    mobile_no = models.CharField(max_length=120,null=True,blank=True)
    dept_name = models.CharField(max_length=120,null=True,blank=True)
    age = models.CharField(max_length=120,null=True,blank=True)
    address = models.CharField(max_length=250,null=True,blank=True)
    add_user = models.BooleanField(default=False)
    del_user = models.BooleanField(default=False)
    view_user = models.BooleanField(default=False)
    edit_user = models.BooleanField(default=False)
    user_stats = models.BooleanField(default=False)

    # def __str__(self):
    #     return str(self.id)