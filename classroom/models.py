import datetime

from django.contrib.auth.models import User

from django.db import models
from django.contrib.postgres.fields import JSONField

from problem.models import ProblemInstance, AnswerInstance

# Create your models here.


class Sensei(models.Model):
    """
    **Teacher Model**.

    :user:
        User Model

    :pen_name:
        Pen Name

    """
    user = models.OneToOneField(User, null=True)
    pen_name = models.CharField(default='', max_length=100)

    def __str__(self):
        return self.pen_name


class Pupil(models.Model):
    """
    **Student Model**

    :user:
        User Model

    :pen_name:
        Pen Name

    :teachers:
        Sensei objects

    """
    user = models.OneToOneField(User)
    pen_name = models.CharField(default='', max_length=100)
    teachers = models.ManyToManyField(Sensei)

    def __str__(self):
        return self.pen_name


class ExamProblems(models.Model):
    """
    **Exam Problems Model**

    name
        Name of the exam

    teacher
        Teacher pointer

    problems
        Array of problems

    status
        Exam current status

        :0: Created
        :1: Draft
        :2: Submitted
        :3: Lock

    created
        date and time when exam is created

    modified
        date and time when exam is modified

    """
    CREATED = 0
    DRAFT = 1
    SUBMITTED = 2
    LOCK = 3

    STATUS_CHOICES = (
        (CREATED, 'Created'),
        (DRAFT, 'Draft'),
        (SUBMITTED, 'Submitted'),
        (LOCK, 'Lock')
    )

    name = models.CharField(default='', max_length=100)
    teacher = models.ForeignKey(Sensei)
    problems = models.ManyToManyField(ProblemInstance, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=CREATED)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        self.modified = datetime.datetime.now()

        models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def add_problem(self, problem):
        """
        Add problem into array

        :param problem:
        :return:
        """
        self.problems.add(problem)


class ExamAnswers(models.Model):
    """
    **Exam Answers Model**

    student
        Student pointer

    exam
        Exam of pointer

    answer
        json

    grade
        Float of the grade exam

    status
        Exam current status

        :0: Created
        :1: Draft
        :2: Submitted
        :3: Lock

    created
        date and time when exam is created

    modified
        date and time when exam is modified

    """
    CREATED = 0
    DRAFT = 1
    SUBMITTED = 2
    LOCK = 3

    STATUS_CHOICES = (
        (CREATED, 'Created'),
        (DRAFT, 'Draft'),
        (SUBMITTED, 'Submitted'),
        (LOCK, 'Lock')
    )

    student = models.ForeignKey(Pupil)
    exam = models.ForeignKey(ExamProblems)
    answers = JSONField(default={})
    results = JSONField(default={})
    grade = models.FloatField(default=0.0)
    status = models.IntegerField(choices=STATUS_CHOICES, default=CREATED)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Answer Key %d' % self.pk

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        self.modified = datetime.datetime.now()

        # self.clean_answers_dataset()
        # self.grade_test()

        models.Model.save(self, force_insert=force_insert, using=using, update_fields=update_fields)

    def clean_answers_dataset(self):
        """
        Clean answer dataset

        :return:
        """
        answers = {}

        for key, item in self.answers.items():
            answers[int(key)] = item

        self.answers = answers

    def grade_test(self):
        """
        Grade the test

        :return:beater
        """
        keys = {}

        # Loop through problem set.
        for item in self.exam.problems.all():
            id = item.pk

            if self.answers.get(id) is not None:
                keys[id] = item.check_answer(self.answers.get(id))
            else:
                keys[id] = False

        correct = 0
        incorrect = 0

        for index, item in keys.items():
            if item:
                correct += 1
            else:
                incorrect += 1

        self.grade = float(correct) / float(correct+incorrect)

        self.results = keys


class Assignment(models.Model):
    """
    **Assignment**


    """
    student = models.ForeignKey(Pupil)
    exam = models.ForeignKey(ExamProblems)
    answers = models.ForeignKey(ExamAnswers, null=True)
    grade = models.FloatField(default=0.0)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now_add=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        self.modified = datetime.datetime.now()

        models.Model.save(self, force_insert=force_insert, using=using, update_fields=update_fields)


class Class(models.Model):
    """
    Class Model

    """
    name = models.CharField(default='', max_length=100)
    teacher = models.ForeignKey(Sensei)
    students = models.ManyToManyField(Pupil)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return '%s' % self.name


class ClassAssignment(models.Model):
    """
    Class Assignments Model

    """
    classroom = models.ForeignKey(Class)
    exam = models.ForeignKey(ExamProblems)
    assignments = models.ManyToManyField(Assignment)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now_add=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        models.Model.save(self, force_insert=force_insert, using=using, update_fields=update_fields)

        # Loop through classroom and assigned test to all the kids.
        for obj in self.classroom.students.all():
            ass = Assignment(student=obj,
                             exam=self.exam)
            ass.save()

            self.assignments.add(ass)

