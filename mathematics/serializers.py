import os
#from urllib.parse import urljoin
from urlparse import urljoin

from collections import OrderedDict

from rest_framework import serializers
from rest_framework.reverse import reverse

from problem.status import STATUS_DICT
from problem.domain import DOMAIN_DICT
from problem.question import QUESTION_DICT
from problem.models import ProblemInstance

from topic.models import Topic

from .models import Math
from .models.fraction import Fraction
from .models.addition import Addition
from .models.subtraction import Subtraction
from .models.multiplication import Multiplication
from .models.division import Division

__author__ = 'jbui'


class MathSerializer(serializers.ModelSerializer):
    """
    **Math Serializer**

    """
    links = serializers.SerializerMethodField(method_name='get_links_url', label='links')
    info = serializers.SerializerMethodField(method_name='get_info_data', label='info')

    class Meta:
        model = Math
        fields = ('id', 'name', 'editors', 'status', 'domain', 'topics', 'created', 'modified', 'stem', 'keys', 'qtype', 'links', 'info')

    def get_info_data(self, obj, *args, **kwargs):
        """
        Get information data

        :param obj:
        :param args:
        :param kwargs:
        :return:
        """
        info = OrderedDict({})

        try:
            if obj.status is not None:
                info['status'] = STATUS_DICT[obj.status]

        except Exception as e:
            info['status'] = str(e)

        try:
            if obj.domain is not None:
                info['domain'] = DOMAIN_DICT[obj.domain]
        except Exception as e:
            info['domain'] = str(e)

        try:
            if obj.qtype is not None:
                info['qtype'] = QUESTION_DICT[obj.qtype]
        except Exception as e:
            info['qtype'] = str(e)

        try:
            info_editors = OrderedDict({})
            for index, value in enumerate(obj.editors.all()):
                info_editors[value.pk] = value.pen_name

            info['editors'] = info_editors
        except Math.DoesNotExist as e:
            info['editors'] = str(e)

        try:
            info_topics = OrderedDict({})
            for index, value in enumerate(obj.topics.all()):
                info_topics[value.pk] = value.name

            info['topics'] = info_topics
        except Math.DoesNotExist as e:
            info['topics'] = str(e)

        return info

    def get_links_url(self, obj, *args, **kwargs):
        """
        Get links url

        :param obj:
        :param args:
        :param kwargs:
        :return:
        """
        links = OrderedDict({})

        try:
            link_editors = OrderedDict({})
            for index, value in enumerate(obj.editors.all()):
                link_editors[value.pk] = urljoin(reverse('v1:editor:editors-list', request=self.context['request']), str(value.pk))

            links['editors'] = link_editors
        except Math.DoesNotExist as e:
            links['editors'] = str(e)

        try:
            if obj.probleminstance_set:
                link_probleminstance = OrderedDict({})

                for instance in obj.probleminstance_set.all():
                    link_probleminstance[instance.pk] = urljoin(reverse('v1:problem:problem-instance-list',
                                                                    request=self.context['request']),
                                                            str(instance.pk))

                links['problem-instance'] = link_probleminstance

        except ProblemInstance.DoesNotExist as e:
            links['problem-instance'] = str(e)

        try:
            link_topics = OrderedDict({})
            for index, value in enumerate(obj.topics.all()):
                link_topics[value.pk] = urljoin(reverse('v1:topic:topic-list', request=self.context['request']), str(value.pk))

            links['topics'] = link_topics
        except Topic.DoesNotExist as e:
            links['topics'] = str(e)

        return links


class FractionSerializer(serializers.ModelSerializer):
    """
    **Fraction Serializer**

    """
    class Meta:
        model = Fraction


class AdditionSerializer(serializers.ModelSerializer):
    """
    **Addition Serializer**

    """
    class Meta:
        model = Addition


class SubtractionSerializer(serializers.ModelSerializer):
    """
    **Subtraction Serializer**

    """
    class Meta:
        model = Subtraction


class MultiplicationSerializer(serializers.ModelSerializer):
    """
    **Multiplication Serializer**

    """
    class Meta:
        model = Multiplication


class DivisionSerializer(serializers.ModelSerializer):
    """
    **Division Serializer**

    """
    class Meta:
        model = Division

