from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Question, Choice
from .forms import QuestionForm, ChoiceForm
from django.urls import reverse

# Create your views here.
def index(request):
    latest_questions = Question.objects.all()
    return render(request, "polls/index.html", {'questions':  latest_questions})

def details(request, question_id):
    question_details = get_object_or_404(Question, pk=question_id)
    context = {'question' : question_details}
    return render(request, "polls/details.html", context)

def add_question(request):
    if request.method == 'POST':
        question = QuestionForm(request.POST)
        if question.is_valid():
            qtext = request.POST.get('question_text')
            pdate = request.POST.get('pub_date')
            question = Question(question_text = qtext, pub_date = pdate )
            question.save()
            return HttpResponseRedirect(reverse('polls:index'))
        else:
            return HttpResponseRedirect(reverse('polls:add_question'))
    else:
        question = QuestionForm()
        return render(request, 'polls/add_question.html', {'question':question})


def add_choice(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    if request.method == 'POST':
        choice = ChoiceForm(request.POST)
        ch_text = request.POST.get('choice_text')
        vts = request.POST.get('votes', 0)
        question.choice_set.create(choice_text = ch_text, votes = vts)
        question.save()
        return HttpResponseRedirect(reverse('polls:details', args = (question.id, )))
    else:
        choice = ChoiceForm()
        return render(request, 'polls/add_choice.html', {'choice':choice, 'question':question})
    
def update_choice(request, choice_id):
    choice = Choice.objects.get(pk=choice_id)
 
    if request.method == "POST":
        new_text = request.POST["choice_text"]
        choice.choice_text = new_text
        choice.save()
 
        return HttpResponseRedirect("polls:details", choice.question.id)
 
    return render(request, "polls/update_choice.html", {"choice": choice})
 