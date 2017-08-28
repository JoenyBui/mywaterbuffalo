from django.test import TestCase

from core.tests import _BaseSetting

from classroom.models import Class, ClassAssignment, Assignment


class TestClass(TestCase, _BaseSetting):

    def setUp(self):
        _BaseSetting.setUp(self)

        self.setUpClassroom()
        self.setUpClassAssignment()

    def setUpClassroom(self):
        self.cls = Class()

        self.cls.name = 'Donkeys'
        self.cls.teacher = self.t3
        self.cls.save()

        self.cls.students.add(self.s4)
        self.cls.students.add(self.s6)

    def setUpClassAssignment(self):
        self.clsAssignment = ClassAssignment()

        self.clsAssignment.exam = self.exam1
        self.clsAssignment.classroom = self.cls

        self.clsAssignment.save()

    def test_num_of_students(self):
        self.assertEqual(self.cls.students.count(), 2)

    def test_class_assignment(self):
        self.assertEqual(self.clsAssignment.assignments.count(), 2)


