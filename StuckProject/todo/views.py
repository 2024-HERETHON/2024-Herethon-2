from django.shortcuts import render, redirect, get_object_or_404
from .models import Routine, ToDo
from .forms import RoutineForm, ToDoForm

def todo_list(request):
    if request.method == 'POST':
        routine_form = RoutineForm(request.POST)
        todo_form = ToDoForm(request.POST)
        
        # 루틴 추가
        if 'routine_submit' in request.POST:
            if routine_form.is_valid():
                routine_form.save()
                return redirect('todo:todo_list')
        
        # 할일 추가
        elif 'todo_submit' in request.POST:
            if todo_form.is_valid():
                routine_id = request.POST.get('routine_id')
                routine = get_object_or_404(Routine, id=routine_id)
                todo = todo_form.save(commit=False)
                todo.routine = routine
                todo.save()
                return redirect('todo:todo_list')
    else:
        routine_form = RoutineForm()
        todo_form = ToDoForm()
    
    routines = Routine.objects.all()
    todos = ToDo.objects.all()
    total_todos = todos.count()
    completed_todos = todos.filter(completed=True).count()
    completion_rate = (completed_todos / total_todos * 100) if total_todos > 0 else 0

    return render(request, 'todo/todo_list.html', {
        'routine_form': routine_form,
        'todo_form': todo_form,
        'routines': routines,
        'completion_rate': completion_rate,
    })

# 할 일 완료
def complete_todo(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    todo.completed = True
    todo.save()
    return redirect('todo:todo_list')
