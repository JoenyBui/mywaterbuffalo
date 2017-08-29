# -*- coding:utf-8 -*-
#from abc import abstractclassmethod

from jinja2 import Template
import random
import datetime

from django.db import models
# from django.contrib.postgres.fields import JSONField
from django_mysql.models.fields.json import JSONField

from taggit.managers import TaggableManager

from editor.models import Editor
from topic.models import Topic

from problem import domain
from problem import question
from problem import status


class ProblemBase(models.Model):
    """
    Base Problem.

    name
        Name of the problem base

    editors
        A problem can have many editors, but a editor can be working on many problems as well.

    tags
        Are used to tag problems category, grade level, etc.

    topic
        Many to many topics

    status
        Status choices

    domain
        Domain type

    created
        Date Time Field

    modified
        Date Time Field

    """

    name = models.CharField(max_length=100)
    editors = models.ManyToManyField(Editor)
    tags = TaggableManager()
    topics = models.ManyToManyField(Topic, default=None)
    status = models.IntegerField(choices=status.STATUS_CHOICES, default=status.CREATED)
    domain = models.IntegerField(choices=domain.DOMAIN_CHOICES, default=domain.DOMAIN_UNKNOWN)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        """

        :return:
        """
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        self.modified = datetime.datetime.now()

        models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def status_draft(self):
        """
        When model is first created, it's currently worked on the by the editor.

        :return:
        """
        self.status = self.DRAFT

        return True

    def status_submitted(self):
        """
        Main author submits the model for verification/validation.

        :return:
        """
        self.status = self.SUBMITTED

        return True

    def status_reviewed(self):
        """
        Problem in reviewed

        :return:
        """
        self.status = self.REVIEWED

        return True

    def status_published(self):
        """
        All the editors approved of the test question and then the algorithm ensure that problem instances can be
        created.

        :return:
        """
        self.status = self.SUBMITTED

        return True

    def status_revised(self):
        """
        After published, some requests that the problem be revised.

        :return:
        """
        self.status = self.REVISED

        return True

    def status_lock(self):
        """
        The model is locked and cannot be revised unless notified to an admin user.

        :return:
        """
        self.status = self.LOCK

        return True

    def get_data(self):
        """
        Get the data from the instance.

        :return:
        """
        try:
            if self.math:
                return self.math.get_instance()
        except Exception as e:
            pass

        try:
            if self.reading:
                return self.reading.get_instance()
        except Exception as e:
            pass

        return None

    def get_count(self):
        try:
            if self.math:
                return self.math.keys.get('count', 1)
        except Exception as e:
            pass

        return None

