from django import forms
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse

from auth.accounts import SchoolAccount


def school_from_short_name(function):
    """
    A decorator that, given a function that takes in a request and a school short-name,
    calls the function with the request and the SchoolAccount object that corresponds to that short-name.
    
    If the school short-name is invalid, returns a HttpResponseNotFound object with the appropriate message.
    """
    def wrapped(request, school_short_name):
        try:
            school = SchoolAccount.objects.get(short_name=school_short_name)
        except SchoolAccount.DoesNotExist:
            return HttpResponseNotFound('No school registered with given name (%s)' % school_short_name)
        except SchoolAccount.MultipleObjectsReturned:
            django.core.mail.mail_admins('School registration conflict', 'Multiple schools registered with name %s.' % school_short_name, fail_silently=True)
            return HttpResponseServerError('Internal error: multiple schools registered with given name')

        return function(request, school)

    return wrapped


def logged_in_as_school(function):
    """
    A decorator that, given a function that takes a request and a SchoolAccount,
    calls that function if and only if the user is logged in as that school.
    
    If the user is logged in as a different user, returns a HttpResponseForbidden with an appropriate message.
    If the user is not logged in, redirects them to the login page using a HttpResponseRedirect.
    """
    def wrapped(request, school):
        # okay, so we know the school they're trying to use. but are they logged in?
        if request.user.is_authenticated():
            # alright, they're logged in. but are they logged in as this school?
            logged_in_school = request.session.get('school', False)
            if logged_in_school and (logged_in_school == school.pk): # logged in as this school!
                return function(request, school) # call the decorated function
            else: # not logged in as this school
                return HttpResponseForbidden('You are not authorized to access this page.')
        else: # not authenticated
            #return HttpResponseRedirect(reverse('school-login', args=[request, school], urlconf=urlpatterns))
            return HttpResponseRedirect('/school/%s/login' % school.short_name)

    return wrapped

