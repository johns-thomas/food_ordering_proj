from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import FoodItem
from .forms import AddFoodItemForm
from users.models import Profile
from users.forms import ProfileCreationForm

@login_required
def home_page(request):
    items = FoodItem.objects.order_by('ratings')
    context = {'items': items}
    return render(request, 'fooditems/index.html', context)

@login_required
def add_or_edit_food_item(request,item_id=None):
    if item_id:
        instance = get_object_or_404(FoodItem, id=item_id)
    else:
        instance = None
    if request.method == "POST":
        form=AddFoodItemForm(request.POST, request.FILES,instance=instance)
        print(form)
        if form.is_valid:
            form.save()
            return redirect('fooditems:home')
    elif request.method == "GET": 
        form = AddFoodItemForm(instance=instance)
        return render(request, 'fooditems/addfoodItem.html', {'form': form})   

@login_required    
def view_item(request,item_id):
    try:
        item = FoodItem.objects.get(pk=item_id)
    except FoodItem.DoesNotExist:
        raise Http404("Item  not found")
    return render(request, 'fooditems/viewitem.html', {'item': item,'is_buy':True})


    
