import random

from jinja2 import Template

from django.db import models

from problem.domain import DOMAIN_FRACTIONS
from problem.models import ProblemInstance

# from problem.models import ProblemBase, QuestionTypeBase
from . import Math

__author__ = ['joenybui']


class Fraction(Math):
    """
    Fraction Question Generator

    """
    class Meta:
        app_label = 'mathematics'
        proxy = True

    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        Math.__init__(self, *args, **kwargs)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
        When saving the fraction model, we need to generate the unique instances of the model
        that are references by the text.

        :param force_insert:
        :param force_update:
        :param using:
        :param update_fields:
        :return:
        """

        self.domain = DOMAIN_FRACTIONS

        Math.save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

        if True:
            count = self.keys.get('count')

            # If count is not specified, than we assume that it's one.
            answer = self.keys.get('answer', None)

            if count is None:
                count = len(answer)

            variables = self.keys.get('variables')

            for i in range(0, count):
                obj = ProblemInstance()

                # Loop through all the variables to integrate them.
                keys = {}
                for var in variables:
                    type = var.get('type')

                    if type == 'whole range' or type == 'decimal range':
                        # Loop through range.
                        keys[var['name']] = var['value'][i]
                    else:
                        # No range type.
                        keys[var['name']] = var['value']


                # Loop through the choices and set.

                data = {}
                data['stem'] = self.get_equation(keys)
                data['answer'] = answer[i]

                obj.data = data
                obj.root = self
                obj.save()

    def get_equation(self, keys):
        """
        Get the equation statement.

        :return:
        """
        template = Template(self.stem['statement'])
        return template.render(keys)

    def get_fill_in_the_blank(self):
        """
        Get the fill in the blank.

        :return:
        """
        answer = self.get_answer()

        return dict(
            qtype=self.qtype,
            statement=self.get_equation(),
            answer=answer,
            choices=None,
            meta=dict(numerator=self.keys.get('numerator'), denominator=self.keys.get('denominator'))
        )

    def get_true_or_false(self):
        """
        Get the True or False setting.

        :return:
        """
        statement = self.get_equation()

        if random.randint(0, 1):
            answer = True
            statement += '=' + eval(statement)
        else:
            answer = False
            statement += '=' + str(1.0/float(eval(statement)))

        return dict(
            qtype=self.qtype,
            statement=self.get_equation(),
            answer=answer,
            choices=[True, False],
            meta=dict(numerator=self.keys.get('numerator'), denominator=self.keys.get('denominator'))
        )

    def get_multiple_choice(self):
        """
        Get the multiple choice version of this problem.

        :return:
        """
        statement = self.get_equation()
        answer = self.get_answer()

        choices, answer = self.get_choices(answer)

        return dict(
            qtype=self.qtype,
            statement=statement,
            answer=answer,
            choices=choices,
            meta=dict(numerator=self.keys.get('numerator'), denominator=self.keys.get('denominator'))
        )

    def get_answer(self):
        """
        Return the answer or evaluate to one.

        :return:
        """
        answer = self.keys.get('answer')

        if answer:
            #TODO: Check in answer is either list or dict.
            return answer
        else:
            return eval(self.get_equation())

    def generate_random_choice(self, answer, **kwargs):
        """
        Generate a random choice.

        :param answer:
        :param kwargs:
        :return:
        """
        diff = random.uniform(kwargs.get('min', -1), kwargs.get('max', 1))

        return answer + diff

    def get_choices(self, answer):
        """
        Grab the number of options.

        :return:
        """
        num_of_choices = self.keys.get('num_of_choices', 4)
        choices = self.keys.get('choices', [])

        while len(choices) < num_of_choices - 1:
            rtr = self.generate_random_choice(answer)

            if rtr not in choices:
                choices.append(rtr)

        for i, choice in enumerate(choices):
            choices[i] = round(choice, 3)

        # Shuffle the list and choose (num_of_choices - 1)
        random.shuffle(choices)
        choices = choices[:num_of_choices-1]

        # Shuffle again with the answer in the list,
        choices.append(answer)
        random.shuffle(choices)

        return choices, choices.index(answer)
