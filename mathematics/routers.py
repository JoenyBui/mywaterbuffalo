from rest_framework.routers import DefaultRouter

from .viewsets import (
    MathViewSet,
    FractionViewSet,
    AdditionViewSet,
    SubtractionViewSet,
    MultiplicationViewSet,
    DivisionViewSet
)

__author__ = ['jbui']

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'maths', MathViewSet, 'math')
router.register(r'fractions', FractionViewSet, 'fraction')
router.register(r'additions', AdditionViewSet, 'addition')
router.register(r'subtractions', SubtractionViewSet, 'subtraction')
router.register(r'multiplications', MultiplicationViewSet, 'multiplication')
router.register(r'divisions', DivisionViewSet, 'division')
