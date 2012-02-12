from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseBadRequest, HttpResponseRedirect

from auth.decorators import *

from models import Assignment

@school_from_short_name
@logged_in_as_school
def assignments(request, school_account):
    if request.method == 'POST':
        for field, value in request.POST.iteritems():
            if not field.startswith('a_'):
                continue

            # Get assignment ID
            try:
                key = int(field[len('a_'):])
            except ValueError:
                return HttpResponseBadRequest('Invalid input field(s)')

            # Get assignment from ID
            assignment = Assignment.objects.filter(pk=key)
            if len(assignment) < 1:
                return HttpResponseBadRequest('Invalid input field(s)')

            # Validate assignment's school
            if(assignment[0].school != school_account.registration):
                return HttpResponseForbidden('Not an assignment to this school')

            assignment.update(delegate_name=value)

        return HttpResponseRedirect('assignments/updated')
    else:
        my_assignments = Assignment.objects.filter(school=school_account.registration)

        return render_to_response('assignments.html', {
            'school' : school_account,
            'assignments' : my_assignments,
        }, context_instance=RequestContext(request))
