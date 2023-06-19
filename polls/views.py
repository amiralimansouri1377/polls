from django.shortcuts import render
from django.views import View
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
    def post(self, request):
        form = ChoiceForm(request.POST)

        if form.is_valid():
            choice_id = form.cleaned_data["choice"]
            choice = Choice.objects.get(pk=choice_id)
            choice.vote_number += 1
            choice.save()
            return render(request, "polls/detail.html")
