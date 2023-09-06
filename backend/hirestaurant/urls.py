from django.urls import path 
from . import views 
from .models import * 

urlpatterns = [
    path('',views.index,name="index"),
    
    path('restraunt_list/',views.RestaurantList.as_view(),name='restraunt_list'),
    
]
