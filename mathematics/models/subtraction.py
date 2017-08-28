from problem.domain import DOMAIN_SUBTRACTION

from . import Math


class Subtraction(Math):

    class Meta:
        app_label = 'mathematics'
        proxy = True

    def __init__(self, *args, **kwargs):
        """
        Constructor.

        :param args:
        :param kwargs:
        """
        Math.__init__(self, *args, **kwargs)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
        Save object model.

        :param force_insert:
        :param force_update:
        :param using:
        :param update_fields:
        :return:
        """

        self.domain = DOMAIN_SUBTRACTION

        Math.save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
