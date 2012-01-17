from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class Fees(models.Model):
    delegation = models.IntegerField()
    delegate = models.IntegerField()

    class Meta:
        app_label = 'conference'
        verbose_name_plural = 'fees'
