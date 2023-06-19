from django.db import models
from django.urls import reverse

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateField()

    def __str__(self):
        return self.question_text

    def get_absolute_url(self):
        return reverse("detail-poll", args=[self.id])


class Choice(models.Model):
    question = models.ForeignKey(
        Question, related_name="choices", on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    vote_number = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
