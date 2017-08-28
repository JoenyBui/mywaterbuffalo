from django.contrib import admin

from editor.models import Editor, PowerSensei, PowerPupil, PowerGuardian, PowerTopicExpert

# Register your models here.

class EditorAdmin(admin.ModelAdmin):
    list_display = ('user', 'pen_name')


class PowerSenseiAdmin(admin.ModelAdmin):
    list_display = ('strength', 'editor', 'assigned', 'validated')


class PowerPupilAdmin(admin.ModelAdmin):
    list_display = ('strength', 'editor', 'assigned', 'validated')


class PowerGuardianAdmin(admin.ModelAdmin):
    list_display = ('strength', 'editor', 'assigned', 'validated')


class PowerTopicExpertAdmin(admin.ModelAdmin):
    list_display = ('strength', 'editor', 'assigned', 'validated')

admin.site.register(Editor, EditorAdmin)
admin.site.register(PowerSensei, PowerSenseiAdmin)
admin.site.register(PowerPupil, PowerPupilAdmin)
admin.site.register(PowerGuardian, PowerGuardianAdmin)
admin.site.register(PowerTopicExpert, PowerTopicExpertAdmin)
