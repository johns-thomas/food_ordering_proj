from django.shortcuts import render,redirect
from django.http import Http404

from .models import FoodItem
from .forms import AddFoodItemForm
from users.models import Profile
from users.forms import ProfileCreationForm

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
    
def view_item(request,item_id):
    try:
        item = FoodItem.objects.get(pk=item_id)
    except FoodItem.DoesNotExist:
        raise Http404("Item  not found")
    return render(request, 'fooditems/viewitem.html', {'item': item,'is_buy':False})

def buy_item(request,item_id):
    try:
        item = FoodItem.objects.get(pk=item_id)
        profile=Profile.objects.filter(user=request.user)
        form = ProfileCreationForm(instance=profile)
        if(item.is_available()):
            context={'item': item,'is_buy':True, 'form':form}
        else:
            raise FoodItem.DoesNotExist
    except FoodItem.DoesNotExist:
        raise Http404("Item  not found")
    return render(request, 'fooditems/viewitem.html', context)
    
