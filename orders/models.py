from django.db import models
from FoodItems.models import FoodItem
from django.contrib.auth.models import User

class Orders(models.Model):
    
    item=models.ForeignKey(FoodItem, on_delete=models.PROTECT,related_name='item')
    user = models.ForeignKey(User,on_delete=models.PROTECT,related_name='user')
    order_placed_at=models.DateTimeField()
    status=models.CharField(max_length=20,default='PENDING')
    selling_price=models.FloatField()

    
