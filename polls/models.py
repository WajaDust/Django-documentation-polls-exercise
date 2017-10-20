from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Question(models.Model):
    question_text = models.CharField(max_length=200, default=None)
    pub_date = models.DateTimeField('date published', default=None)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    choice_text = models.CharField(max_length=200, default=None)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text