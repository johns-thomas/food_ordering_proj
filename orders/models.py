from django.db import models
from FoodItems.models import FoodItem
from django.contrib.auth.models import User

class Orders(models.Model):
    
    item=models.ForeignKey(FoodItem, on_delete=models.PROTECT)
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    order_placed_at=models.DateTimeField()
    status=models.CharField(max_length=20,default='PENDING')

    
