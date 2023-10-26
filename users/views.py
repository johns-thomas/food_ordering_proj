from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Profile
from .forms import CreateUserForm
from users.forms import ProfileCreationForm

def sign_up(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        pform = ProfileCreationForm(request.POST)
        if form.is_valid() and pform.is_valid():
            user=form.save()
            profile= pform.save(commit=False)
            profile.user=user
            profile.save()
            return redirect('users:log_in')
        
    elif request.method == "GET":
        form = CreateUserForm()
        profileform = ProfileCreationForm(instance=request.user.profile)
    return render(request, 'users/createacc.html', {'form': form,'profileform':profileform,'is_staff':False})

def staff_signup(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            profile= Profile()
            profile.user=user
            profile.role='staff'
            profile.save()
            return redirect('log_in')
        
    elif request.method == "GET":
        form = CreateUserForm()
    return render(request, 'users/createacc.html', {'form': form,'is_staff':True})



def on_login(request):
    #profile=Profile.objects.filter(user=request.user).values().first()
    #print(request.user)
    #print(profile)
    if request.user.profile.role=='customer':
        return redirect('fooditems:home')
    else:
        return redirect('orders:view_orders')