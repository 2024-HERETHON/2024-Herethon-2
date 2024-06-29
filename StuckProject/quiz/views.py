from django.shortcuts import render, get_object_or_404, redirect
from .models import *


# 메인페이지
def home(request):
    # quizs = Quiz.objects.all()
    return render(request, 'quiz/home.html')

# 폴더 조회
def view_folder(request, folder_id=None):
    if folder_id:
        folder = get_object_or_404(Folder, id=folder_id)
        children = folder.get_children() # 하위에 있는 모든 폴더
    else:
        folder = None
        children = Folder.objects.filter(parent=None, user=request.user) # 루트에 있는 모든 폴더

    return render(request, 'quiz/view_folder.html', {'folder': folder, 'children': children})


# 폴더 추가
def add_folder(request, parent_id):
    if request.method == "GET":
        return render(request, 'quiz/add_folder.html', {'parent_id' : parent_id})
    
    if parent_id == 0:
        parent = None
    else:
        parent = get_object_or_404(Folder, id=parent_id)

    name = request.POST['folder_name']

    new_category = Folder.objects.create(name=name, parent=parent, user=request.user)
    # print(new_category.id)

    if parent == None:
        return redirect('folder-view', 0)
    return redirect('folder-view', parent.id)


# 폴더 드래그로 이동
def move_folder(request, folder_id, parent_id):
    folder = get_object_or_404(Folder, id=folder_id)

    if parent_id == 0:
        new_parent = None
    else:
        new_parent = get_object_or_404(Folder, id=parent_id)

    folder.parent = new_parent
    folder.save()

    if new_parent == None:
            return redirect('folder-view', 0)
    
    return redirect('folder-view', folder_id=new_parent.parent.id if new_parent.parent else 0)
