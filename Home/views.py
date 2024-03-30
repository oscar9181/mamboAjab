from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponseRedirect
from .models import Rentals
from .forms import RentalsForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    

    return render(request, 'Home/home.html',{})

def base(request):
    
    return render(request, 'Home/base.html',{})

@login_required(login_url='login')
def properties(request):
    vacant = Rentals.objects.all()
    return render(request,'Home/properties.html',{"all":vacant})
 
def add_property(request):
    form = RentalsForm
    if request.method =='POST':
      form = RentalsForm(request.POST, request.FILES)
      print(form.data)
      print('for is valid', form.is_valid)
      if form.is_valid():
        form.save()
        return redirect("properties")
      else:
         print('not saved')
         return redirect('home')    


    # else:
    #     form = RentalsForm
    return render(request, 'Home/add-property.html', {'form': form})




def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        print(search)
        if search:
         rentals = Rentals.objects.filter( location__icontains=search )
    return render(request, 'Home/search.html',{'rentals': rentals})

# propert details page
def property_detail_view(request, property_id):
    # Retrieve the property object based on the property_id
    property_obj = get_object_or_404(Rentals, id=property_id)
    print('loggged ins', request.user)

    
    # Pass the property object to the template
    return render(request, 'Home/property_details.html', {'property': property_obj})
        