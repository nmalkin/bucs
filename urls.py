from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bucs.views.home', name='home'),
    # url(r'^bucs/', include('bucs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# patterns for the site's main pages. these should remain relatively static.
urlpatterns += patterns('django.views.generic.simple',
    url(r'^$', 'direct_to_template', {'template' : 'index.html'}),
    url(r'^about/?$', 'direct_to_template', {'template' : 'about.html'}),
    url(r'^committees/?$', 'direct_to_template', {'template' : 'committees.html'}),
    url(r'^logistics/?$', 'direct_to_template', {'template' : 'logistics.html'}),
    url(r'^registration$', 'direct_to_template', {'template' : 'registration.html'}),
)

urlpatterns += patterns('',
    url(r'^registration/$', 'django.views.generic.simple.redirect_to', {'url': '/registration'}),
    url(r'^registration/', include('registration.urls')),
)

urlpatterns += patterns('',
    # Redirect legacy URLs to static pages. In v2 of site (CodeIgniter era), they started with page/.
    url(r'^page/(?P<page>.*)', 'django.views.generic.simple.redirect_to', {'url': '/%(page)s', 'permanent': True}),
    url(r'^home/?$', 'django.views.generic.simple.redirect_to', {'url': '/', 'permanent': True}), # home page now index page
)

# schools
urlpatterns += patterns('',
    url(r'^school/', include('school.urls')),
)

# auth
urlpatterns += patterns('',
    url(r'^do_logout$', 'auth.views.do_logout'), #TODO: make this better!!!
    url(r'^logout$', 'auth.views.do_logout'), #TODO: make this better!!!
    url(r'^logout_success$', 'auth.views.logout_success'),
)

urlpatterns += staticfiles_urlpatterns()
