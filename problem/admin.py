from django.contrib import admin

from .models import ProblemBase, ProblemInstance
from .models import AnswerInstance, AnswerFillInTheBlank, AnswerMultipleChoice, AnswerShortAnswer, AnswerTrueOrFalse

# Register your models here.


class ProblemBaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'tags', 'status',)


class ProblemInstanceAdmin(admin.ModelAdmin):
    list_display = ('data', 'root')


class AnswerInstanceAdmin(admin.ModelAdmin):
    list_display = ('problem',)


class AnswerFillInTheBlankAdmin(admin.ModelAdmin):
    list_display = ('data',)


class AnswerMultipleChoiceAdmin(admin.ModelAdmin):
    list_display = ('data',)


class AnswerShortAnswerAdmin(admin.ModelAdmin):
    list_display = ('data',)


class AnswerTrueOrFalseAdmin(admin.ModelAdmin):
    list_display = ('data',)


admin.site.register(ProblemBase, ProblemBaseAdmin)
admin.site.register(ProblemInstance, ProblemInstanceAdmin)
admin.site.register(AnswerInstance, AnswerInstanceAdmin)
admin.site.register(AnswerFillInTheBlank, AnswerFillInTheBlankAdmin)
admin.site.register(AnswerMultipleChoice, AnswerMultipleChoiceAdmin)
admin.site.register(AnswerShortAnswer, AnswerShortAnswerAdmin)
admin.site.register(AnswerTrueOrFalse, AnswerTrueOrFalseAdmin)
