from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    daddress = models.CharField(max_length=250)
    phone= models.CharField(max_length=150)
    user = models.OneToOneField(to=User,on_delete=models.CASCADE,related_name='profile')
    role=models.CharField(max_length=10,default='customer')

    def is_customer(self):
        return self.role=='customer'
