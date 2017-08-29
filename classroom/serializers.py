import os
from collections import OrderedDict

# from urllib.parse import urljoin
from urlparse import urljoin

from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Sensei, Pupil, ExamProblems, ExamAnswers, ProblemInstance, Assignment, Class, ClassAssignment


__author__ = 'jbui'


class SenseiSerializer(serializers.ModelSerializer):
    """
    Serialize Sensei Model

    """
    links = serializers.SerializerMethodField(method_name='get_links_url', label='links')
    info = serializers.SerializerMethodField(method_name='get_info_data', label='info')

    class Meta:
        model = Sensei
        fields = ('id', 'pen_name', 'user', 'links', 'info')

    def get_info_data(self, obj, *args, **kwargs):
        """
        Get the sensei information url.

        :param obj:
        :param args:
        :param kwargs:
        :return:
        """
        info = OrderedDict({})

        try:
            info['user'] = str(obj.user)
        except User.DoesNotExist as e:
            info['user'] = str(e)

        return info

    def get_links_url(self, obj, *args, **kwargs):
        user_url = urljoin(reverse('v1:editor:users-list', request=self.context['request']), str(obj.user.pk))

        return dict(user=user_url)


class PupilSerializers(serializers.ModelSerializer):
    """
    Serialize Pupil Model

    """
    links = serializers.SerializerMethodField(method_name='get_links_url', label='links')
    info = serializers.SerializerMethodField(method_name='get_info_data', label='info')

    class Meta:
        model = Pupil
        fields = ('id', 'pen_name', 'user', 'links', 'info')

    def get_info_data(self, obj, *args, **kwargs):
        """
        Get the pupil information url.

        :param obj:
        :param args:
        :param kwargs:
        :return:
        """
        info = OrderedDict({})

        try:
            info['user'] = str(obj.user)
        except User.DoesNotExist as e:
            info['user'] = str(e)

        return info

    def get_links_url(self, obj, *args, **kwargs):
        user_url = urljoin(reverse('v1:editor:users-list', request=self.context['request']), str(obj.user.pk))

        return dict(user=user_url)


class ExamProblemsSerializers(serializers.ModelSerializer):
    """
    Serialize the Exam Problem with link and info.

    """
    links = serializers.SerializerMethodField(method_name='get_links_url', label='links')
    info = serializers.SerializerMethodField(method_name='get_info_data', label='info')

    class Meta:
        model = ExamProblems
        fields = ('id', 'name', 'teacher', 'problems', 'info', 'links')

    def get_info_data(self, obj, *args, **kwargs):
        """
        Get information data.

        :param obj:
        :param args:
        :param kwargs:
        :return:
        """
        info = {}

        try:
            if obj.teacher:
                info['teacher'] = obj.teacher.pen_name
        except Sensei.DoesNotExist as e:
            info['teacher'] = str(e)

        try:
            info_problems = OrderedDict({})

            for index, value in enumerate(obj.problems.all()):
                info_problems[value.pk] = value.get_data()

            info['problems'] = info_problems

        except ProblemInstance.DoesNotExist as e:
            info['problems'] = str(e)

        return info

    def get_links_url(self, obj, *args, **kwargs):
        """
        Get link url

        :param obj:
        :param args:
        :param kwargs:
        :return:
        """
        link = OrderedDict({})

        try:
            if obj.teacher:
                link['teacher'] = urljoin(reverse('v1:classroom:sensei-list', request=self.context['request']), str(obj.teacher.pk))
        except Sensei.DoesNotExist as e:
            link['teacher'] = str(e)

        try:
            link_problems = OrderedDict({})
            for index, value in enumerate(obj.problems.all()):
                link_problems[value.pk] = urljoin(reverse('v1:problem:problem-instance-list', request=self.context['request']), str(value.pk))

            link['problems'] = link_problems
        except ProblemInstance.DoesNotExist as e:
            link['problems'] = str(e)

        return link


class ExamAnswersSerializers(serializers.ModelSerializer):
    """
    Serialize the Exam Answer Key with links and info

    """

    links = serializers.SerializerMethodField(method_name='get_links_url', label='links')
    info = serializers.SerializerMethodField(method_name='get_info_data', label='info')
    grade = serializers.ReadOnlyField()
    created = serializers.ReadOnlyField()
    modified = serializers.ReadOnlyField()
    results = serializers.ReadOnlyField()

    class Meta:
        model = ExamAnswers
        fields = ('id', 'created', 'modified', 'exam', 'student', 'answers', 'results', 'grade', 'info', 'links')

    def get_info_data(self, obj, *args, **kwargs):
        """
        Get Information data

        :param obj:
        :param args:
        :param kwargs:
        :return:
        """
        info = OrderedDict({})

        try:
            if obj.student:
                info['student'] = obj.student.pen_name
        except Pupil.DoesNotExist as e:
            info['student'] = str(e)

        try:
            if obj.exam:
                info['exam'] = obj.exam.name

        except Pupil.DoesNotExist as e:
            info['exam'] = str(e)

        try:
            info_problems = OrderedDict({})

            for index, value in enumerate(obj.exam.problems.all()):
                info_problems[value.pk] = value.get_data()

            info['problems'] = info_problems

        except ProblemInstance.DoesNotExist as e:
            info['problems'] = str(e)

        return info

    def get_links_url(self, obj, *args, **kwargs):
        """
        Get links url

        :param obj:
        :param args:
        :param kwargs:
        :return:
        """
        link = OrderedDict({})

        try:
            if obj.student:
                link['student'] = urljoin(reverse('v1:classroom:pupil-list', request=self.context['request']),
                                          str(obj.student.pk))
        except Pupil.DoesNotExist as e:
            link['student'] = str(e)

        try:
            if obj.exam:
                link['exam'] = urljoin(reverse('v1:classroom:exam-problems-list', request=self.context['request']),
                                          str(obj.exam.pk))
        except Pupil.DoesNotExist as e:
            link['exam'] = str(e)

        return link


class AssignmentSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    modified = serializers.ReadOnlyField()

    class Meta:
        model = Assignment
        fields = ('id', 'created', 'modified', 'student', 'exam', 'answers', 'grade')


class ClassSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    modified = serializers.ReadOnlyField()

    class Meta:
        model = Class
        fields = ('id', 'created', 'modified', 'teacher', 'students', 'name')


class ClassAssignmentSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    modified = serializers.ReadOnlyField()

    class Meta:
        model = ClassAssignment
        fields = ('id', 'created', 'modified', 'classroom', 'exam', 'assignments')
