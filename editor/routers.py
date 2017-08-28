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
editor_router = router.register(r'editors', viewsets.EditorModelViewSets, 'editors')
editor_router.register(r'power-sensei',
                       viewsets.PowerSenseiViewSets,
                       base_name='editors-power-sensei',
                       parents_query_lookups=['editor'])
editor_router.register(r'power-pupil',
                       viewsets.PowerPupilViewSets,
                       base_name='editors-power-pupil',
                       parents_query_lookups=['editor'])
editor_router.register(r'power-guardian',
                       viewsets.PowerGuardianViewSets,
                       'editor-power-guardian',
                       parents_query_lookups=['editor'])
editor_router.register(r'power-topic-experts',
                       viewsets.PowerTopicExpertViewSets,
                       'editor-power-topic-experts',
                       parents_query_lookups=['editor'])
editor_router.register(r'problems',
                       ProblemBaseModelViewSet,
                       'editor-problem-base',
                       parents_query_lookups=['editors'])
