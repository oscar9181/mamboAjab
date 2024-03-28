from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('properties',views.properties,name='properties'),
    path('add-property',views.add_property, name='add-property'),
    # path('base', views.base, name='base'),
    
   

]