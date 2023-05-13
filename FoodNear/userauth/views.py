from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.db import IntegrityError
# Create your views here.
def index(request):
    if request.POST:
        if 'create_user' in request.POST:
            try:
                username = request.POST.get('username', '')
                password = request.POST.get('password', '')
                email = request.POST.get('usermail', '')
                user = User.objects.create_user(username=username, password=password,email = email)
                user.save()
                return render(request, 'userauth/registration.html',{'signupIsSuccess': True})
            except IntegrityError:
                return render(request,'userauth/registration.html',{'error' : 'Такой логин уже существует'} )

        elif 'login_user' in request.POST:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/main/')
            else:
                return render(request,'userauth/registration.html',{'error' : 'Неверный логи или пароль'} )
    return render(request, 'userauth/registration.html')
def out(request):
    logout(request)
    return redirect('../')