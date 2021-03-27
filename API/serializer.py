from rest_framework import serializers

from .models import QuizQuestion,Answer

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = ('id', 'question', 'op1', 'op2', 'op3', 'op4')

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'questnId', 'answer')
