from v1.viewsets import QuestionsViewset
from v1.viewsets import AnswersViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('question', QuestionsViewset)
router.register('qanswer', AnswersViewset)
