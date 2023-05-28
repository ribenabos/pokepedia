from .forms import SignupForm
from django.utils.text import slugify

from .models import User

from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm
from .backend import EmailBackend


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = EmailBackend().authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                user.is_authenticated = True
                return redirect('index')
            else:
                return render(request, 'auth_signup/login.html', {'form': form})
        else:
            return render(request, 'auth_signup/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'auth_signup/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = generate_unique_username(user.first_name, user.last_name)
            user.username = username
            user.save()
            return redirect('signup_success')
    else:
        form = SignupForm()

    return render(request, 'auth_signup/signup.html', {'form': form})


def generate_unique_username(first_name, last_name):
    base_username = slugify(first_name + last_name)
    username = base_username
    suffix = 1
    while User.objects.filter(username=username).exists():
        username = f"{base_username}{suffix}"
        suffix += 1

    return username


def signup_success(request):
    return render(request, 'auth_signup/signup_success.html')
