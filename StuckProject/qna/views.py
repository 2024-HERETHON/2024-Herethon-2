from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from accounts.models import *

# 퀴즈 생성 전 폴더 선택
@login_required
def select_folder(request, folder_id=None):
    if request.method == "POST":
        return redirect('qna:create-question-room', folder_id)
    if folder_id:
        folder = get_object_or_404(Folder, id=folder_id)
        children = folder.get_children() # 하위에 있는 모든 폴더
        path = "Stuck/" + folder.get_path()
    else:
        folder = None
        children = Folder.objects.filter(parent=None, user=request.user) # 루트에 있는 모든 폴더
        path = ""

    return render(request, 'qna/select_folder.html', {'folder': folder, 'children': children, 'path': path})


# 폴더 추가
def add_folder(request, parent_id):
    if parent_id == 0:
        parent = None
    else:
        parent = get_object_or_404(Folder, id=parent_id)

    name = request.POST['folder_name']

    Folder.objects.create(name=name, parent=parent, user=request.user)
    # print(new_category.id)

    if parent == None:
        return redirect('qna:select-folder', 0)
    return redirect('qna:select-folder', parent.id)


def create_question_room(request, folder_id):
    if request.method == "POST":
        file = request.FILES.get('file')
        title = request.POST['title']
        folder = get_object_or_404(Folder, id=folder_id)
        user = get_object_or_404(User, id=request.user.id)

        custom_user = get_object_or_404(CustomUser, user=user)

        question_room = QuestionRoom.objects.create(
            file=file,
            title=title,
            user=custom_user,
            folder=folder,
            memo=""
        )

        return redirect('qna:enter-question-room', folder_id, question_room.id)

    context = {
        'folder_id': folder_id
    }
    return render(request, "qna/create_question_room.html", context)


def enter_question_room(request, folder_id, question_room_id):
    return render(request, 'qna/question_room.html')