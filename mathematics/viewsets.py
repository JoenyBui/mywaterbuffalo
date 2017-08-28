from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters

from rest_framework_extensions.mixins import NestedViewSetMixin

from problem import domain

from .models import Math

from .serializers import MathSerializer

__author__ = ['jbui']


class MathViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    **Mathematic Viewset**

    """
    queryset = Math.objects.all()
    serializer_class = MathSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('id', 'status', 'domain', 'qtype', 'editors', 'topics')
    search_fields = ('name', 'keys', 'stem')
    ordering_fields = ('id', 'created', 'modified', 'name',)


class FractionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    **Fraction Viewset**

    """
    queryset = Math.objects.filter(topics__key=domain.DOMAIN_FRACTIONS)
    serializer_class = MathSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = ('id', 'name', 'status', 'qtype', 'editors', )
    search_fields = ('name', 'keys', 'stem')
    ordering_fields = ('id', 'created', 'modified', 'name',)


class AdditionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    **Addition Viewset**

    """
    queryset = Math.objects.filter(topics__key=domain.DOMAIN_ADDITION)
    serializer_class = MathSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = ('id', 'name', 'status', 'qtype', 'editors', )
    search_fields = ('name', 'keys', 'stem')
    ordering_fields = ('id', 'created', 'modified', 'name',)


class SubtractionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    **Subtraction Viewset**

    """
    queryset = Math.objects.filter(topics__key=domain.DOMAIN_SUBTRACTION)
    serializer_class = MathSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = ('id', 'name', 'status', 'qtype', 'editors', )
    search_fields = ('name', 'keys', 'stem')
    ordering_fields = ('id', 'created', 'modified', 'name',)


class MultiplicationViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    **Multiplication Viewset**

    """
    queryset = Math.objects.filter(topics__key=domain.DOMAIN_MULTIPLICATION)
    serializer_class = MathSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = ('id', 'name', 'status', 'qtype', 'editors', )
    search_fields = ('name', 'keys', 'stem')
    ordering_fields = ('id', 'created', 'modified', 'name',)


class DivisionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    **Division Viewset**

    """
    queryset = Math.objects.filter(topics__key=domain.DOMAIN_DIVISION)
    serializer_class = MathSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = ('id', 'name', 'status', 'qtype', 'editors', )
    search_fields = ('name', 'keys', 'stem')
    ordering_fields = ('id', 'created', 'modified', 'name',)



