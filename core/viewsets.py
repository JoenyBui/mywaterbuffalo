from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters

from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.generics import RetrieveUpdateAPIView

from .serializers import ProfileSerializer, UserRoleSerializer


class ProfileDetailViewSets(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_fields = ('id', 'first_name')
    # search_fields = ('first_name', 'last_name')
    # ordering_fields = ('id', )

    # def get_queryset(self):
    #     return User.objects.filter(pk=self.request.user.pk)

    def get_object(self):
        return self.request.user


class UserRoleDetailViewSet(RetrieveUpdateAPIView):
    serializer_class = UserRoleSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
