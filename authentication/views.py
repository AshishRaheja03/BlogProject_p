from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib  import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        username = email.split('@')[0]

        user = User.objects.filter(username=username)
        if not user.exists():
            messages.info(request, "User does not exist. Please Register.")
            return render(request, 'authentication/login.html')

        user = authenticate(username=username, password=password)
        if not user:
            messages.error(request, "Incorrect Username or Password.")
            return render(request, 'authentication/login.html')
        else:
            login(request, user)
            return redirect('/', {'username': username})
                
    return render(request, 'authentication/login.html')

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'authentication/signup.html', {'first_name': first_name, 'last_name': last_name, 'email': email})

        username = email.split('@')[0] 

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "User already exists.")
            return render(request, 'authentication/signup.html')

        user = User.objects.create_user(
            username=username,   
            email=email,
            password=password
            )
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        messages.success(request, "Account created Successfully!")
        return redirect('/auth/login/')

    return render(request, 'authentication/signup.html')

def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect('/auth/login/')