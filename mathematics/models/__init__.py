import random

from jinja2 import Template

# from django.contrib.postgres.fields import JSONField
from django_mysql.models.fields.json import JSONField

from django.core import serializers

from taggit.managers import TaggableManager

from problem.models import ProblemBase, QuestionTypeBase, ProblemInstance
from problem import domain
from problem import status
from problem import question

# from .fraction import Fraction

list_of_math_topics = [
    'addition',
    'subtraction',
    'multiplication'
    'division',
    'fraction',
]


class Math(ProblemBase, QuestionTypeBase):
    """
    **Math Problem**

    Used the domain key to choose the appropriate proxy model to derive the

    stem
        :statement:
            pass

        :figures:
            An array of optional figure.

        :charts:
            An array of chart figure.

    keys
        :answer:
            pass

        :choices:
            pass

        :variables:
            :name: name of the variable that is defined in the statement
            :value: numerical, array, or text value
            :type: different "type" of variables

                * number
                    all numerical value
                * whole
                    numerical value without decimal
                * decimal
                    specific float numerical value
                * range
                    array using "[..]" to define values
                * whole range
                    array using "[..]" to define whole values
                * decimal range
                    array using "[..]" to define decimal values
                * blank
                    fill-in-the-blank textbox

    topic
        Topic Many-to-Many object

    """
    stem = JSONField()                        # Statement or Question
    keys = JSONField()                        # Attributes, variables, answers and logic
    # validation = JSONField(default={})                  # Add in validation code
    # explanation = JSONField(default={})                 # Explanation of the answer.
    # topic = TaggableManager(verbose_name='Math Topics',
    #                         help_text='A comma separated list of valid topics this question covers')
                                                        # Math Topics

    class Meta:
        app_label = 'mathematics'

    def __init__(self, *args, **kwargs):
        """
        Initialize the model.

        :param args:
        :param kwargs:
        """

        ProblemBase.__init__(self, *args, **kwargs)
        QuestionTypeBase.__init__(self, *args, **kwargs)

        self.domain = domain.DOMAIN_MATH

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
        When saving the math model, we need to generate the unique instances of the model that are references by the text.

        :param force_insert:
        :param force_update:
        :param using:
        :param update_fields:
        :return:
        """

        ProblemBase.save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
        # QuestionTypeBase.save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

        if self.status == status.CREATED:
            pass
        elif self.status == status.DRAFT:
            pass
        elif self.status == status.SUBMITTED:
            pass
        elif self.status == status.REVIEWED:
            pass
        elif self.status == status.PUBLISHED:
            self.submit_problem()
        elif self.status == status.REVISED:
            pass
        elif self.status == status.LOCK:
            pass

    def get_instance(self):
        """
        Return all possible instance of the mathematics models.

        :return:
        """
        data = {}

        count = self.keys.get('count', 1)

        # If count is not specified, than we assume that it's one.
        variables = self.keys.get('variables')

        # Loop through the count and return the value.
        for i in range(0, count):
            data[i] = self.create_problem_instance(variables, i)

        return data

    def submit_problem(self):
        """
        Submit the problem.

        :return:
        """

        count = self.keys.get('count', 1)

        # If count is not specified, than we assume that it's one.
        variables = self.keys.get('variables')

        # Loop through the count and return the value.
        for i in range(0, count):
            obj = self.create_problem_instance(variables, i)

            obj.save()

    def create_problem_instance(self, variables, index):
        """
        Create problem instance.

        :param variables: variable list
        :param index: appropriate index for the range
        :return:
        """
        # obj = ProblemInstance()

        # Loop through all the variables to integrate them.
        keys = {}

        # If we have variables, look into setting it for the project.
        if variables:
            for var in variables:
                type = var.get('type')

                if type == 'whole range' or type == 'decimal range':
                    # Loop through range.
                    keys[var['name']] = var['value'][index]
                else:
                    # No range type.
                    keys[var['name']] = var['value']

        # Create the problem statement.
        keys['stem'] = self.get_equation(keys)
        keys['blank'] = "<input></input>"
        keys['answer'] = self.keys.get('answer')
        keys['choices'] = self.keys.get('choices')

        return keys

    def get_equation(self, keys):
        """
        Get the equation statement.

        :param keys:
        :return:
        """
        template = Template(self.stem['statement'])
        return template.render(keys)

    def get_answer(self, index):
        """
        Get the answer.

        :param index:
        :return:
        """
        answers = self.keys.get('answer')

        if isinstance(answers, list):
            return answers[index]
        else:
            return answers

    def check_answer(self, answer, *args, **kwargs):
        """
        Check the answer.

        :param answer:
        :param args:
        :param kwargs:
            :index: array

        :return:
        """
        index = kwargs.get('index', 0)

        if self.get_answer(index) == answer:
            return True
        else:
            return False
