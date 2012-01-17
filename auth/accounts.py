from django.db import models
from django.contrib.auth.models import User
from registration.models import Registration

class SchoolAccount(models.Model):
    user = models.OneToOneField(User)
    registration = models.ForeignKey(Registration)
    
    short_name = models.CharField(max_length=32, unique=True, verbose_name='URL-friendly school name')
    
    
    def __unicode__(self):
        return unicode(self.registration.school)
    
