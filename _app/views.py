from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def accounts_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'registration/login.html')

@login_required(login_url='login')
def account_logout(request):
    logout(request)
    next_url = reverse('login') + '?next=logout'
    return redirect(next_url)


def error_500view(request):
    return render(request, 'errors/500.html', status=500)

def error_404view(request, exception):
    return render(request, 'errors/404.html', status=404)

def error_403view(request, exception):
    return render(request, 'errors/403.html', status=403)

def error_400view(request, exception):
    return render(request, 'errors/400.html', status=400)

@login_required(login_url='login')
def license(request):
    return render(request, 'components/license.html')

@login_required(login_url='login')
def documentation(request):
    return render(request, 'components/documentation.html')
