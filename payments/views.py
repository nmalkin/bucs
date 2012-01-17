from django.shortcuts import render_to_response
from django.template import RequestContext

from auth.decorators import *
from payments.models import Due, Payment

@school_from_short_name
@logged_in_as_school
def payments(request, school):
    dues = Due.objects.filter(school=school.registration)
    payments = Payment.objects.filter(school=school.registration)
    
    total = 0
    for due in dues:
        total += due.amount
    for payment in payments:
        total -= payment.amount

    return render_to_response('payments.html', {
        'school': school,
        'dues': dues,
        'payments': payments,
        'total': total
    }, context_instance=RequestContext(request))
