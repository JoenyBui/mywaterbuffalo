import os

from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as rf_reverse
from rest_framework.test import APIRequestFactory

from editor.models import Editor
from ..models import Math

from core.tests import _BaseSetting

from problem import status
from problem import question
from problem import domain

factory = APIRequestFactory()


class FractionTestCase(TestCase, _BaseSetting):
    def setUp(self):
        _BaseSetting.setUp(self)

    def test_fill_in_the_blank(self):
        f1 = Math(name="fill in the blank")
        f1.qtype = question.FILL_IN_THE_BLANK
        f1.stem = dict(statement="{{ numerator }}/{{ denominator }}", )
        f1.keys = dict(
            count=4,
            variables=[
                {"name": "numerator", "value": [4, 3, 12, 8], "type": "whole range"},
                {"name": "denominator", "value": [16, 6, 18, 15], "type": "whole range"}
            ],
            answer=["1/4", "1/2", "2/3", "8/15"],
            choices=["2/3", "3/5", "8/9", "10/13", "14/11", "8/9"]
        )
        f1.validation = dict(expression="")
        f1.explanation = dict(explanation="")

        f1.save()
        f1.editors.add(self.e1)
        f1.save()

        data = f1.get_instance()

        self.assertEqual(len(data), 4)

    def test_true_or_false(self):

        f2 = Math(name="true_or_false")
        f2.qtype = question.TRUE_OF_FALSE
        f2.stem = dict(statement="{{ numerator }}/{{ denominator }}",)
        f2.keys = dict(
            count=1,
            variables=[
                dict(name='numerator', value=1, type='whole'),
                dict(name='denominator', value=4, type='whole')
            ],
            answer=[0.25]
        )

        f2.save()
        f2.editors.add(self.e1)
        f2.save()

        data = f2.get_instance()

        self.assertEqual(len(data), 1)

    def test_simple_multiple_choice(self):

        f3 = Math(name="multiple choice")
        f3.qtype = question.MULTIPLE_CHOICE
        f3.stem = dict(statement="{{ numerator }}/{{ denominator }}",)
        f3.keys = dict(
            count=1,
            variables=[
                dict(name='numerator', value=8, type='whole'),
                dict(name='denominator', value=8, type='whole')
            ],
            choices=[1.0/4.0, 1.0/2.0, 3.0/4.0, 6.0/4.0],
            answer=[1.0]
        )

        f3.save()
        f3.editors.add(self.e1)
        f3.save()

        data = f3.get_instance()

        self.assertEqual(len(data), 1)


class FractionViewsTestCase(TestCase, _BaseSetting):
    def test_index(self):
        resp = self.client.get('/v1/math/fractions')
        self.assertEqual(resp.status_code, 301)
        resp = self.client.get('/v1/math/fractions/')
        self.assertEqual(resp.status_code, 200)


class FractionApiTests(APITestCase, _BaseSetting):
    def setUp(self):
        _BaseSetting.__init__(self)

    def test_list(self):
        url = rf_reverse('v1:math:fractions-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        url = rf_reverse('v1:math:fractions-list')

        data = {
            "name": "Fill-in-the-Blank Multiplication Fraction",
            "qtype": 0,
            "stem": {"statement": "{{numerator1}}/{{denominator1}} * {{numerator2}}/{{denominator2}}"},
            "keys": {
                "numerator1": [8, 4],
                "denominator1": [5, 5],
                "numerator2": [9, 2],
                "denominator2": [6, 10],
                "answer": ["72/30", "4/50"]
            },
            "editors": [
                1
            ]
        }

        self.client.force_login(user=self.u1)

        response = self.client.post(url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(url, format='json')
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