class QuestionTypeBase(models.Model):
    """
    **Summary**


    Ref: http://hofstrateach.org/index.php?title=Types_of_Questions

    Calculated Formula
        A [Calculated Formula] question contains a formula, the variables of which can be set to change for each user.

    Calculated Numeric
        A [Calculated Numeric] question resembles a fill-in-the-blank question. The user enters a number to complete a
        statement. The correct answer can be a specific number or within a range of numbers. Please note that the answer
        must be numeric, not alphanumeric.

    Either/Or
        In an [Either/Or]question, users are presented with a statement and asked to respond using a selection of
        pre-defined two-choice answers, such as: Yes/No, Agree/Disagree, Right/Wrong

    Essay
        [Essay] questions must be graded manually. Essay questions may use the Math and Science Notation Tool.

    File Upload
        In a [File Upload] question, users upload a file from the local drive as the answer to the question. This type
        of question is graded manually.

    Fill in the Blank
        [Fill in the Blank] answers are evaluated based on an exact text match. Accordingly, it is important to keep the
        answers simple and limited to as few words as possible.

    Fill in Multiple Blanks
        [Fill in Multiple Blanks]builds on fill-in-the-blank questions with multiple fill in the blank responses that
        can be inserted into a sentence or paragraph. Separate sets of answers are defined for each blank.

    Hot Spot
        in a [Hot Spot] question, users indicate the answer by marking a specific point on an image. A range of pixel
        coordinates is used to define the correct answer. For example in Geography to select an area QuestionTypeBaseon a map.

    Matching
        [Matching] questions allow Students to pair items in one column to items in another column. Instructors may
        include a different numbers of questions and answers.

    Ordering
        [Ordering] questions require users to provide an answer by selecting the correct order of a series of items.

    Jumbled Sentence
        In a [Jumbled Sentence], users are shown a sentence with a few parts of the sentence as variables. The user
        selects the proper answer for each variable from drop-down lists to assemble the sentence.

    Multiple Choice
        [Multiple-Choice] questions allow the users a multitude of choices with only one correct answer. In
        multiple-choice questions, users indicate the correct answer by selecting a radio button.

    Multiple Answer
        [Multiple Answer] questions allow users to choose more than one answer. The number of answer choices is limited
        to 20.

    Opinion Scale/Likert
        [Opinion Scale/Likert] questions are based on a rating scale designed to measure attitudes or reactions. This
        type of question is popular to use in surveys in order to get a comparable scale of opinion.

    Quiz Bowl
        (Jeopardy®-like) [Quiz Bowl] questions are a way to add fun and creativity to tests, such as self assessments or
        in-class contests. The user is shown the answer and responds by entering the correct question into a text box.

    Short Answer
        [Short Answer] questions are similar to essay questions. The length of the answer can be limited to a specified
        number of rows in the text box. Essay questions, Short Answer questions must be graded manually.

    True/False
        [True/False] questions allow the user to choose either true or false. True and False answer options are limited
        to the words True and False.

    Random Block
        [Random Block]s enable the Instructor to use a random selection of questions from a Pool. Be aware that it is
        not possible to add a Random Block of questions from another Test or Survey.

    From a Question Pool or Assessment
        Questions can be added from a [Question Pool or Assessment]. This section discusses how to select specific
        questions from Pools and other Assessments. Instructors may choose questions based on category, keyword and
        question type.

    Upload Questions
        You can use [Upload Questions] to import files containing questions into an Assessment. The questions in the
        uploaded file must match the file structure explained below. The file may include Essay, Ordering, Matching,
        Fill in the Blank, Multiple Choice, Multiple Answer, and True/False.


    :param qtype: Question Type defines what type of view question.

        Types

        :0:
            Unassigned
        :1:
            Fill in the Blank
        :2:
            True False
        :3:
            Multiple Choice
        :4:
            Problem Set
        :5:
            Short Answer
        :6:
            Multiple Answer

    """

    qtype = models.IntegerField(choices=question.QUESTION_CHOICES, default=question.UNASSIGNED)   # Question type

    class Meta:
        abstract = True

    def set_fill_in_the_blank(self):
        """
        Set the fill-in-the-blank index.

        :return:
        """
        self.qtype = question.FILL_IN_THE_BLANK

    def set_true_or_false(self):
        """
        Set the true-or-false index.

        :return:
        """
        self.qtype = question.TRUE_OF_FALSE

    def set_multiple_choice(self):
        """
        Set the multiple choice index.

        :return:
        """
        self.qtype = question.MULTIPLE_CHOICE

    def set_problem_set(self):
        """
        Set the problem set index.

        :return:
        """
        self.qtype = question.PROBLEM_SET

    def set_short_answer(self):
        """
        Set the short answer index.

        :return:
        """
        self.qtype = question.SHORT_ANSWER

    def set_multiple_answer(self):
        """
        Set the multiple answer index.

        :return:
        """
        self.qtype = question.MULTIPLE_ANSWER

    def set_word_problem(self):
        """
        Set the word problem index.

        :return:
        """
        self.qtype = question.WORD_PROBLEM

    def get_instance(self):
        """
        Return all possible instance of the models.

        :return:
        """
        return None

    def check_answer(self, answer, *args, **kwargs):
        """
        Check the answer

        :param answer:
        :param args:
        :param kwargs:
        :return:
        """
        pass


