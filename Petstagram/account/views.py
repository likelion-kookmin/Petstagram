from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.views.decorators.http import require_http_methods
# Create your views here.
# 회원가입
def signup_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("index")
    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'form' : form})

#로그인
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request = request, username = username, password = password)
            if user is not None:
                login(request, user)
            
            return redirect("index")
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form' : form})

#로그아웃
def logout_view(request):
    logout(request)
    return redirect("index")