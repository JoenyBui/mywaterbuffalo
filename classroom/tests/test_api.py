from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as rf_reverse
from rest_framework.test import APIRequestFactory

from mathematics.models import ProblemInstance
from classroom.models import ExamProblems

from core.tests import _BaseSetting

factory = APIRequestFactory()


class ExamApiTest(APITestCase, _BaseSetting):
    def setUp(self):
        _BaseSetting.setUp(self)

        self.exam = ExamProblems.objects.create(teacher=self.t3)

        self.exam.problems.add(ProblemInstance.objects.get(pk=1))
        self.exam.problems.add(ProblemInstance.objects.get(pk=2))
        self.exam.problems.add(ProblemInstance.objects.get(pk=3))

        self.client.force_login(user=self.u1)

    def test_list(self):
        url = rf_reverse('v1:classroom:exam-problems-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['problems'], [1, 2, 3])


