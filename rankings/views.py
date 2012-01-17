from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.exceptions import ValidationError

from auth.decorators import *
from conference.crisis import Crisis, crisis_count
from rankings.models import CrisisRanking, new_crisis_rankings

@school_from_short_name
@logged_in_as_school
def crisis_rankings(request, school):
    saved = False

    if request.method == 'POST':
        # process POSTed form
        # NOTE: this is handling things manually, rather than the "Django way" -- using Form objects
        # There doesn't seem to be something suitable for this type of input,
        # and writing custom form fields doesn't seem worth it.
        
        # get all the order_* fields
        rankings = []
        for field, value in request.POST.iteritems():
            print field, value
            if field.startswith('order_'):
                crisis_short_name = field[len('order_'):]
                crisis = Crisis.objects.get(short_name=crisis_short_name)
                ranking = int(value)

                rankings.append(CrisisRanking(school=school.registration, crisis=crisis, ranking=ranking))

        if len(rankings) != crisis_count():
            raise ValidationError('missing or extra crises received')

        # TODO: further validation?

        # clear current rankings
        CrisisRanking.objects.filter(school=school.registration).delete()

        # save the new ones
        for ranking in rankings:
            ranking.save()

        saved = True
    
    rankings = CrisisRanking.objects.filter(school=school.registration).order_by('ranking')
    
    while len(rankings) == 0: # no rankings yet
        new_crisis_rankings(school) # generate new rankings
        rankings = CrisisRanking.objects.filter(school=school.registration).order_by('ranking') # try the query again
    
    crises = [ranking.crisis for ranking in rankings]

    return render_to_response('committee_preferences.html', {
        'school' : school,
        'committees': crises,
        'saved': saved,
    }, context_instance=RequestContext(request))
