from rest_framework.routers import DefaultRouter

from .viewsets import (
    ReadingViewSet,
    SpellingViewSet,
    VocabularyViewSet
)

__author__ = ['jbui']


router = DefaultRouter()
router.register(r'readings', ReadingViewSet, 'reading')
router.register(r'spellings', SpellingViewSet, 'spelling')
router.register(r'vocabulary', VocabularyViewSet, 'vocabulary')
