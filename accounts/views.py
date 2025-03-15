from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm
from django.contrib import messages

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.models import User  # Import if using default User model

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


# User Login View
def user_login(request):
    # Redirect already logged-in users to the home page
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in.')
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}! You have successfully logged in.")

            # Log user information for debugging (optional)
            user_info = {
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'role': getattr(user, 'role', 'guest'),
                'last_login': user.last_login,
                'date_joined': user.date_joined
            }
            print(f"User Information: {user_info}")
            print(f"User Role: {user_info['role']}")

            return redirect('home')
        else:
            messages.success(request, 'Invalid username or password. Please try again.')

    return render(request, 'accounts/login.html')