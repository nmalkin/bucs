from django.shortcuts import render_to_response
from django.template import RequestContext

from auth.accounts import SchoolAccount
from auth.decorators import *

@school_from_short_name
@logged_in_as_school
def index(request, school):
    """
    Show the default page for the school section.
    """
    return render_to_response('school/index.html', {
        'school' : school.registration.school,
        'school_code' : school.short_name,
    }, context_instance=RequestContext(request))


