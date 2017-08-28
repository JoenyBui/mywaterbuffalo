"""
Core Test Base Setting

"""
import os

from django.contrib.auth.models import User

from editor.models import Editor
from classroom.models import Sensei, Pupil, ExamProblems, ExamAnswers
from problem.models import ProblemBase, QuestionTypeBase, ProblemInstance
from problem import question
from problem import status
from problem import domain

from mathematics.models import Math
from readings.models import Reading


class _BaseSetting(object):

    def setUp(self, **kwargs):
        self.setUpUser()
        self.setUpEditor()
        self.setUpSensei()
        self.setUpPupil()
        self.setUpMath()
        self.setUpExam()

    def setUpUser(self):
        self.u1 = User.objects.create_user(username='superman', password='ClarkKent1938')
        self.u2 = User.objects.create_user(username='lex', password='LutherCorp')
        self.u3 = User.objects.create_user(username='trump', password='CrookedHillary')
        self.u4 = User.objects.create_user(username='clinton', password='monicaMyGal')
        self.u5 = User.objects.create_user(username='pence', password='JesusFreak')
        self.u6 = User.objects.create_user(username='kaine', password='Jesuit2016')

    def setUpEditor(self):
        self.e1 = Editor.objects.create(pen_name='S', user=self.u1)
        self.e2 = Editor.objects.create(pen_name='Lana', user=self.u2)

    def setUpSensei(self):
        self.t3 = Sensei.objects.create(user=self.u3, pen_name='Donald Trump')
        self.t4 = Sensei.objects.create(user=self.u4, pen_name='Hillary Clinton')

    def setUpPupil(self):
        self.s4 = Pupil.objects.create(user=self.u4, pen_name='Hillary')
        self.s5 = Pupil.objects.create(user=self.u5, pen_name='Mike')
        self.s6 = Pupil.objects.create(user=self.u6, pen_name='Tim')

    def setUpMath(self):

        self.create_math_problem(name='P1',
                                 qtype=question.FILL_IN_THE_BLANK,
                                 stem=dict(statement="{{left}} + {{right}} = {{blank}}"),
                                 keys=dict(
                                     variables=[dict(name='left', value=5, type='whole'),
                                                dict(name='right', value=5, type='whole')],
                                     answer=[10]),
                                 status=status.PUBLISHED)

        self.create_math_problem(name='P2',
                                 editor=self.e1,
                                 qtype=question.FILL_IN_THE_BLANK,
                                 stem=dict(statement="{{left}} + {{right}} = {{blank}}"),
                                 keys=dict(
                                     variables=[dict(name='left', value=1, type='whole'),
                                                dict(name='right', value=5, type='whole')],
                                     answer=[6]),
                                 status=status.PUBLISHED)

        self.create_math_problem(name='P3',
                                 editor=self.e1, qtype=question.FILL_IN_THE_BLANK,
                                 stem=dict(statement="{{left}} + {{right}} = {{blank}}"),
                                 keys=dict(
                                     variables=[
                                         dict(name='left', value=9, type='whole'),
                                         dict(name='right', value=2, type='whole')
                                     ],
                                     answer=[11]
                                 ),
                                 status=status.PUBLISHED)

        self.create_math_problem(name='P4',
                                 editor=self.e1,
                                 qtype=question.FILL_IN_THE_BLANK,
                                 stem=dict(statement="{{left}} + {{right}} = {{blank}}"),
                                 keys=dict(
                                     variables=[
                                         dict(name='left', value=1, type='whole'),
                                         dict(name='right', value=1, type='whole')
                                     ],
                                     answer=[2]
                                 ),
                                 status=status.PUBLISHED)

        self.create_math_problem(name='P5',
                                 editor=self.e2,
                                 qtype=question.FILL_IN_THE_BLANK,
                                 stem=dict(statement="{{left}} + {{right}} = {{blank}}"),
                                 keys=dict(
                                     variables=[
                                         dict(name='left', value=5, type='whole'),
                                         dict(name='right', value=5, type='whole')
                                     ],
                                     answer=[10]
                                 ))

        self.create_math_problem(name='P6',
                                 editor=self.e2,
                                 qtype=question.FILL_IN_THE_BLANK,
                                 stem=dict(statement="{{left}} + {{right}} = {{blank}}"),
                                 keys=dict(
                                     variables=[
                                         dict(name='left', value=5, type='whole'),
                                         dict(name='right', value=5, type='whole')
                                     ],
                                     answer=[10]
                                 ))

        self.create_math_problem(name='P7',
                                 editor=self.e1,
                                 qtype=question.FILL_IN_THE_BLANK,
                                 stem=dict(statement="{{left}} + {{right}} = {{blank}}"),
                                 keys=dict(
                                     variables=[
                                         dict(name='left', value=5, type='whole'),
                                         dict(name='right', value=5, type='whole')
                                     ],
                                     answer=[10]
                                 ))

        stem = {
            "statement": "Which fraction is bigger than {{numerator}}/{{denominator}}",
            "figures": [],
            "charts": []
        }

        keys = {
            "answer": "3/4",
            "choices": ["2/5", "4/7", "2/4", "3/4"],
            "variables": [
                {"name": "numerator", "value": 2, "type": "whole"},
                {"name": "denominator", "value": 2, "type": "whole"}
            ]
        }

        self.create_math_problem(name='P8', editor=self.e2, qtype=question.MULTIPLE_CHOICE,
                                 stem=stem, keys=keys, status=status.PUBLISHED)

    def create_math_problem(self, name, editor=None, qtype=None, stem=None, keys=None, status=status.CREATED):
        obj = Math(name=name)

        if stem:
            obj.stem = stem

        if keys:
            obj.keys = keys

        if qtype:
            obj.qtype = qtype

        obj.save()

        if editor:
            obj.editors.add(editor)

        obj.status = status

        obj.save()

        return obj

    def setUpExam(self):
        self.exam1 = ExamProblems.objects.create(teacher=self.t3)

        self.exam1.problems.add(ProblemInstance.objects.get(pk=1))
        self.exam1.problems.add(ProblemInstance.objects.get(pk=2))
        self.exam1.problems.add(ProblemInstance.objects.get(pk=3))

        self.exam2 = ExamProblems.objects.create(teacher=self.t3)

        self.exam2.problems.add(ProblemInstance.objects.get(pk=5))
