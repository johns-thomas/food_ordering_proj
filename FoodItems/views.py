from django.shortcuts import render,redirect
from .models import FoodItem
from .forms import AddFoodItemForm

def home_page(request):
    items = FoodItem.objects.order_by('ratings')[:15]
    context = {'items': items}
    return render(request, 'fooditems/index.html', context)

def add_food_item(request):
    if request.method == "POST":
        form=AddFoodItemForm(request.POST, request.FILES)
        print(form)
        if form.is_valid:
            form.save()
            return redirect('fooditems:home')
    elif request.method == "GET": 
        form = AddFoodItemForm()
        return render(request, 'fooditems/addfoodItem.html', {'form': form})   
    
