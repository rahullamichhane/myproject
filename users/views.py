from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages
from .forms import UserRegistrationForm



# Create your views here.
def home(request):
    return render(request,'users/home.html')

def details(request):
    return render(request,'users/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, f'Your account is created.')
            return redirect('login')

    else:
        form = UserRegistrationForm()

    context = {'form': form}

    return render(request, 'users/register.html', context)
            


