from django.urls import path
from . import views

app_name = 'users'


urlpatterns = [
path('', views.sign_up, name='sign_up'),
path('login_home/', views.on_login, name='on_login'),
]
