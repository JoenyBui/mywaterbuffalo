from __future__ import unicode_literals

import django_filters

from utilities.filters import NullableCharFieldFilter, NullableModelMultipleChoiceFilter, NumericInFilter
from .models import Math


class MathFilter(django_filters.FilterSet):
    parent_id = NullableModelMultipleChoiceFilter(
        queryset=Math.objects.all(),
        label='Parent region (ID)',
    )
    parent = NullableModelMultipleChoiceFilter(
        queryset=Math.objects.all(),
        to_field_name='slug',
        label='Parent region (slug)',
    )

    class Meta:
        model = Math
        fields = ['stem', 'keys']
