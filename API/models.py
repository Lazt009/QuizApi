from django.db import models

# Create your models here.
class QuizQuestion(models.Model):
    question = models.CharField(max_length=500)
    op1 = models.CharField(max_length=60)
    op2 = models.CharField(max_length=60)
    op3 = models.CharField(max_length=60)
    op4 = models.CharField(max_length=60)
    def __str__(self):
        return self.question[0:50]

class Answer(models.Model):
    questnId = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=60)

    def __str__(self):
        return self.answer
