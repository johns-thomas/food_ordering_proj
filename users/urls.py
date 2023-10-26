from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'users'


urlpatterns = [
path('signup/', views.sign_up, name='sign_up'),
path('login_home/', views.on_login, name='on_login'),
path('staff_signup/', views.staff_signup, name='staff_signup'),
]
