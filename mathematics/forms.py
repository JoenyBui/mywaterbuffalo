from django import forms


# from utilities.forms import CustomFieldForm, CustomFieldBulkEditForm, CustomFieldFilterForm
from utilities.forms import (
    APISelect, add_blank_choice, ArrayFieldSelectMultiple, BootstrapMixin, BulkEditForm, BulkEditNullBooleanSelect,
    ChainedFieldsMixin, ChainedModelChoiceField, CommentField, ConfirmationForm, CSVChoiceField, ExpandableNameField,
    FilterChoiceField, FlexibleModelChoiceField, Livesearch, SelectWithDisabled, SmallTextarea, SlugField,
    FilterTreeNodeMultipleChoiceField,
)

from .models import (
    Math
)


# class MathFilterForm(BootstrapMixin, CustomFieldFilterForm):
#     model = Math
#     q = forms.CharField(required=False, label='Search')
#     region = FilterTreeNodeMultipleChoiceField(
#         queryset=Math.objects.annotate(filter_count=Count('sites')),
#         to_field_name='slug',
#         required=False,
#     )
#     tenant = FilterChoiceField(
#         queryset=Tenant.objects.annotate(filter_count=Count('sites')),
#         to_field_name='slug',
#         null_option=(0, 'None')
#     )
#