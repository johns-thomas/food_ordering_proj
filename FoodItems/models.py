from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    ratings = models.FloatField(default=0)
    description = models.CharField(max_length=400)
    discount=models.FloatField()
    img= models.ImageField(upload_to='images/')
    

    def __str__(self):
        return self.name + " - " + self.description
    
    def is_available(self):
        return self.flag&1==1
    def get_selling_price(self):
        return self.price-self.discount
    
