from django.shortcuts import render
from django.http import HttpResponse
from .models import Rentals

# Create your views here.
def home(request):
   
    return render(request, 'Home/home.html')

def base(request):
    
    return render(request, 'Home/base.html',{})

def properties(request):
    vacant = Rentals.objects.all()
    return render(request,'Home/properties.html',{"all":vacant})

