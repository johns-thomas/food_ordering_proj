from django.urls import path
from . import views

app_name = 'orders'


urlpatterns = [
path('/buyitem/<int:item_id>/', views.create_order, name='place_order'),
]
