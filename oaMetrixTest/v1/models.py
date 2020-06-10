from django.db import models

class Questions(models.Model):
    questions = models.CharField(max_length=100)


class Answers(models.Model):
    answers = models.CharField(max_length=100)
    questionID = models.CharField(max_length=15)

