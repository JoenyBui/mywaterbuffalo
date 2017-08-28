from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters

from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import ProblemBase, ProblemInstance
from .models import AnswerInstance, AnswerTrueOrFalse, AnswerMultipleChoice, AnswerFillInTheBlank, AnswerShortAnswer

from .serializers import ProblemBaseSerializer, ProblemInstanceSerializer
from .serializers import AnswerInstanceSerializer, AnswerTrueOrFalseSerializer, AnswerMultipleChoiceSerializer, AnswerFillInTheBlankSerializer


__author__ = 'jbui'


class ProblemBaseModelViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Problem Base Model View Set

    """
    queryset = ProblemBase.objects.all()
    serializer_class = ProblemBaseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('id', 'status', 'domain', 'editors', 'topics',)
    search_fields = ('name', )
    ordering_fields = ('id', 'created', 'modified', 'name',)


class ProblemInstanceModelViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Problem Instance Model View Set

    """
    queryset = ProblemInstance.objects.all()
    serializer_class = ProblemInstanceSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('id', 'data', 'root',)
    search_fields = ('data', )
    ordering_fields = ('id', )

    def create(self, request, *args, **kwargs):
        """
        Create model

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if not request.data.get('data') and request.data.get('root'):
            pi = ProblemBase.objects.get(id=request.data['root'])

            # data = pi.get_data()
            #
            # if data:
            #     self.request.data['data'] = data

            self.request.data['data'] = dict(keys={})

        return viewsets.ModelViewSet.create(self, request, *args, **kwargs)

    def perform_create(self, serializer, *args, **kwargs):
        viewsets.ModelViewSet.perform_create(self, serializer=serializer)

        id = serializer.instance.id

        if self.kwargs.get('parent_lookup_examproblems'):
            ep_id = self.kwargs.get('parent_lookup_examproblems')

            from classroom.models import ExamProblems

            obj = ExamProblems.objects.get(id=ep_id)

            obj.problems.add(id)

            obj.save()


class AnswerInstanceModelViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = AnswerInstance.objects.all()
    serializer_class = AnswerInstanceSerializer
    permission_classes = (permissions.IsAuthenticated, )


class AnswerTrueOrFalseModelViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = AnswerTrueOrFalse.objects.all()
    serializer_class = AnswerTrueOrFalseSerializer
    permission_classes = (permissions.IsAuthenticated, )


class AnswerMultipleChoiceModelViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = AnswerMultipleChoice.objects.all()
    serializer_class = AnswerMultipleChoiceSerializer
    permission_classes = (permissions.IsAuthenticated, )


class AnswerFillInTheBlankModelViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = AnswerFillInTheBlank.objects.all()
    serializer_class = AnswerFillInTheBlankSerializer
    permission_classes = (permissions.IsAuthenticated, )
