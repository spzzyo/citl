# views.py

from rest_framework import generics
from .models import Question
from .serializers import QuestionSerializer
from django.views.generic import TemplateView
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# def index(request):
#     template = loader.get_template('quiz/question_list.html')
#     questions = [
#         {'id': 1, 'question': 'What is the capital of France?', 'answer': 'Paris'},
#         {'id': 2, 'question': 'What is 2 + 2?', 'answer': '4'},
#         # Add more questions and answers as needed
#     ]

#     context = {'questions': questions}
   
#     return render(request, 'quiz/question_list.html', context)



def index(request):
    # Assuming your API endpoint is 'api/questions/'
    api_url = 'http://127.0.0.1:8000/api/questions/'  # Replace with your actual API URL

    # Fetch data from the API
    response = requests.get(api_url)

    if response.status_code == 200:
        questions = response.json()
    else:
        # Handle the error case, for example, by providing a default set of questions
        questions = [
            {'id': 1, 'text': 'Default Question 1', 'answer': 'Default Answer 1'},
            {'id': 2, 'text': 'Default Question 2', 'answer': 'Default Answer 2'},
        ]

    context = {'questions': questions}
   
    return render(request, 'quiz/question_list.html', context)


