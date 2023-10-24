from django.db import models
from FoodItems.models import FoodItem
from users.models import User

class Orders(models.Model):
    daddress = models.CharField(max_length=150)
    eircode= models.CharField(max_length=150)
    item_id=models.ForeignKey(FoodItem)
    user_id=models.ForeignKey(User)
    order_placed_at=models.DateTimeField()

    
