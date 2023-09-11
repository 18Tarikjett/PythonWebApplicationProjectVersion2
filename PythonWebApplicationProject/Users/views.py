from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Accound created for {username}')
            return redirect('Users-login')
    else: 
        user_form = UserRegistrationForm()
    return render(request,'register.html', {'form' : user_form})


@login_required
def profile(request):
    return render(request, 'profile.html')