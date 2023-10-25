from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Profile
from .forms import CreateUserForm


def sign_up(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            pwd = form.cleaned_data.get('password1')
            cpwd=form.cleaned_data.get('password2')
            if(pwd!=cpwd):
                messages.error(request,'Password does not match')
                return render(request, 'users/createacc.html', {'form': form})
            form.save()
            return redirect('log_in')
    elif request.method == "GET":
        form = CreateUserForm()
        return render(request, 'users/createacc.html', {'form': form})
    
def on_login(request):
    profile=Profile.objects.filter(user=request.user)
    if profile.is_customer():
        return redirect('fooditems:home')
    else:
        return redirect('orders:home')