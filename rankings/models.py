from django.db import models
from conference.crisis import Crisis, crisis_count

class CrisisRanking(models.Model):
    school = models.ForeignKey('registration.Registration') # whose preference is this?
    crisis = models.ForeignKey(Crisis) # this is a preference for what committee?
    
    
    choices = [(v, v) for v in range(1, crisis_count() + 1)]
    ranking = models.PositiveSmallIntegerField(choices=choices) # the ranking of this crisis in the preferences

    def __unicode__(self):
        return u'%s: %d - %s' % (self.school.school, self.ranking, self.crisis)

def new_crisis_rankings(school):
    # get all crises
    crises = Crisis.objects.all().order_by('?') # order randomly

    for order, crisis in enumerate(crises):
        ranking = CrisisRanking(school=school.registration, crisis=crisis, ranking=order+1)
        ranking.save()
