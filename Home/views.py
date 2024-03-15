from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'Home/home.html')

def home2(request):
    return  HttpResponse('<h1> home page about </>')

