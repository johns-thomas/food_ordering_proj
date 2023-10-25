from django.shortcuts import render, redirect
from django.utils import timezone
from users.forms import ProfileCreationForm
from .models import Orders
from FoodItems.models import FoodItem

def create_order(request):
    if request.method == "POST":
        form=ProfileCreationForm(request.POST)
       # print(form)
        item_id= request.POST.get('item_id')
        item = FoodItem.objects.get(pk=item_id)
        if form.is_valid:
            order=Orders()
            order.user=request.user
            order.item=item
            order.order_placed_at=timezone.now()
            order.save()
            form.save()# updating the address and phone number

    return redirect('orders:view_orders')

def view_orders(request):
    filter=request.GET.get('status')
    user=request.user
    if( user.profile.is_customer() ):
        if filter is not None:
            list=Orders.objects.filter(status=filter,user=user ).order_by('order_placed_at').values()
        else:
            list=Orders.objects.filter(user=user ).order_by('order_placed_at').values()
    else:
        if filter is not None:
            list=Orders.objects.filter(status=filter).order_by('order_placed_at').values()
        else:
            list =Orders.objects.all().order_by('order_placed_at').values()

    return render(request,'orders/vieworders.html',{'orders':list})
        
    
    
            