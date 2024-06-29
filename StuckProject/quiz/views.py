from django.shortcuts import render, get_object_or_404, redirect
from .models import *
import os

# openai
import openai
from django.conf import settings

# pdf에서 text 추출 
import fitz

# 이미지에서 text 추출
from google.cloud import vision


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
    if parent_id == 0:
        parent = None
    else:
        parent = get_object_or_404(Folder, id=parent_id)

    name = request.POST['folder_name']

    Folder.objects.create(name=name, parent=parent, user=request.user)
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


# pdf 파일 열기 및 텍스트 추출
def extract_text_from_pdf(file_path):
    document = fitz.open(file_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text


# 문제와 정답 항목 분리
def extract_questions_and_answers(response, type):
    print("all" + response)
    questions_part, answers_part = response.split("Answers:")
    
    # 문제 부분을 줄 단위로 분리
    questions_lines = questions_part.split("\n\n")
    
    # 문제를 담을 리스트 초기화
    questions = []
    
    # 각 질문을 확인하며 리스트에 추가
    for question in questions_lines:
        if question.strip():
            questions.append(question.strip())
    
    # 답안 부분을 줄 단위로 분리
    answers = answers_part.strip().split('\n')
    
    # 객관식일 경우
    if type == "객관식":
        # 숫자 이외의 값 제거
        answers = [answer.strip() for answer in answers if answer.strip().isdigit()]
    
    return questions, answers


# 이미지 인식하여 텍스트 추출 (google vision)
def extract_text_from_image(image_file_path):
    client = vision.ImageAnnotatorClient()

    # 파일 경로에서 이미지 파일을 읽어와 바이트 스트림으로 변환
    with open(image_file_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # 텍스트 인식
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if response.error.message:
        raise Exception(f'{response.error.message}')

    return texts[0].description if texts else ''



# 퀴즈 생성 
def create_question(request, folder_id):
    # print(settings.OPENAI_API_KEY)
    if request.method == "GET":
        return render(request, 'quiz/create_quiz.html', {'folder_id':folder_id})
    
    folder = get_object_or_404(Folder, id=folder_id)

    file = request.FILES.get('file')
    title = request.POST['title']
    question_num = request.POST['question_num']
    type = request.POST['type']

    # 퀴즈 생성
    quiz = Quiz.objects.create(
        folder=folder,
        file=file,
        title=title,
        question_num=int(question_num),
        type=type
    )

    file_path = quiz.file.path

    # 업로드한 파일이 pdf라면 
    if quiz.file and quiz.file.name.lower().endswith('.pdf'):
        # PyMuPDF 라이브러리를 사용하여 PDF 파일에서 텍스트 추출
        text = extract_text_from_pdf(file_path)
    else:
        # google cloud vision을 사용하여 이미지에서 텍스트 추출
        text = extract_text_from_image(file_path)

    openai.api_key = settings.OPENAI_API_KEY

    print(text)
    print(type)

    # 모델 - GPT 4 Turbo 선택
    model = "gpt-4-turbo"

    # 주관식을 선택했을 경우 프롬프트
    if type == "주관식":
        query = f"""
            이 내용을 기반으로 {question_num}개의 {type} 문제를 내줘. 
            문제의 답안은 서술형이 아닌 단어 하나여야 해.
            각 문제의 시작은 문제 1. 처럼 문제 + 문제 번호 수 .이야. 
            문제는 꼭 물음표로 끝나야 해.
            문제는 모두 \n\n\n으로 꼭 구분해줘.
            예를 들어서 문제 1. 첫번째 문제 제시.\n\n\n문제2. 두번째 문제 제시.\n\n\n처럼 문제를 \n\n\n으로 구분해서 응답해줘.
            문제를 모두 내준 후 답안은 Answers: 으로 구분해서 아래에 답도 알려줘. Answers: 외에 구분선을 넣으면 안돼.
            Answers: 아래에 답안을 알려줄때는 문제 번호, 문항 내용 없이 문제 답만 작성하고 답 구분은 \n으로 해줘.
            꼭 답안이 서술형이 아닌 단어 하나로 구성해줘.
        """
    # 객관식을 선택했을 경우 프롬프트
    else : 
        query = f"""
        이 내용을 기반으로 {question_num}개의 {type} 문제를 내줘. 
        각 문제의 시작은 문제 1. 처럼 문제 + 문제 번호 수 .이야. 
        문제는 꼭 물음표로 끝나야 해.
        각 문제의 항목은 1. 2. 3. 4. 처럼 [숫자.]으로 시작하고 문제마다 4개야. 
        문제는 모두 \n\n\n으로 구분해줘. 
        문제를 모두 내준 후 답안은 Answers: 으로 구분해서 아래에 답도 알려줘. Answers: 외에 구분선을 넣으면 안돼.
        Answers: 아래에 답안을 알려줄때는 문제 번호, 문항 내용 없이 문제 답 번호만 작성하고 답 구분은 \n으로 해줘.
        예를 들어서 1\n2\n4\n 처럼."""

    # 메시지 설정하기
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": text},
        {"role": "user", "content": query}
    ]

    # ChatGPT API 호출하기
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.8
    )

    # 응답 출력
    response = response['choices'][0]['message']['content']

    # 문제와 답안 추출
    questions, answers = extract_questions_and_answers(response, type)

    # 테스트 출력
    print("Questions:")
    for q in questions:
        print(q)
        print()

    print("Answers:")
    for a in answers:
        print(a)
        print()

    print(f"questions len {len(questions)}")
    print(f"answers len {len(answers)}")
    
    # 각 질문과 답안을 개별적으로 저장
    for i in range(0, int(question_num)):
        Question.objects.create(
            quiz=quiz,
            ai_question=questions[i],
            correct_answer=answers[i]
        )

    return redirect('test', folder_id, quiz.id)


