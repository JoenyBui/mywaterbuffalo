
from django.db import models
# from django.contrib.postgres.fields import JSONField
#from django_mysql.models.fields.json import JSONField
from jsonfield import JSONField

from problem.models import ProblemBase, QuestionTypeBase
from problem.domain import DOMAIN_READING


class ReadingPassage(models.Model):
    """
    Reading Passage that can be linked to a question.

    """
    text = models.TextField()

    class Meta:
        app_label = 'readings'

    def __init__(self, *args, **kwargs):
        models.Model.__init__(self, *args, **kwargs)


class Reading(ProblemBase, QuestionTypeBase):
    """
    **Reading Problem**

    """
    passage = models.ForeignKey(ReadingPassage, default=None)
    stem = JSONField()
    keys = JSONField()

    class Meta:
        app_label = 'readings'

    def __init__(self, *args, **kwargs):
        ProblemBase.__init__(self, *args, **kwargs)
        QuestionTypeBase.__init__(self, *args, **kwargs)

        self.domain = DOMAIN_READING

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
        When saving the math model, we need to generate the unique instances of the model
        that are references by the text.

        :param force_insert:
        :param force_update:
        :param using:
        :param update_fields:
        :return:
        """

        ProblemBase.save(self, force_insert=force_insert, force_update=force_update, using=using,
                         update_fields=update_fields)
        QuestionTypeBase.save(self, force_insert=force_insert, force_update=force_update, using=using,
                              update_fields=update_fields)

        if self.status == self.CREATED:
            pass
        elif self.status == self.DRAFT:
            pass
        elif self.status == self.SUBMITTED:
            pass
        elif self.status == self.REVIEWED:
            pass
        elif self.status == self.PUBLISHED:
            self.submit_problem()
        elif self.status == self.REVISED:
            pass
        elif self.status == self.LOCK:
            pass

    def submit_problem(self):
        pass

    def check_answer(self, answer, *args, **kwargs):
        pass
