from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializer import QuestionSerializer
from .models import QuizQuestion


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = QuizQuestion.objects.all()
    serializer_class = QuestionSerializer
