from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import Http404
from django.contrib.auth.decorators import login_required

from .models import Orders
from FoodItems.models import FoodItem

from django.contrib.auth.decorators import user_passes_test

def is_customer(user):
    print(user)
    return user.profile.role=='customer'

def is_staff(user):
    print(user)
    return user.profile.role=='staff'

@user_passes_test(is_customer)
@login_required
def create_order(request):
    if request.method == "POST":
        print(request)
        item_id= request.POST.get('item_id')
        item = FoodItem.objects.get(pk=item_id)
        order=Orders()
        order.user=request.user
        order.item=item
        order.order_placed_at=timezone.now()
        order.selling_price=item.get_selling_price()
        order.save()
           
    return redirect('orders:view_orders')

@login_required
def view_orders(request):
    filter=request.GET.get('status')
    user=request.user
    if( user.profile.is_customer() ):
        if filter is not None:
            list=Orders.objects.filter(status=filter,user=user ).order_by('order_placed_at').select_related()
        else:
            list=Orders.objects.filter(user=user ).order_by('order_placed_at').select_related()
    else:
        if filter is not None:
            list=Orders.objects.filter(status=filter).order_by('order_placed_at').select_related()
        else:
            list =Orders.objects.all().order_by('order_placed_at').select_related()
    print(list)
    return render(request,'orders/vieworders.html',{'orders':list})

@user_passes_test(is_staff)
@login_required
def change_order_status(request):
    try:
        order_id=request.POST.get('order_id')
        order = Orders.objects.get(pk=order_id)
        print('###########')
        print(order)
        status= request.POST.get('status')
        print(status)
        order.status=status
        order.save()
    except Orders.DoesNotExist:
        raise Http404("Item  not found")
    return  redirect('orders:view_orders')


        
    
    
            