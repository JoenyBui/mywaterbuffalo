from django.shortcuts import render

from utilities.views import ObjectListView

from . import filters, forms, tables

from .models import (
    Math
)

# Create your views here.


class MathematicsListView(ObjectListView):
    # queryset = Math.objects.select_related('region', 'tenant')
    queryset = Math.objects.all()
    filter = filters.MathFilter
    filter_form = forms.MathFilterForm
    table = tables.MathDetailTable
    template_name = 'math/math_list.html'
