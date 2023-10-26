from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'users'


urlpatterns = [
path('signup/', views.sign_up, name='sign_up'),
path('login_home/', views.on_login, name='on_login'),
 path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='log_in'),
path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='log_out'),
]
