from django.conf.urls.defaults import *

urlpatterns = patterns('registration.views',
    url(r'^form$', 'form', name='form'),
    url(r'^submit$', 'submit'),
)