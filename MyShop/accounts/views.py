from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views import View


def LoginView(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'success')
            else:
                messages.error(request, 'your username or password is wrong', 'danger')
    else:
        form = LoginForm

    return render(request, "accounts/login.html", {'form': form})


def RegisterView(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['phone_number'], cd['email'], cd['full_name'], cd['password'])
            user.save()
            messages.success(request, 'you registered successfully', 'success')
            return redirect('views:home')
    else:
        form = RegisterForm

    return render(request, "accounts/register.html", {'forms': form})



def LogoutView(request):
    logout(request)
    messages.success(request, 'you logged out successfully', 'success')
    return redirect('views:home')