from rest_framework.routers import DefaultRouter

from .viewsets import ProblemBaseModelViewSet, ProblemInstanceModelViewSet
from .viewsets import AnswerInstanceModelViewSet, AnswerFillInTheBlankModelViewSet
from .viewsets import AnswerMultipleChoiceModelViewSet, AnswerTrueOrFalseModelViewSet


router = DefaultRouter()
router.register('problem-base', ProblemBaseModelViewSet, 'problem-base')
router.register('problem-instance', ProblemInstanceModelViewSet, 'problem-instance')
router.register('answer-instance', AnswerInstanceModelViewSet, 'answer-instance')
router.register('answer-fill-in-the-blank', AnswerFillInTheBlankModelViewSet, 'answer-fill-in-the-blank')
router.register('answer-multiple-choice', AnswerMultipleChoiceModelViewSet, 'answer-multiple-choice')
router.register('answer-true-or-false', AnswerTrueOrFalseModelViewSet, 'answer-true-or-false')
