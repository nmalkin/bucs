from django.db import models
from registration.models import Registration as School
from conference.crisis import Role

class Assignment(models.Model):
    role = models.OneToOneField(Role)
    school = models.ForeignKey(School)
    delegate_name = models.CharField(max_length=128, blank=True)

    def __unicode__(self):
        return unicode(self.role)
