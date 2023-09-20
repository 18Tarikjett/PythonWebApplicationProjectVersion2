from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm


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
    if request.method == 'POST':
        update_user = UserUpdateForm(request.POST, instance=request.user)
        update_profile = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if update_user.is_valid() and update_profile.is_valid():
            update_user.save()
            update_profile.save()
            messages.success(request, f'Your profile has been updated successfully. ')
            return redirect('profile')
    else:
        update_user = UserUpdateForm(instance=request.user)
        update_profile = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form':update_user,
        'p_form':update_profile
    }
    return render(request, 'profile.html', context)