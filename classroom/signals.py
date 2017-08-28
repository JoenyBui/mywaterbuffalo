from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.conf import settings

from classroom.models import Sensei, Pupil


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_root(sender, instance=None, created=False, **kwargs):
    if created:
        editor = Pupil.objects.create(user=instance)
        editor.save()

