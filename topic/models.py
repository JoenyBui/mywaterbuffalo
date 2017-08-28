from django.db import models

# Create your models here.


class Topic(models.Model):
    """
    Topic of the problems.

    """
    name = models.CharField(default='', max_length=100)
    key = models.IntegerField(default=0)

    def __str__(self):
        return "%s - %d" % (self.name, self.key)
