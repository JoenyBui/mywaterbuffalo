from django.contrib.auth.models import User

from django.db import models


class Editor(models.Model):
    """
    Editor has a one-to-one relationship with the user.  All things related to
    creating problem templates runs through the Editor model.

    """
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    pen_name = models.CharField(default='', max_length=100)

    def __str__(self):
        return self.pen_name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        models.Model.save(self,
                          force_insert=force_insert,
                          force_update=force_update,
                          using=using,
                          update_fields=update_fields)


    @staticmethod
    def get_editor_id(user_instance):
        """
        Get editor ID.

        :param user_instance:
        :return:
        """
        try:
            if user_instance.editor:
                return user_instance.editor.id
        except Editor.DoesNotExist as e:
            return None


class SuperPowerBase(models.Model):
    """
    Super Power gives each editor more strength on their voting power.

    validated: power only kicks in if it's validated.

    """
    strength = models.IntegerField(default=1)
    editor = models.ForeignKey(Editor, on_delete=models.PROTECT)
    assigned = models.DateTimeField(auto_now_add=True)
    validated = models.BooleanField(default=False)

    class Meta:
        abstract = True


class PowerSensei(SuperPowerBase):
    """
    Sensei are deem to have more experience, although we all know that's not always true.

    """
    def __init__(self, *args, **kwargs):
        SuperPowerBase.__init__(self, *args, **kwargs)

        self.strength = 9
        self.validated = False


class PowerPupil(SuperPowerBase):
    """
    Pupil gets a base power of 1.  Babies need time to grow.

    """
    def __init__(self, *args, **kwargs):
        SuperPowerBase.__init__(self, *args, **kwargs)
        self.strength = 2
        self.validated = True


class PowerGuardian(SuperPowerBase):
    """
    Guardians get a 0.5 point.  They are too biased to trust.

    """
    def __init__(self, *args, **kwargs):
        SuperPowerBase.__init__(self, *args, **kwargs)
        self.strength = 1
        self.validated = True


class PowerTopicExpert(SuperPowerBase):
    """
    Perceive Experts gets the most say in a topic.  These powers are
    problem specific.  Nobody wants a Philosophy major voting on Science.

    """
    def __init__(self, *args, **kwargs):
        SuperPowerBase.__init__(self, *args, **kwargs)
        self.strength = 15
        self.validated = False