class ProblemInstance(models.Model):
    """
    Problem instances are linked to a problem template.


    :1:
        **Fill in the Blank**

        1. stem
            problem statement, blanks is the unique key used in the template language
        2. answer
            list of answers should be the same as the amount of blank spaces

    :2:
        **True False**

        1. stem
            problem statement
        2. answer
            true or false options, use radio choices

    :3:
        **Multiple Choice**

        1. stem
            problem statement
        2. answer
            list of choices, user radio choices

    :4:
        **Problem Set**

    :5:
        **Short Answer**

        1. stem
            problem statement
        2. answer
            open/ended answer, use textbox for answer

    :6:
        **Multiple Answer**

        1. stem
            problem statement
        2. answer
            multiple correct choices, use checkbox for answer selection

    """
    data = JSONField()
    # data = JSONField(default=dict(
    #     keys=dict(),
    #     index=0
    # ))
    root = models.ForeignKey(ProblemBase, default=None)

    def __str__(self):
        return self.root.name

    def get_data(self):
        data = self.root.get_data()

        return data

    def check_answer(self, answer, *args, **kwargs):
        """
        Check if the answer

        :param answer:
        :param args:
        :param kwargs:
        :return:
        """
        index = self.data.get('index')
        qtype = self.data.get('qtype')

        if hasattr(self.root, 'reading'):
            return self.root.reading.check_answer(answer, index, *args, **kwargs)

        elif hasattr(self.root, 'math'):
            clean_answer = None
            if qtype == question.FILL_IN_THE_BLANK:
                clean_answer = answer
            elif qtype == question.TRUE_OF_FALSE:
                clean_answer = bool(answer)
            elif qtype == question.MULTIPLE_CHOICE:
                index = answer
                choices = self.data.get('choices')
                clean_answer = choices[index]

            return self.root.math.check_answer(clean_answer, index, *args, **kwargs)

        else:
            return False

    def get_multiple_choice(self, stem, choices, answer, index, **kwargs):
        """
        Create the multiple choice statement.

        :param stem:
        :param choices:
        :param answer:
        :param index:
        :param kwargs:
        :return:
        """

        # Check to see if all the answers
        # Add choices and answer together.
        choices = choices + [answer]
        random.shuffle(choices)
        data = {}

        for key, item in enumerate(choices):
            data[key] = item

        return dict(qtype=question.MULTIPLE_CHOICE,
                     stem=stem,
                     choices=data,
                     answer=choices.index(answer),
                     index=index)

    def get_true_or_false(self, stem, index, **kwargs):
        """
        Create the true or false statement.

        :param stem: true/false statement
        :param index:
        :param kwargs:
        :return:
        """

        return dict(qtype=question.TRUE_OF_FALSE,
                    stem=stem,
                    choices=[True, False],
                    index=index)

    def get_fill_in_the_blank(self, stem, num_of_blank, index, **kwargs):
        """
        Create a fill-in-the-blank statement.

        :param stem:
        :param num_of_blank:
        :param index:
        :param kwargs:
        :return:
        """

        return dict(qtype=question.FILL_IN_THE_BLANK,
                    stem=stem,
                    num_of_blank=num_of_blank,
                    index=index)


class AnswerInstance(models.Model):
    """
    Answers are linked to problems.

    """
    problem = models.ForeignKey(ProblemInstance, default=None)


class AnswerTrueOrFalse(AnswerInstance):
    """
    Answer for True or False.

    """
    data = models.BooleanField(default=None)


class AnswerMultipleChoice(AnswerInstance):
    """
    Answer for Multiple Choice.

    """
    data = models.IntegerField(default=-1)


class AnswerFillInTheBlank(AnswerInstance):
    """
    Answer Fill in the Blank.

    """
    data = models.CharField(max_length=150, default='')


class AnswerShortAnswer(AnswerInstance):
    """
    Answer Short Answer

    """
    data = models.CharField(max_length=400, default='')
