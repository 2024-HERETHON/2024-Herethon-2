from django.shortcuts import render

# Create your views here.
def home(request):
    # quizs = Quiz.objects.all()
    return render(request, 'quiz/home.html')
