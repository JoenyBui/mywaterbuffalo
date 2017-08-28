import os

from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from .models import ProblemInstance
from editor.models import Editor
from mathematics.models.fraction import Fraction

from core.tests import _BaseSetting

# Create your tests here.


class ProblemApiTests(APITestCase, _BaseSetting):

    def setUp(self):
        _BaseSetting.setUp(self)

        self.pt = Fraction(name="Fill-in-the-Blank")
        self.pt.set_fill_in_the_blank()
        self.pt.stem={
            "statement": "Express the following fractions in simplest form: {{numerator}}/{{denominator}}"
        }

        self.pt.keys = {
            "variables": [
                dict(name="numerator", value=[4, 3, 12, 8], type='whole range'),
                dict(name="denominator", value=[16, 6, 18, 15], type='whole range')
            ],
            "answer": ["1/4", "1/2", "2/3", "8/15"]
        }

        self.pt.save()

        self.pt.editors.add(self.e1)

        self.pt.save()

    def test_create_url(self):
        url = reverse('v1:problem:problem-instance-list')

        self.client.login(username='superman', password='ClarkKent1938')

        response = self.client.post(url, data=dict(root=1), format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
