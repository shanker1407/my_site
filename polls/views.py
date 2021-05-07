from django.http import HttpResponseRedirect
from django.shortcuts import render
from polls.models import Question, Choice


def home(request):
    question = Question.objects.order_by('pub_date')[:5]
    return render(request, 'polls/home.html', {'question': question})


def details(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = Choice.objects.filter(question_id=question_id)
    choices = question.choice_set.all()
    return render(request, 'polls/details.html', {'question': question, 'choices': choices})


def vote(request, question_id):
    print(request.POST)
    question = Question.objects.get(id=question_id)
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(f"/polls/{question_id}/result/")


def results(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'polls/result.html', {'question': question})
