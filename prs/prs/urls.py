from django.conf.urls import include, url
from django.contrib import admin

import movie

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^log/', include('evidenceCollector.urls')),
    url(r'^', include('movie.urls')),
]
