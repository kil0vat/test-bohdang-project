from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ticket1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
<<<<<<< HEAD
	url(r'^$', include('contact_info.urls')),
=======

>>>>>>> 5d85341923385aafa51653d558122ef954454e95
    url(r'^admin/', include(admin.site.urls)),
)
