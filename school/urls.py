from django.conf.urls.defaults import *
#from auth.views import login

urlpatterns = patterns('',
    url(r'^(\w+)/?$', 'school.views.index', name='school-index'),
    url(r'^(\w+)/login/?', 'auth.views.school_login', name='school-login'),
    url(r'^(\w+)/payments/?', 'payments.views.payments'),
    url(r'^(\w+)/registration/?', 'registration.views.submitted_info'),
    url(r'^(\w+)/rankings/crisis/?', 'rankings.views.crisis_rankings'),
    url(r'', 'auth.views.school_login_generic')
)