# 퀴즈 풀기
def test(request, folder_id, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = list(quiz.questions.all())
    
    # 세션에서 현재 질문의 인덱스를 가져옴, 기본값은 0
    current_question_index = request.session.get('current_question_index', 0)
    
    # 사용자가 제출한 답을 처리
    if request.method == 'POST':
        user_answer = request.POST.get('answer')
        if user_answer is not None:
            question_id = request.POST.get('question_id')
            question = get_object_or_404(Question, id=question_id)
            question.user_answer = user_answer
            question.save()
        
        # 다음 질문으로 인덱스 증가
        current_question_index += 1
        request.session['current_question_index'] = current_question_index
    
    # 현재 질문 인덱스가 질문 리스트 범위를 벗어나면 결과 페이지로 이동
    if current_question_index >= len(questions):
        request.session['current_question_index'] = 0
        return redirect('quiz-results', folder_id=folder_id, quiz_id=quiz_id)
    
    # 현재 질문 가져오기
    current_question = questions[current_question_index]

    context = {
        'question': current_question,
         'quiz_id': quiz_id,
         'is_last_question': current_question_index == len(questions) - 1
    }
    
    return render(request, 'quiz/test.html', context)


# 퀴즈 결과 확인
def quiz_results(request, folder_id, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()

    correct_count = sum(1 for q in questions if q.status) # 맞은 개수
    total_questions = questions.count() # 전체 문제 수

    quiz.score = correct_count
    quiz.save()

    context = {
        'quiz': quiz,
        'questions': questions,
        'correct_count': correct_count,
        'total_questions': total_questions,
        'folder_id':folder_id
    }
    
    return render(request, 'quiz/results.html', context)


# 생성된 문제 전체 확인
def view_questions(request, folder_id, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    return render(request, 'quiz/view_questions.html', {'questions':questions, 'folder_id': folder_id})


# 생성된 문제 중 틀린 문제만 확인
def view_wrong_questions(request, folder_id, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.filter(status=False)
    return render(request, 'quiz/view_questions.html', {'questions':questions, 'folder_id': folder_id})

