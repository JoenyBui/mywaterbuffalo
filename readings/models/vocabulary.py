import random

from jinja2 import Template

from django.db import models

from problem.domain import DOMAIN_VOCABULARY

from . import Reading


__author__ = ['joenybui']


class Vocabulary(Reading):
    """
    Vocabulary Problem Type
    """

    class Meta:
        app_label = 'readings'

    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        Reading.__init__(self, *args, **kwargs)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """

        :param force_insert:
        :param force_update:
        :param using:
        :param update_fields:
        :return:
        """

        self.domain = DOMAIN_VOCABULARY

        Reading.save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
