from django.shortcuts import render, redirect
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
        elif request.POST['password'] != request.POST['password2']:
            error_message = "비밀번호가 일치하지 않습니다"
            return render(request, 'signup.html', {'error_message': error_message})

    return render(request, 'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            error_message = "로그인 성공"
            return render(request, 'login.html', {'error_message': error_message})
            # return redirect('home')
        
        else:
            error_message = "아이디 또는 비밀번호가 잘못되었습니다."
            return render(request, 'login.html', {'error_message': error_message})
        
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth_logout(request)
    # return redirect('home')