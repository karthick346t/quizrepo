from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Question

def home(request):
    return redirect('login')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('quiz')
        else:
            return render(request, 'quiz/login.html', {'error': 'Invalid credentials'})
    return render(request, 'quiz/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'quiz/signup.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'quiz/signup.html', {'error': 'Username already exists'})

        User.objects.create_user(username=username, password=password1)
        return redirect('login')

    return render(request, 'quiz/signup.html')

@login_required
def quiz(request):
    questions = Question.objects.all()  # Fetch all questions from the database
    
    # Handle form submission (POST)
    if request.method == 'POST':
        score = 0
        total_questions = len(questions)

        for question in questions:
            selected_option = request.POST.get(f"question{question.id}")  # Get the selected option for each question
            
            # Check if the selected option is correct
            if selected_option and int(selected_option) == question.correct_option:
                score += 1
        
        # Render the result page
        return render(request, 'quiz/result.html', {'score': score, 'total': total_questions})

    # Render the quiz page with the questions
    return render(request, 'quiz/quiz.html', {'questions': questions})