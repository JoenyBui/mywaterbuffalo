from django.contrib import admin

from core.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    """

    """
    list_display = ('user', 'bio', 'location', 'birth_date', 'website', 'twitter')


admin.site.register(Profile, ProfileAdmin)
