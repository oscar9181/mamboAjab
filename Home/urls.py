from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('properties',views.properties,name='properties'),
    path('add-property',views.add_property, name='add-property'),
    path('search',views.search, name='search'),
    path('property/<int:property_id>/', views.property_detail_view, name='property_detail'),
    # path('base', views.base, name='base'),
    
   

]