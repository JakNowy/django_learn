from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrerForm
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
    return render(request, 'users/profile.html')
