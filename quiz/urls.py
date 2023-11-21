


from django.urls import path
from .views import QuestionListCreateAPIView, QuestionDetailAPIView, index

urlpatterns = [
    path('questions/', QuestionListCreateAPIView.as_view(), name='question-list-create'),
    path('questions/<int:pk>/', QuestionDetailAPIView.as_view(), name='question-detail'),
    path('quiz/', index, name='question-list'),
    
    
]
