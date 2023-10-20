from django.urls import path
from . import views
from django.conf import settings

from django.conf.urls.static import static



app_name = 'fooditems'


urlpatterns=[
    path('', views.home_page, name='home'), # type: ignore
    path('addfooditem/', views.add_food_item, name='addfooditem'), # type: ignore
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)