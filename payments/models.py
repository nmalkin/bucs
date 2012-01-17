from django.db import models

class Item(models.Model):
    description = models.CharField(max_length=128)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    school = models.ForeignKey('registration.Registration')

    def __unicode__(self):
        return u'%s: %s (%d)' % (self.school, self.description, self.amount)

    class Meta:
        abstract = True

class Due(Item):
    paid = models.BooleanField() 

class Payment(Item):
    comment = models.CharField(max_length=256, blank=True)
    date = models.DateField(auto_now_add=True)
