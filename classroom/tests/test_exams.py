import os

from django.test import TestCase
from django.contrib.auth.models import User

from mathematics.models import Math, ProblemBase, QuestionTypeBase, ProblemInstance
from editor.models import Editor
from classroom.models import Sensei, ExamProblems, ExamAnswers

from core.tests import _BaseSetting

# Create your tests here.


class TestExam(TestCase, _BaseSetting):

    def setUp(self):
        _BaseSetting.setUp(self)

        self.exam = ExamProblems.objects.create(teacher=self.t3)

        self.exam.problems.add(ProblemInstance.objects.get(pk=1))
        self.exam.problems.add(ProblemInstance.objects.get(pk=2))
        self.exam.problems.add(ProblemInstance.objects.get(pk=3))

    def test_number_of_problems(self):
        self.assertEqual(self.exam.problems.count(), 3)


class TestExamAnswersTrueOrFalse(TestCase, _BaseSetting):

    def setUp(self):
        _BaseSetting.setUp(self)

        self.answer = ExamAnswers()
        self.answer.exam = self.exam1
        self.answer.student = self.s4
        self.answer.answers = {
            1: 10,
            2: 6,
            3: 11
        }
        self.answer.save()

    def test_data_answers(self):
        self.answer.grade_test()

        self.assertEqual(self.answer.grade, 1.0)


class TestExamAnswersMultipleChoice(TestCase, _BaseSetting):

    def setUp(self):
        _BaseSetting.setUp(self)

        self.answer = ExamAnswers()
        self.answer.exam = self.exam2
        self.answer.student = self.s4
        self.answer.answers = {
            5: "3/4",
        }
        self.answer.save()

    def test_data_answers(self):
        self.answer.grade_test()

        self.assertEqual(self.answer.grade, 1.0)

