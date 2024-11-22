from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django import forms
from .models import CustomUser

class CustomUserCreationRole(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'role')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        selected_role = request.POST.get('role')

        print(f"Trying to authenticate user: {username}")  
        print(f"Selected role: {selected_role}")  

        user = authenticate(request, username=username, password=password, role=selected_role)

        if user is not None:
            print(f"Authenticated user: {username} with role: {user.role}")  

            if user.role == selected_role:
                login(request, user) 
                print(f"User {username} logged in successfully.") 

                if selected_role == 'organizer':
                    messages.success(request, 'Login successful! Redirecting to event page.')
                    return redirect('/event')  
                elif selected_role == 'volunteer':
                    messages.success(request, 'Login successful! Redirecting to volunteer page.')
                    return redirect('/volunteer')  
            else:
                messages.error(request, f'Selected role "{selected_role}" does not match your account role "{user.role}". Please select the correct role.')
                return redirect('/auth/login')
        else:
            messages.error(request, 'Invalid username or password.')
            print(f"Authentication failed for user: {username}")  

    return render(request, 'user_auth/login.html')  


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationRole(request.POST)  

        if form.is_valid():
            user = form.save()  
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('/auth/login')
        else:
            messages.error(request, "Registration failed, please correct all errors.")
    else:
        form = CustomUserCreationRole()  
    return render(request, 'user_auth/register.html', {'form': form})
