from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import ExtendedDefaultRouter

from .viewsets import (
    TopicViewSet
)

router = DefaultRouter()
router.register(r'topics', TopicViewSet, 'topic')
