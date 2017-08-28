from collections import OrderedDict

from rest_framework import serializers
from rest_framework.reverse import reverse

# from urllib.parse import urljoin
from urlparse import urljoin

# from classroom.models import Sensei, Pupil
# from editor.models import Editor
from .models import Profile
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    """
    Profile Serializer

    """

    bio = serializers.CharField(source='profile.bio', allow_blank=True)
    location = serializers.CharField(source='profile.location', allow_blank=True)
    birth_date = serializers.DateField(source='profile.birth_date', allow_null=True)
    website = serializers.CharField(source='profile.website', allow_blank=True)
    twitter = serializers.CharField(source='profile.twitter', allow_blank=True)
    avatar = serializers.CharField(source='profile.avatar', allow_blank=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'location', 'birth_date', 'website', 'twitter', 'avatar')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)
        user = super(ProfileSerializer, self).create(validated_data)
        self.create_or_update_profile(user, profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        self.create_or_update_profile(instance, profile_data)
        return super(ProfileSerializer, self).update(instance, validated_data)

    def create_or_update_profile(self, user, profile_data):
        profile, created = Profile.objects.get_or_create(user=user, defaults=profile_data)
        if not created and profile_data is not None:
            super(ProfileSerializer, self).update(profile, profile_data)


class UserRoleSerializer(serializers.ModelSerializer):
    """
    User Role Serializer

    """
    links = serializers.SerializerMethodField(method_name='get_links_url', label='links')

    class Meta:
        model = User
        fields = ('id', 'editor', 'sensei', 'pupil', 'links')

    def get_editor(self, obj):
        try:
            if obj.editor:
                return obj.editor.pk
        except Editor.DoesNotExist as e:
            return None

    def get_sensei(self, obj):

        try:
            if obj.sensei:
                return obj.sensei.pk
        except Sensei.DoesNotExist as e:
            return None

    def get_pupil(self, obj):

        try:
            if obj.pupil:
                return obj.pupil.pk
        except Pupil.DoesNotExist as e:
            return None

    def get_links_url(self, obj, *args, **kwargs):
        """
        Get links url

        :param obj:
        :param args:
        :param kwargs:
        :return:
        """
        links = OrderedDict({})

        # try:
        #     if obj.editor:
        #         links['editor'] = urljoin(reverse('v1:editor:editors-list', request=self.context['request']),
        #                                       str(obj.editor.pk))
        # except Editor.DoesNotExist as e:
        #     links['editor'] = str(e)
        #
        # try:
        #     if obj.sensei:
        #         links['sensei'] = urljoin(reverse('v1:classroom:sensei-list', request=self.context['request']),
        #                                       str(obj.sensei.pk))
        # except Sensei.DoesNotExist as e:
        #     links['sensei'] = str(e)
        #
        # try:
        #     if obj.pupil:
        #         links['pupil'] = urljoin(reverse('v1:classroom:pupil-list', request=self.context['request']),
        #                                      str(obj.pupil.pk))
        # except Pupil.DoesNotExist as e:
        #     links['pupil'] = str(e)

        return links
