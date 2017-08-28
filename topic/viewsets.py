from rest_framework import viewsets
from rest_framework import permissions

from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Topic
from .serializers import TopicSerializer


class TopicViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Topic View Set
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
