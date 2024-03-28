from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Rentals
from .forms import RentalsForm

# Create your views here.
def home(request):
   
    return render(request, 'Home/home.html',{})

def base(request):
    
    return render(request, 'Home/base.html',{})

def properties(request):
    vacant = Rentals.objects.all()
    return render(request,'Home/properties.html',{"all":vacant})
 
def add_property(request):

    if request.method =='POST':
      form = RentalsForm(request.POST)
      if form.is_valid():
        form.save()
        # return HttpResponseRedirect("Home/add-property? submitted=True")
    else:
        form = RentalsForm     
    return render(request, 'Home/add-property.html',{"form":form})


def add_property(request):
    if request.method == 'POST':
        form = RentalsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Home/add-property?submitted=True')
    else:
        form = RentalsForm()

    return render(request, 'Home/add-property.html', {'form': form})

def search(request):
    if request.method == 'GET':
        search=request.GET.get('search')
        if search:
          hoods=home.objects.filter(name__icontains=search)
        return render(request, 'Home/search.html',{'hoods':hoods})
        