from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('user------------------------------------>', user)
            return redirect('login') 
    else:
        form = CustomUserForm()
    return render(request, 'accounts/register.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         print('username ------------------------>', username )
#         print('user ------------------------>', password)
#         user = authenticate(request, username=username, password=password)
#         print('user ------------------------>', user)
#         if user:
#             login(request, user)
#             return redirect('home')
#     return render(request, 'accounts/login.html')


# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user:
#             login(request, user)
#             return redirect('home')  # Redirect to the home page after login
#         else:
#             messages.error(request, "Invalid username or password!")

#     return render(request, 'accounts/login.html')

def user_login(request):
    # Check if the user is already logged in
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home if already logged in

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Successful login: log the user in
            login(request, user)
            
            # Get user information except password
            user_info = {
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'role': getattr(user, 'role', 'guest'),  # Safely get role from custom user model
                'last_login': user.last_login,
                'date_joined': user.date_joined
            }

            # Debugging: print user information (or save to a log file)
            print(f"User Information: {user_info}")

            # Check the user's role and print it for debugging (optional)
            user_type = user_info.get('role', 'guest')  # Default to 'guest' if no role is defined
            print(f"User Role: {user_type}")

            # Redirect the user to the home page after successful login
            return redirect('home')
        
        else:
            # Invalid login credentials: Render the login page with an error message
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})

    # GET request: Render the login page
    return render(request, 'accounts/login.html')