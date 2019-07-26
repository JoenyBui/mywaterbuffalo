from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Sensei, Pupil, ExamProblems, ExamAnswers, Assignment, Class, ClassAssignment

from .serializers import SenseiSerializer, PupilSerializers, ExamProblemsSerializers, ExamAnswersSerializers, \
    AssignmentSerializer, ClassSerializer, ClassAssignmentSerializer


__author__ = 'jbui'


class SenseiModelViewSets(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    **Sensei Viewset**

    """
    queryset = Sensei.objects.all()
    serializer_class = SenseiSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class PupilModelViewSets(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    **Pupil Viewset**

    """
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializers
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class ExamProblemsModelViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    **Exam Problem Viewset**

    """
    queryset = ExamProblems.objects.all()
    serializer_class = ExamProblemsSerializers
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    def create(self, request, *args, **kwargs):
        if request.data['teacher'] is None:
            request.data['teacher'] = self.request.user.sensei.pk

        return viewsets.ModelViewSet.create(self, request, *args, **kwargs)


class ExamAnswerModelViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    **Exam Answer Viewset**

    """
    queryset = ExamAnswers.objects.all()
    serializer_class = ExamAnswersSerializers
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class AssignmentModelViewSet(NestedViewSetMixin, viewsets.ModelViewSet):

    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class ClassModelViewSet(NestedViewSetMixin, viewsets.ModelViewSet):

    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class ClassAssignmentsModelViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = ClassAssignment.objects.all()
    serializer_class = ClassAssignmentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

