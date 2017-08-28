import os

from django.test import TestCase
from django.contrib.auth.models import User


from editor.models import Editor

from core.tests import _BaseSetting


class TestEditor(TestCase, _BaseSetting):

    def setUp(self):
        _BaseSetting.setUp(self)

    def test_is_editor(self):
        self.assertTrue(Editor.objects.get(pk=1))
