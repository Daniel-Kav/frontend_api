from django import forms
from .models import Lesson, Quiz,Course

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'content']

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['question', 'answer']

