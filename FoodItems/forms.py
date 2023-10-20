from django import forms
from .models import FoodItem

class AddFoodItemForm(forms.ModelForm):
    
    class Meta:
        model = FoodItem
        fields = ('name', 'description','price','discount','img')