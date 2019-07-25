from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Reading
from .models.vocabulary import Vocabulary
from .models.spelling import Spelling

from problem import domain

from .serializers import ReadingSerializer


__author__ = ['jbui']


class ReadingViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    ** Reading ViewSet***

    """
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('id', 'status', 'domain', 'qtype', 'editors', 'topics')
    search_fields = ('name', 'keys', 'stem')
    ordering_fields = ('id', 'created', 'modified', 'name',)


class SpellingViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    **Spelling Viewset***

    """
    queryset = Spelling.objects.filter(domain=domain.DOMAIN_SPELLING)
    serializer_class = ReadingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('id', 'status', 'domain', 'qtype', 'editors', 'topics')
    search_fields = ('name', 'keys', 'stem')
    ordering_fields = ('id', 'created', 'modified', 'name',)


class VocabularyViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    **Vocabulary Viewset***

    """
    queryset = Vocabulary.objects.filter(domain=domain.DOMAIN_VOCABULARY)
    serializer_class = ReadingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('id', 'status', 'domain', 'qtype', 'editors', 'topics')
    search_fields = ('name', 'keys', 'stem')
    ordering_fields = ('id', 'created', 'modified', 'name',)
