from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.conf import settings

from editor.models import Editor


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_root(sender, instance=None, created=False, **kwargs):
    if created:
        editor = Editor.objects.create(user=instance)
        editor.save()

