from django.contrib import admin

from problem.domain import DOMAIN_FRACTIONS, DOMAIN_ADDITION, DOMAIN_SUBTRACTION, DOMAIN_DIVISION, DOMAIN_MULTIPLICATION

from mathematics.models import Math
from mathematics.models.fraction import Fraction
from mathematics.models.addition import Addition
from mathematics.models.subtraction import Subtraction
from mathematics.models.multiplication import Multiplication
from mathematics.models.division import Division


class MathAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain')


class FractionAdmin(admin.ModelAdmin):
    list_display = ('name', )

    def get_queryset(self, request):
        return self.model.objects.filter(domain=DOMAIN_FRACTIONS)


class AdditionAdmin(admin.ModelAdmin):
    list_display = ('name', )

    def get_queryset(self, request):
        return self.model.objects.filter(domain=DOMAIN_ADDITION)


class SubtractionAdmin(admin.ModelAdmin):
    list_display = ('name', )

    def get_queryset(self, request):
        return self.model.objects.filter(domain=DOMAIN_SUBTRACTION)


class MultiplicationAdmin(admin.ModelAdmin):
    list_display = ('name', )

    def get_queryset(self, request):
        return self.model.objects.filter(domain=DOMAIN_MULTIPLICATION)


class DivisionAdmin(admin.ModelAdmin):
    list_display = ('name', )

    def get_queryset(self, request):
        return self.model.objects.filter(domain=DOMAIN_DIVISION)


admin.site.register(Math, MathAdmin)
admin.site.register(Fraction, FractionAdmin)
admin.site.register(Addition, AdditionAdmin)
admin.site.register(Subtraction, SubtractionAdmin)
admin.site.register(Multiplication, MultiplicationAdmin)
admin.site.register(Division, DivisionAdmin)