from django.contrib import admin

# Register your models here.
from topic.models import Topic


class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Topic, TopicAdmin)
