from rest_framework import viewsets
from . import models
from . import serializers


class QuestionsViewset(viewsets.ModelViewSet):
    queryset = models.Questions.objects.all()
    serializer_class = serializers.QuestionsSerializer


class AnswersViewset(viewsets.ModelViewSet):
    queryset = models.Answers.objects.all()
    serializer_class = serializers.AnswersSerializer
