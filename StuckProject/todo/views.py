from django.shortcuts import render, redirect, get_object_or_404
from .models import Routine, ToDo
from .forms import RoutineForm, ToDoForm
from accounts.models import *
from datetime import date


def todo_list(request,  year, month, day, offset):
    user = get_object_or_404(User, id=request.user.id)
    custom_user = get_object_or_404(CustomUser, user=user)

    if request.method == 'POST':
        routine_form = RoutineForm(request.POST)
        todo_form = ToDoForm(request.POST)

        # 루틴 추가
        if 'routine_submit' in request.POST:
            if routine_form.is_valid():
                routine = routine_form.save(commit=False)
                routine.user = custom_user
                routine.save()
                return redirect('accounts:mypage_by_date', year, month, day, offset)
        
        # 할일 추가
        elif 'todo_submit' in request.POST:
            print("todo_submit")
            if todo_form.is_valid():
                routine_id = request.POST.get('routine_id')
                routine = get_object_or_404(Routine, id=routine_id)
                todo = todo_form.save(commit=False)
                todo.date = date(year, month, day)
                todo.routine = routine
                todo.save()
                return redirect('accounts:mypage_by_date', year, month, day, offset)
    else:
        routine_form = RoutineForm()
        todo_form = ToDoForm()
    
    return redirect('accounts:mypage_by_date', year, month, day, offset)


# 할 일 완료
def complete_todo(request, year, month, day, offset, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    if todo.completed:
        todo.completed = False
    else:
        todo.completed = True
    todo.save()
    return redirect('accounts:mypage_by_date', year, month, day, offset)


# 루틴 삭제
def delete_routine(request,  year, month, day, offset, pk):
    routine = get_object_or_404(Routine, id=pk)
    routine.delete()
    return redirect('accounts:mypage_by_date', year, month, day, offset)
