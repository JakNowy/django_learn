from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrerForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def resister(request):
    if request.method == 'GET':
        form = UserRegistrerForm()
    else:
        form = UserRegistrerForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You can now log in!!')
            return redirect('login')
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    if request.method == 'GET':
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    else:
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('profile')
        else:
            messages.error(request, f'Invalid data.')

    context = {
        'u_form':u_form,
        'p_form':p_form,
    }

    return render(request, 'users/profile.html', context)
