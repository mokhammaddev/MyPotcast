from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('blog:index')
    return render(request, 'account/login.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('blog:index')
    return render(request, 'account/logout.html')


def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('.')
    ctx = {
        'form': form
    }
    return render(request, 'account/register.html', ctx)

