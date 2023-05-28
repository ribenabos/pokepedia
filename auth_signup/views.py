from django.shortcuts import render, redirect
from .forms import SignupForm
from django.utils.text import slugify

from .models import User


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = generate_unique_username(user.first_name, user.last_name)
            user.username = username
            user.save()
            # Redirect to signup success page
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
