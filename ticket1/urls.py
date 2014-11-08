from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ticket1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', include('contact_info.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
