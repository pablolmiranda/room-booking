from django.conf.urls import patterns, include, url

from django.contrib import admin
from homepage import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'room_scheduler.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^campus/', include('campus.urls', namespace="campus")),
    url(r'^booking/', include('booking.urls', namespace="booking")),
    url(r'^$', views.index , name="index")
)
