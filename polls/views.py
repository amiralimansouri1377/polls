from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from .form import ChoiceForm

# Create your views here.


def index(request):
    questions = Question.objects.order_by("-pub_date")
    return render(request, "polls/index.html", {
        "questions": questions
    })


def detail_poll(request, id):
    question = Question.objects.get(pk=id)
    choices = question.choices.all()

    radio_choices = [(c.id, c) for c in choices]
    form = ChoiceForm(radio_choices=radio_choices)

    return render(request, "polls/detail.html", {
        "question": question,
        "form": form
    })


class VoteView(View):
    def post(self, request, id):
        form = ChoiceForm(request.POST)

        if form.is_valid():
            choice_id = form.cleaned_data["choice"]
            choice = Choice.objects.get(pk=choice_id)
            choice.vote_number += 1
            choice.save()
            return HttpResponseRedirect(reverse("result", args=[id]))
        

def result(request, id):
    question = get_object_or_404(Question, pk=id)
    choices = question.choices.order_by("-vote_number")

    return render(request, "polls/result.html", {
        "question": question,
        "choices": choices
    })