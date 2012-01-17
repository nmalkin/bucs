from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
 
class Registration(models.Model):
    school = models.CharField(max_length=100, unique=True, verbose_name='school name')
    contact_person = models.CharField(max_length=100, verbose_name='contact person')
    email = models.EmailField(max_length=100, verbose_name='contact e-mail address')
    phone = models.CharField(max_length=100)
    delegates = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(25)], verbose_name='number of delegates')
    registration_time = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return unicode(self.school)
