from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.forms import ModelForm
from django.shortcuts import render_to_response
from django.core.mail import send_mail

from registration.models import Registration
from auth.decorators import *

class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        exclude = ('registration_time',)

def form(request):
    form = RegistrationForm()
    return render_to_response('registration/form.html', {
        'form': form,
    }, context_instance=RequestContext(request))

def submit(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            
            # (try) sending confirmation email
            bucs_address = 'info@browncrisis.org'
            address = form.cleaned_data['email']
            message = 'Dear %s,\n\n' \
                'This is an automatic message to let you know ' \
                'that your registration for the Brown University Crisis Simulation was successfully submitted. ' \
                'We will be in touch shortly to provide you with further information.\n\n' \
                'Thank you, and we look forward to seeing you in March!' % form.cleaned_data['contact_person']
            send_mail('BUCS Registration', message, bucs_address, [address], fail_silently=True)

            # now notify us about new registration
            message = 'A new registration has been received from %s. Please take action promptly.' % form.cleaned_data['school']
            send_mail('New BUCS Registration', message, bucs_address, [bucs_address], fail_silently=True)
            
            return render_to_response('registration/success.html', context_instance=RequestContext(request))
        else:
            return render_to_response('registration/form.html', {
                'form': form,
            }, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect(reverse('form'))
 
@school_from_short_name
@logged_in_as_school
def submitted_info(request, school):
    registration = Registration.objects.get(school=school)
    return render_to_response('school/registration-info.html', {
        'school': school,
        'registration': registration,
    }, context_instance=RequestContext(request))
