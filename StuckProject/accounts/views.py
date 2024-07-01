from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


# Create your views here.
def signup(request):
    if request.method=='POST':    
        if request.POST['password'] == request.POST['password2']:
            new_user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
                email=request.POST['email']
                )
            nickname=request.POST['nickname']
            univ = request.POST['univ']
            semester = request.POST['semester']
            resolution = request.POST['resolution']
            customuser = CustomUser(user=new_user, nickname=nickname, univ=univ, semester=semester, resolution=resolution, introduce="")
            customuser.save()

        elif request.POST['password'] != request.POST['password2']:
            error_message = "비밀번호가 일치하지 않습니다"
            return render(request, 'accounts/signup.html', {'error_message': error_message})
        return redirect('accounts:login')

    return render(request, 'accounts/signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('quiz:home')
        
        else:
            error_message = "아이디 또는 비밀번호가 잘못되었습니다."
            return render(request, 'accounts/login.html', {'error_message': error_message})
        
    else:
        return render(request, 'accounts/login.html')
    
def logout(request):
    auth_logout(request)
    return redirect('quiz:home')