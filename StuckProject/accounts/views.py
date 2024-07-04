from datetime import date, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from todo.models import Routine, ToDo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from todo.forms import RoutineForm, ToDoForm

from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage

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
            introduce = request.POST['introduce']
            customuser = CustomUser(user=new_user, nickname=nickname, univ=univ, semester=semester, resolution=resolution, introduce=introduce)
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
@login_required
def mypage(request, year=None, month=None, day=None, week_offset=0):
    
    chlicked_day = {
        'year': year,
        'month': month,
        'day': day
    }

    return render(request, 'accounts/mypage.html')



# 아이디 찾기
def forgot_id(request):
    context = {}
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            if user:
                method_email = EmailMessage(
                    'STUCK에서 온 아이디 찾기 메일입니다.',
                    str(user.username),
                    settings.EMAIL_HOST_USER,
                    [email],
                )
                method_email.send(fail_silently=False)
                messages.success(request, "이메일로 아이디가 전송되었습니다.")
                return render(request, 'accounts/login.html', context)
        except User.DoesNotExist:
            messages.info(request, "등록된 이메일이 없습니다.")
        
    return render(request, 'accounts/forgot_id.html', context)            


# 마이페이지 - 본인 정보 수정 
@login_required
def mypage(request, year=None, month=None, day=None, week_offset=0):
    
    chlicked_day = {
        'year': year,
        'month': month,
        'day': day
    }

    user = get_object_or_404(User, id=request.user.id)
    custom_user = get_object_or_404(CustomUser, user=user)

    if request.method == "POST":
        custom_user.nickname = request.POST['nickname']
        custom_user.resolution = request.POST['resolution']
        custom_user.introduce = request.POST['introduce']
        custom_user.save()

    # 루틴 및 투두 정보
    routines = Routine.objects.filter(user=custom_user)

    if year and month and day:
        selected_date = date(year, month, day) 
    else:
        selected_date = date.today() 

    # offset 만큼 week 변화
    selected_date += timedelta(weeks=week_offset)

    # 클릭한 날짜에 해당하는 todo를 가져옴
    todos = ToDo.objects.filter(routine__in=routines, date=selected_date)

    # 일요일 시작 
    start_of_week = selected_date - timedelta(days=(selected_date.weekday() + 1) % 7)  # Sunday
    end_of_week = start_of_week + timedelta(days=6)  # Saturday

    # 주에 걸친 월 정보
    start_month = start_of_week.month
    end_month = end_of_week.month
    start_year = start_of_week.year
    end_year = end_of_week.year

    if start_month == end_month:
        week_month = f"{start_year}년 {start_month}월"
    else:
        week_month = f"{start_year}년 {start_month}월 - {end_month}월"

    week_days = []
    for i in range(7):
        day = start_of_week + timedelta(days=i)
        day_name = day.strftime('%a')

        day_todos = ToDo.objects.filter(routine__in=routines, date=day)
        completed_count = day_todos.filter(completed=True).count()
        pending_count = day_todos.filter(completed=False).count()

        color = "blue" if completed_count > 0 else "gray"

        week_days.append({
            'day_name': day_name,
            'date': day,
            'todo_count': pending_count,
            'completed_count': completed_count,
            'color': color
        })

    total_todos = todos.count()
    completed_todos = todos.filter(completed=True).count()
    completion_rate = (completed_todos / total_todos * 100) if total_todos > 0 else 0

    routine_form = RoutineForm()
    todo_form = ToDoForm()

    context = {
        'week_days': week_days,
        'selected_date': selected_date,
        'routines': routines,  
        'todos': todos,  
        'completion_rate': completion_rate,
        'routine_form': routine_form,
        'todo_form': todo_form,
        'week_offset': week_offset,
        'chlicked_day': chlicked_day,
        'week_month': week_month,
        'today_day': date.today().day
    }

    return render(request, 'accounts/mypage.html', context)