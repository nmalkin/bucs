from django.db import models
from django.core.validators import MinValueValidator

class Crisis(models.Model):
    name = models.CharField(max_length=64)
    short_name = models.CharField(max_length=32) # url-friendly name
    description = models.TextField(blank=True)
    #icon = models.ImageField(upload_to='crises', blank=True) # TODO: use storage object to put it in the standard image directory?
    
    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        app_label = 'conference'
        verbose_name_plural = 'crises'

def crisis_count():
    return len(Crisis.objects.all())

class Committee(models.Model):
    crisis = models.ForeignKey('Crisis')
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    size = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1)], verbose_name='number of delegates')
    
    def __unicode__(self):
        return unicode(self.crisis) + ': ' + unicode(self.name)

    class Meta:
        app_label = 'conference'

class Role(models.Model):
    committee = models.ForeignKey('Committee')
    role = models.CharField(max_length=256, blank=True) # e.g., Emperor of France

    def __unicode__(self):
        return unicode(self.role)

    class Meta:
        app_label = 'conference'
