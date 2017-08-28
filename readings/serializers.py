from rest_framework import serializers

from .models import Reading
from .models.spelling import Spelling
from .models.vocabulary import Vocabulary


__author__ = ['jbui']


class ReadingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reading


class SpellingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spelling


class VocabularySerializer(serializers.ModelSerializer):

    class Meta:
        model = Vocabulary
