from django.db import models
from django.contrib.localflavor.us.forms import USPhoneNumberField

from conference.crisis import Crisis

class Staff(models.Model):
    first_name = models.CharField(max_length=32, verbose_name='first name')
    last_name = models.CharField(max_length=32, verbose_name='last name')
    email = models.EmailField(max_length=100, verbose_name='e-mail address')
    phone = USPhoneNumberField()
    
    def __unicode__(self):
        return unicode((self.first_name, self.last_name))

    class Meta:
        app_label = 'conference'
        ordering = ('last_name', 'first_name')
        verbose_name_plural = 'staff'

class CrisisDirector(Staff):
    crisis = models.ForeignKey('Crisis')

