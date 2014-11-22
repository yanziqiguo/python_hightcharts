from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import hello, current_datetime

urlpatterns = patterns('',
	('^hello/$', hello),
	('^time/$', current_datetime),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
