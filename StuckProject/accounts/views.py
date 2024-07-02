from datetime import date, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser
from todo.models import Routine, ToDo
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



# 마이페이지 - 본인 정보 수정 
def mypage(request):
    if request.method == "POST":
        request.user.customuser.nickname = request.POST['nickname']
        request.user.customuser.resolution = request.POST['resolution']
        request.user.customuser.introduce = request.POST['introduce']
        request.user.customuser.save()

    user = get_object_or_404(User, id=request.user.id)
    custom_user = get_object_or_404(CustomUser, user=user)

    # 루틴 및 투두 정보
    routines = Routine.objects.filter(user=custom_user)
    todos = ToDo.objects.filter(routine__in=routines)

    # Calculate the current week
    today = date.today()
    start_of_week = today - timedelta(days=(today.weekday() + 1) % 7)  # Sunday
    end_of_week = start_of_week + timedelta(days=6)  # Saturday
    
    week_days = []
    for i in range(7):
        day = start_of_week + timedelta(days=i)
        day_name = day.strftime('%a')
        day_todos = todos.filter(date=day)
        completed_count = day_todos.filter(completed=True).count()
        pending_count = day_todos.filter(completed=False).count()
        color = "blue" if completed_count > 0 else "gray"
        week_days.append({
            'day_name': day_name,
            'date': day.day,
            'todo_count': pending_count,
            'completed_count': completed_count,
            'color': color
        })

    context = {
        'week_days': week_days,
        'today': today,
    }

    return render(request, 'accounts/mypage.html', context)