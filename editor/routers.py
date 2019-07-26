from rest_framework_extensions.routers import ExtendedDefaultRouter

from problem.viewsets import ProblemBaseModelViewSet
from . import viewsets

# Create a router and register our viewsets with it.
router = ExtendedDefaultRouter()

router.register(r'users', viewsets.UserModelViewSets, 'users')
router.register(r'power-sensei', viewsets.PowerSenseiViewSets, 'power-sensei'),
router.register(r'power-pupil', viewsets.PowerPupilViewSets, 'power-pupil'),
router.register(r'power-guardian', viewsets.PowerGuardianViewSets, 'power-guardian')
router.register(r'power-topic-experts', viewsets.PowerTopicExpertViewSets, 'power-topic-experts')


# Editor
editor_router = router.register(r'editors', viewsets.EditorModelViewSets, basename='editors')
editor_router.register(r'power-sensei', viewsets.PowerSenseiViewSets, basename='editors-power-sensei', parents_query_lookups=['editors'])
editor_router.register(r'power-pupil', viewsets.PowerPupilViewSets, basename='editors-power-pupil', parents_query_lookups=['editors'])
editor_router.register(r'power-guardian', viewsets.PowerGuardianViewSets, 'editors-power-guardian', parents_query_lookups=['editors'])
editor_router.register(r'power-topic-experts', viewsets.PowerTopicExpertViewSets, 'editors-power-topic-experts', parents_query_lookups=['editors'])
editor_router.register(r'problems', ProblemBaseModelViewSet, 'editors-problem-base', parents_query_lookups=['editors'])
