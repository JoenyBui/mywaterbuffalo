from rest_framework.viewsets import ViewSet
from rest_framework_extensions.routers import ExtendedDefaultRouter
# from rest_framework_nested import routers as NestedRouter


from classroom import viewsets
from problem import viewsets as problem_viewsets


router = ExtendedDefaultRouter()
# router = NestedRouter.DefaultRouter()

sensei_router = router.register(r'sensei', viewsets.SenseiModelViewSets, 'sensei')
sensei_router.register(r'exams',
                       viewsets.ExamProblemsModelViewSet,
                       basename='sensei-exams',
                       parents_query_lookups=['teacher'])

pupil_router = router.register(r'pupil', viewsets.PupilModelViewSets, 'pupil')
pupil_router.register(r'exams',
                      viewsets.ExamAnswerModelViewSet,
                      basename='pupil-exams',
                      parents_query_lookups=['student'])
class_router = router.register(r'class', viewsets.ClassModelViewSet, 'class')
class_router.register(r'students',
                      viewsets.PupilModelViewSets,
                      basename='class-pupil',
                      parents_query_lookups=['class'])
class_router.register(r'teachers',
                      viewsets.SenseiModelViewSets,
                      basename='class-sensei',
                      parents_query_lookups=['class'])

# from rest_framework.routers import
# exam_problem_router = router.register(r'exam-problems', viewsets.ExamProblemsModelViewSet, base_name='exam-problems')

exam_problem_router = router.register(r'exam-problems', viewsets.ExamProblemsModelViewSet, 'exam-problems')
exam_problem_router.register(r'problems',
                             problem_viewsets.ProblemInstanceModelViewSet,
                             basename='exam-problems-instance',
                             parents_query_lookups=['examproblems'])

# from problem.models import ProblemInstance
# from problem.serializers import ProblemInstanceSerializer
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
#
# class ProblemInstanceViewSet(ViewSet):
#     serializer_class = ProblemInstanceSerializer
#
#     def list(self, request,):
#         queryset = ProblemInstance.objects.filter()
#         serializer = ProblemInstanceSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = ProblemInstance.objects.filter()
#         client = get_object_or_404(queryset, pk=pk)
#         serializer = ProblemInstanceSerializer(client)
#         return Response(serializer.data)
#
#
# exam_problem_problem_router = NestedRouter.NestedSimpleRouter(exam_problem_router, r'', lookup='exam-problems')
# exam_problem_problem_router.register(r'problems', ProblemInstanceViewSet, base_name='exam-problems-problems')

exam_answer_router = router.register(r'exam-answers', viewsets.ExamAnswerModelViewSet, 'exam-answers')
assignments_router = router.register(r'assignments', viewsets.AssignmentModelViewSet, 'assignments')
class_assignment_router = router.register(r'class-assignments', viewsets.ClassAssignmentsModelViewSet, 'class-assignments')