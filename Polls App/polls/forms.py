from django import forms
from .models import Question, Choice
from django.utils import timezone
 
class QuestionForm(forms.ModelForm):
    question_text = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Enter Question Text', 'class':'form-control'
        }))
    pub_date = forms.DateTimeField(initial=timezone.now())
    
    class Meta:
        model = Question
        fields = ('question_text', 'pub_date')

class ChoiceForm(forms.ModelForm):
    choice_text=forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Enter Choice Text','class':'form-control'

        }))
    votes=forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder':'Enter votes','class':'form-control'
        }))
    class Meta:
        model=Choice
        fields='__all__'
