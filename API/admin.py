from django.contrib import admin

# Register your models here.
from .models import QuizQuestion,Answer

admin.site.register(QuizQuestion)
admin.site.register(Answer)
