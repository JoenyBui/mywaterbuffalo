import django_tables2 as tables

from utilities.tables import BaseTable, ToggleColumn

from .models import Math


class MathTable(BaseTable):
    pk = ToggleColumn()
    # name = tables.LinkColumn()
    # region = tables.TemplateColumn(template_code=SITE_REGION_LINK)
    # tenant = tables.LinkColumn('tenancy:tenant', args=[Accessor('tenant.slug')])

    class Meta(BaseTable.Meta):
        model = Math
        fields = ('pk',)


class MathDetailTable(MathTable):

    class Meta(MathTable.Meta):
        fields = (
            'pk',
        )