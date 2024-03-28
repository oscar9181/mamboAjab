from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from.forms import RegisterUserForm



# Create your views here.
def register(request):
   form=RegisterUserForm()
   if request.method == 'POST':
         form=RegisterUserForm(request.POST)
         if form.is_valid():
             form.save()    
             username = form.cleaned_data.get('username')
             messages.success(request,f'Account has been created for{username}' )    
             return redirect('login')    
         else:       
             form=RegisterUserForm()       
             
   return render(request, 'account/register.html',{'form':form})

def login(request):
    if request.method == 'POST':
       username = request.POST.get("username")
       print('username:', username)

       password = request.POST.get("password")
       print(password)
       user = authenticate(request, username=username, password=password)
       if user is not None:
            print(user)
            auth_login(request,user)
            messages.success(request,("Login succesful"))
            return redirect('home')
       else:
           messages.info(request,'Username or Password is incorrect')
    return render(request, 'account/login.html')

 