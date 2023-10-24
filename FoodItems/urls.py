from django.urls import path
from . import views






app_name = 'fooditems'


urlpatterns=[
    path('', views.home_page, name='home'), # type: ignore
    path('addfooditem/', views.add_food_item, name='addfooditem'), 
    path('<int:item_id>/', views.view_item, name='viewitem'),
    path('buyitem/<int:item_id>/', views.buy_item, name='buyitem')# type: ignore
]
