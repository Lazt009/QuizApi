from rest_framework import serializers

from .models import QuizQuestion

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = ('id', 'question', 'op1', 'op2', 'op3', 'op4')
