from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'users/base.html')


def register(request):
    error = None
    username = ''
    email = ''

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        if not username or not email or not password or not password2:
            error = 'Please fill in all fields.'
        elif password != password2:
            error = 'Passwords do not match.'
        elif User.objects.filter(username=username).exists():
            error = 'That username is already taken.'
        elif User.objects.filter(email=email).exists():
            error = 'That email is already registered.'
        else:
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')

    return render(request, 'todos/register.html', {
        'error': error,
        'username': username,
        'email': email,
    })