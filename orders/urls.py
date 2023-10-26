from django.urls import path
from . import views

app_name = 'orders'


urlpatterns = [
path('buyitem/', views.create_order, name='place_order'),
path('view_orders/', views.view_orders, name='view_orders'),
path('change_status/', views.change_order_status, name='change_status')
]
