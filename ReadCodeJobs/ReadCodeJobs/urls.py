from django.conf.urls import patterns, include, url
from data import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ReadCodeJobs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^Data/MedCodes/$', MedCodes.as_view(), name='MedCodes'),
)
