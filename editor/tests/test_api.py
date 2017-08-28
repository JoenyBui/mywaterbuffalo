import os

from django.test import TestCase
from django.contrib.auth.models import User


from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as rf_reverse

from editor.models import Editor

from core.tests import _BaseSetting


class EditorApiTests(APITestCase, _BaseSetting):
    """
    Test Editor API

    """

    def setUp(self):
        _BaseSetting.setUp(self)

    def test_list(self):
        url = rf_reverse('v1:editor:editors-list')
        self.client.login(username='trump', password='CrookedHillary')
        response = self.client.get(url, format='json')
        print(response.status_text)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_url(self):
        url = rf_reverse('v1:editor:editors-list')
        self.client.login(username='clinton', password='monicaMyGal')

        response = self.client.post(url, data=dict(user=4, pen_name='Kal-El',), secure=True, format='json')
        print(response.status_text)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_no_user_pk(self):
        url = rf_reverse('v1:editor:editors-list')
        self.client.login(username='clinton', password='monicaMyGal')

        response = self.client.post(url, data=dict(pen_name='Big L',), secure=True, format='json')
        print(response.status_text)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_power(self):
        url = rf_reverse('v1:editor:power-sensei-list')
        self.client.force_login(self.u1)

        response = self.client.post(url, data=dict(), secure=True, format='json')
        print(response.status_text)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
