from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializer import QuestionSerializer, AnswerSerializer
from .models import QuizQuestion, Answer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = QuizQuestion.objects.all()
    serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
