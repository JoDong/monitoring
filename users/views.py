from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from users.forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            login(request, user)
            return redirect('/')
        else:
            render(request, 'users/login.html', {'form': form})
    else:
        return render(request, 'users/login.html', {'form': LoginForm()})


def user_logout(request):
    logout(request)
    return redirect('home')