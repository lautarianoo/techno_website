from django.contrib.auth import get_user_model, authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .form import UserLoginForm, UserRegisterForm

User = get_user_model()
def userloginview(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)
        login(request, user)
        return HttpResponseRedirect(reverse('reviews_ali:index'))
    return render(request, 'users/login.html', {'form': form})

def userregisterview(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password1'])
        new_user.save()
        return render(request, 'users/register_done.html', {'new_user': new_user})
    return render(request, 'users/register.html', {'form': form})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('reviews_ali:index'))