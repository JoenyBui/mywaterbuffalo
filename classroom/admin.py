from django.contrib import admin

from .models import Sensei, Pupil, ExamProblems, ExamAnswers

# Register your models here.


class SenseiAdmin(admin.ModelAdmin):
    list_display = ('user',)


class PupilAdmin(admin.ModelAdmin):
    list_display = ('user',)


class ExamProblemAdmin(admin.ModelAdmin):
    list_display = ('teacher',)


class ExamAnswersAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam')


admin.site.register(Sensei, SenseiAdmin)
admin.site.register(Pupil, PupilAdmin)
admin.site.register(ExamProblems, ExamProblemAdmin)
admin.site.register(ExamAnswers, ExamAnswersAdmin)
