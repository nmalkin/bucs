from django import forms
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

from auth.accounts import SchoolAccount
from auth.decorators import school_from_short_name

def do_logout(request):
    logout(request)
    request.session.clear()
    return HttpResponseRedirect('/logout_success')

def logout_success(request):
    return render_to_response('logout.html', context_instance=RequestContext(request))


# The login form displayed on the school-specific page.
# Since we know the school, the only thing we ask for is the password.
class SchoolLoginForm(forms.Form):
    password = forms.CharField(required=True, widget=forms.PasswordInput)
 

def school_login_generic(request):
    if request.user.is_authenticated():
        logged_in_school = request.session.get('school', False)
        if logged_in_school:
            school_short_name = SchoolAccount.objects.get(pk=logged_in_school).short_name
            return HttpResponseRedirect('/school/%s' % school_short_name)
        else: # not logged in as this school
            return HttpResponseForbidden('You are not a school. What are you doing here?')
    else:
        if request.method == 'POST':
            school = request.POST['school']
            return school_login(request, school)
        else:
            return render_to_response('login.html', {
            }, context_instance=RequestContext(request))

@school_from_short_name
def school_login(request, school):
    """
    Attempts login as the given school.
    If no data posted, shows login form.
    If data is posted, attempts validation and authentication.
        On success, redirects to school's default page (/school/<school>).
        On failure, redisplays the form with errors.
    """
    if request.user.is_authenticated(): # you're already logged in. what are you doing here?
        return HttpResponseRedirect('/school/%s' % school.short_name) #TODO: maybe use a reverse for more automation?
    
    if request.method == 'POST':
        form = SchoolLoginForm(request.POST) 
        if form.is_valid(): # clean submitted form
            # attempt authentication
            user = authenticate(username=school.user.username, password=form.cleaned_data['password'])
            
            if user is not None and user.is_active: # login successful!
                login(request, user) # log the user in
                request.session.set_expiry(0) # log them out when they close the browser; this also happens by default with our settings
                request.session['school'] = school.pk # remember that this school is logged in
                # redirect to success page
                #return HttpResponseRedirect(reverse('school-index'))
                return HttpResponseRedirect('/school/%s' % school.short_name) #TODO: maybe use a reverse for more automation?
            else:
                login_failed = True
        else:
            login_failed = True
    else:
        form = SchoolLoginForm()
        login_failed = False

    return render_to_response('school/login-school.html', {
        'form': form, 
        'school': school.registration.school,
        'short_name': school.short_name,
        'login_failed' : login_failed
    }, context_instance=RequestContext(request))

