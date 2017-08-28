from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters

from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Editor
from .models import PowerSensei, PowerPupil, PowerGuardian, PowerTopicExpert

from .serializers import UserSerializer, EditorSerializer
from .serializers import PowerSenseiSerializer, PowerPupilSerializer, PowerGuardianSerializer, PowerTopicExpertsSerializer


__author__ = 'jbui'


class UserModelViewSets(NestedViewSetMixin, viewsets.ModelViewSet):
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('id', 'last_name', )
    search_fields = ('first_name', 'last_name', )
    ordering_fields = ('id', 'first_name', 'last_name',)

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)


class EditorModelViewSets(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Editor.objects.all()
    serializer_class = EditorSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('id', 'pen_name', )
    search_fields = ('pen_name', )
    ordering_fields = ('id', 'pen_name',)


    # def get_queryset(self):
    #     return Editor.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        if not request.data.get('user'):
            request.data['user'] = request.user.pk

        return viewsets.ModelViewSet.create(self, request, *args, **kwargs)


class PowerSenseiViewSets(NestedViewSetMixin, viewsets.ModelViewSet):
    # queryset = PowerSensei.objects.all()
    serializer_class = PowerSenseiSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        editor = user.editor
        return PowerSensei.objects.filter(editor=editor)

    def create(self, request, *args, **kwargs):
        """
        Assign superpower to user.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if not request.data.get('user'):
            request.data['editor'] = Editor.get_editor_id(self.request.user)

        return viewsets.ModelViewSet.create(self, request, *args, **kwargs)


class PowerPupilViewSets(NestedViewSetMixin, viewsets.ModelViewSet):
    # queryset = PowerPupil.objects.all()
    serializer_class = PowerPupilSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        editor = user.editor
        return PowerPupil.objects.filter(editor=editor)

    def create(self, request, *args, **kwargs):
        """
        Assign pupil superpower to user.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if not request.data.get('user'):
            request.data['editor'] = Editor.get_editor_id(self.request.user)

        return viewsets.ModelViewSet.create(self, request, *args, **kwargs)


class PowerGuardianViewSets(NestedViewSetMixin, viewsets.ModelViewSet):
    # queryset = PowerGuardian.objects.all()
    serializer_class = PowerGuardianSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        editor = user.editor
        return PowerGuardian.objects.filter(editor=editor)

    def create(self, request, *args, **kwargs):
        """
        Assign SuperPower to user.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if not request.data.get('user'):
            request.data['editor'] = Editor.get_editor_id(self.request.user)

        return viewsets.ModelViewSet.create(self, request, *args, **kwargs)


class PowerTopicExpertViewSets(NestedViewSetMixin, viewsets.ModelViewSet):
    # queryset = PowerTopicExpert.objects.all()
    serializer_class = PowerTopicExpertsSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        editor = user.editor
        return PowerTopicExpert.objects.filter(editor=editor)

    def create(self, request, *args, **kwargs):
        """
        Assign SuperPower to user.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if not request.data.get('user'):
            request.data['editor'] = Editor.get_editor_id(self.request.user)

        return viewsets.ModelViewSet.create(self, request, *args, **kwargs)
