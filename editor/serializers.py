import os
from collections import OrderedDict

from urllib.parse import urljoin

from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.reverse import reverse


from classroom.models import Sensei, Pupil
from problem.models import ProblemBase
from .models import Editor
from .models import PowerSensei, PowerPupil, PowerGuardian, PowerTopicExpert

__author__ = 'jbui'


class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer

    """
    links = serializers.SerializerMethodField(method_name='get_links_url', label='links')

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'links')

    def get_links_url(self, obj, *args, **kwargs):
        """
        Get the editor link urls.

        :param obj: User object
        :param args:
        :param kwargs:
        :return:
        """
        link_dict = OrderedDict({})

        try:
            if obj.editor:
                link_dict['editor'] = urljoin(reverse('v1:editor:editors-list', request=self.context['request']), str(obj.editor.pk))
        except Editor.DoesNotExist as e:
            link_dict['editor'] = str(e)

        try:
            if obj.sensei:
                link_dict['sensei'] = urljoin(reverse('v1:classroom:sensei-list', request=self.context['request']), str(obj.sensei.pk))
        except Sensei.DoesNotExist as e:
            link_dict['sensei'] = str(e)

        try:
            if obj.pupil:
                link_dict['pupil'] = urljoin(reverse('v1:classroom:pupil-list', request=self.context['request']), str(obj.pupil.pk))
        except Pupil.DoesNotExist as e:
            link_dict['pupil'] = str(e)

        return link_dict


class EditorSerializer(serializers.ModelSerializer):
    """
    Editor Serializer

    """
    links = serializers.SerializerMethodField(method_name='get_links_url', label='links')

    class Meta:
        model = Editor
        fields = ('id', 'pen_name', 'user', 'links')

    def get_links_url(self, obj, *args, **kwargs):
        """
        Get links url obj model.

        :param obj:
        :param args:
        :param kwargs:
        :return:
        """
        links = OrderedDict({})

        try:
            if obj.user:
                links['user'] = urljoin(reverse('v1:editor:users-list', request=self.context['request']), str(obj.user.pk))
        except User.DoesNotExist as e:
            links['user'] = str(e)

        try:
            if obj.problembase_set:
                link_problembase = OrderedDict({})

                for value in obj.problembase_set.all():
                    link_problembase[value.pk] = urljoin(reverse('v1:problem:problem-base-list',
                                                                 request=self.context['request']),
                                                         str(value.pk))

                links['problem-base'] = link_problembase

        except ProblemBase.DoesNotExist as e:
            links['problem-base'] = str(e)

        return links

    def create(self, validated_data):
        return serializers.ModelSerializer.create(self, validated_data=validated_data)


class PowerSenseiSerializer(serializers.ModelSerializer):
    # editor = serializers.HyperlinkedRelatedField(
    #     read_only=False,
    #     view_name='editors-detail',
    #     queryset=Editor.objects.all()
    # )

    class Meta:
        model = PowerSensei
        fields = ('id', 'strength', 'assigned', 'validated', 'editor')


class PowerPupilSerializer(serializers.ModelSerializer):

    class Meta:
        model = PowerPupil


class PowerGuardianSerializer(serializers.ModelSerializer):

    class Meta:
        model = PowerGuardian


class PowerTopicExpertsSerializer(serializers.ModelSerializer):

     class Meta:
         model = PowerTopicExpert

