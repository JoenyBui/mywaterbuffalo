from django.test import TestCase
from django.contrib.auth.models import User

from editor.models import Editor

from problem.models import ProblemBase, QuestionTypeBase
from mathematics.models import Math


class _BaseSetUser(TestCase):
    """
    Setup the common base user/editor setup.

    """
    def setUp(self):
        self.user = User.objects.create_user(username='test_user1', password='password')
        self.editor = Editor.objects.create(pen_name='Giant Man', user=self.user)


class TestMathFillInTheBlank(_BaseSetUser):
    """
    Test Fill-in-the-Blank

    """
    def setUp(self):
        _BaseSetUser.setUp(self)

        self.problem = Math(name='Fill in the Blank')

        self.problem.set_fill_in_the_blank()
        self.problem.stem = dict(statement="{{left}} + {{right}} = {{blank}}", )
        self.problem.keys = dict(
            variables=[
                dict(name='left', value=1, type='decimal'),
                dict(name='right', value=2, type='decimal'),
            ],
            answer=[
                3
            ]
        )

    def test_set(self):
        self.assertEqual(self.problem.qtype, QuestionTypeBase.FILL_IN_THE_BLANK)

    def test_submit(self):
        self.problem.status = ProblemBase.PUBLISHED
        self.problem.save()

        self.assertEqual(len(self.problem.probleminstance_set.all()), 1)


class TestMathTrueOrFalse(_BaseSetUser):
    """
    Test True or False

    """
    def setUp(self):
        _BaseSetUser.setUp(self)

        self.problem = Math(name='True or False')

        self.problem.set_true_or_false()
        self.problem.stem = dict(
            statement="{{left}} is the same as {{numerator}}/{{denominator}}",
            figures=[],
            charts=[]
        )
        self.problem.keys = dict(
            variables=[
                dict(name='left', value=0.1, type='decimal'),
                dict(name='numerator', value=1, type='whole'),
                dict(name='denominator', value=10, type='whole')
            ],
            answer=True
        )

    def test_submit(self):
        self.problem.status = ProblemBase.PUBLISHED
        self.problem.save()

        self.assertEqual(len(self.problem.probleminstance_set.all()), 1)


class TestMathMultipleChoice(_BaseSetUser):
    """
    Test Multiple Choice

    """
    def setUp(self):
        _BaseSetUser.setUp(self)

        # Problem
        self.p1 = Math(name='Multiple Choice')
        self.p1.set_multiple_choice()
        self.p1.stem = dict(
            statement="Which of the following is a subset of {b, c, d}?"
        )
        self.p1.keys = dict(
            choices=[
                "{ }",
                "{1, 2, 3}",
                "{a, b, c}"
            ],
            answer="{a}"
        )

        self.p2 = Math(name="MC ")
        self.p2.set_multiple_choice()
        self.p2.stem = dict(
            statement="The value of {{left}} in the number {{full_number}} is"
        )
        self.p2.keys = dict(
            variables=[
                dict(name='left', value=5, type='whole'),
                dict(name='full_number', value=357.21, type='decimal')
            ],
            choices=[
                "5 ones",
                "5 tens",
                "5 hundreds"
            ],
            answer="5 tenths"
        )

    def test_submit(self):
        self.p2.status = 4
        self.p2.save()

        # Check if the problem instance exists and it's the correct one.
        self.assertEqual(len(self.p2.probleminstance_set.all()), 1)
