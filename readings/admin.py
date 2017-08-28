from django.contrib import admin

from readings.models import Reading
from readings.models.vocabulary import Vocabulary
from readings.models.spelling import Spelling


class ReadingAdmin(admin.ModelAdmin):
    list_display = ('name',)


class VocabularyAdmin(admin.ModelAdmin):
    list_display = ('name', )


class SpellingAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Reading, ReadingAdmin)
admin.site.register(Vocabulary, VocabularyAdmin)
admin.site.register(Spelling, SpellingAdmin)

