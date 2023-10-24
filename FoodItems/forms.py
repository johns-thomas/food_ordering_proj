
from django import forms

from .models import FoodItem

class AddFoodItemForm(forms.ModelForm):
    
    class Meta:
        model = FoodItem
        fields = ('name', 'description','price','discount','img')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['discount'].widget.attrs.update({'class': 'form-control'})
        self.fields['img'].widget.attrs.update({'class': 'form-control'})