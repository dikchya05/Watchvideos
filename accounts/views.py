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
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            # Get user information except password
            user_info = {
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'role': user.role,  # Use the 'role' field from CustomUser model
                'last_login': user.last_login,
                'date_joined': user.date_joined
            }

            # Print or use this user information as needed
            print('User Information:', user_info)

            # Check the user's role to define if the user is an admin or normal user
            user_type = user.role if user.role else 'guest'  # Default to 'normal' if no role assigned

            print('user role --------------------------------------->', user_type)
            return redirect('home')  # Redirect to home page after login
        else:
            # Invalid credentials
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})

    return render(request, 'accounts/login.html')