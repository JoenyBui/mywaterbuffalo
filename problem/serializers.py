from collections import OrderedDict

# from urllib.parse import urljoin
from urlparse import urljoin

from rest_framework import serializers
from rest_framework.reverse import reverse

from editor.models import Editor
from classroom.models import ExamProblems

from .models import ProblemBase, ProblemInstance
from .models import AnswerInstance, AnswerTrueOrFalse, AnswerMultipleChoice, AnswerFillInTheBlank

from problem import domain
from problem import status
from problem import question


class ProblemBaseSerializer(serializers.ModelSerializer):
    """
    Problem Base Serializer

    """
    links = serializers.SerializerMethodField(method_name='get_links_url', label='links')
    info = serializers.SerializerMethodField(method_name='get_info_data', label='info')

    class Meta:
        model = ProblemBase
        fields = ('id', 'name', 'editors', 'status', 'domain', 'topics', 'created', 'modified', 'links', 'info')

    def get_info_data(self, obj, *args, **kwargs):
        """
        Get Information Data

        :param obj:
        :param args:
        :param kwargs:
        :return:
        """
        info = OrderedDict({})

        # Add Editors links
        try:
            info_editors = OrderedDict({})

            for instance in obj.editors.all():
                info_editors[instance.pk] = instance.pen_name

            info['editors'] = info_editors
        except Editor.DoesNotExist as e:
            info['editors'] = str(e)

        # Domain
        try:
            info['domain'] = domain.DOMAIN_DICT[obj.domain]
        except Exception as e:
            info['domain'] = str(e)

        # Status
        try:
            info['status'] = status.STATUS_CHOICES[obj.status][1]
        except Exception as e:
            info['status'] = str(e)

        return info

    def get_links_url(self, obj, *args, **kwargs):
        """
        Get links url

        :param obj:
        :param args:
        :param kwargs:
        :return:
        """
        links = {}

        # Add Editors links
        try:
            links_editors = OrderedDict({})

            for instance in obj.editors.all():
                links_editors[instance.pk] = urljoin(reverse('v1:editor:editors-list', request=self.context['request']),
                                                     str(instance.pk))

            links['editors'] = links_editors
        except Editor.DoesNotExist as e:
            links['editors'] = str(e)

        # Add Problem-Instance links
        try:
            if obj.probleminstance_set:

                links_probleminstance = OrderedDict({})

                for instance in obj.probleminstance_set.all():
                    links_probleminstance[instance.pk] = urljoin(reverse('v1:problem:problem-instance-list', request=self.context['request']), str(instance.pk))

                links['problem-instance'] = links_probleminstance
        except ProblemInstance.DoesNotExist as e:
            links['problem-instance'] = str(e)

        # Add Math
        try:
            if obj.math:
                links['child'] = urljoin(
                    reverse('v1:math:math-list', request=self.context['request']), str(obj.pk)
                )

        except Exception as e:
            links['child'] = None

        return links


class ProblemInstanceSerializer(serializers.ModelSerializer):
    """
    Problem Instance Serializer

    """
    links = serializers.SerializerMethodField(method_name='get_links_url', label='links')
    info = serializers.SerializerMethodField(method_name='get_info_data', label='info')

    class Meta:
        model = ProblemInstance
        fields = ('id', 'data', 'root', 'info', 'links')

    def create(self, validated_data):
        """
        Serialize a new problem instance model.

        :param validated_data:
        :return:
        """

        return serializers.ModelSerializer.create(self, validated_data)

    def get_info_data(self, obj, *args, **kwargs):
        """
        Get information data.

        :param obj:
        :param args:
        :param kwargs:
        :return:
        """
        info = {}

        problem = obj.root

        info['base'] = problem.get_data()
        info['data'] = None
        info['name'] = problem.name
        info['count'] = problem.get_count()

        if problem.math:
            info['qtype'] = problem.math.qtype
        else:
            info['qtype'] = None

        return info

    def get_links_url(self, obj, *args, **kwargs):
        """
        Get links url.

        :param obj:
        :param args:
        :param kwargs:
        :return:
        """
        link = OrderedDict({})

        try:
            if obj.root:
                link['root'] = urljoin(
                    reverse('v1:problem:problem-base-list', request=self.context['request']), str(obj.root.pk)
                )

        except ProblemBase.DoesNotExist as e:
            link['root'] = str(e)

        # Add Math
        try:
            if obj.root.math:
                link['child'] = urljoin(
                    reverse('v1:math:math-list', request=self.context['request']), str(obj.root.math.pk)
                )

        except Exception as e:
            link['child'] = None

        try:
            if obj.examproblems_set:
                link_exam = OrderedDict({})

                for instance in obj.examproblems_set.all():
                    link_exam[instance.pk] = urljoin(reverse('v1:classroom:exam-problems-list',
                                                                    request=self.context['request']),
                                                            str(instance.pk))

                link['exam-problem'] = link_exam

        except ExamProblems.DoesNotExist as e:
            link['exam-problem'] = str(e)

        return link


class AnswerInstanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerInstance


class AnswerTrueOrFalseSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerTrueOrFalse


class AnswerMultipleChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerMultipleChoice


class AnswerFillInTheBlankSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerFillInTheBlank

