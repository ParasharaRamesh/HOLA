from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
 
urlpatterns = [
    # (?P<pk>[0-9]+)
    url(r'^carstatus/$', CarStatus.as_view(), name='getCarStatus'),
    url(r'^canceltrip/$', CancelTrip.as_view(), name='cancelTrip'),
    url(r'^cardetails/$', CarDetails.as_view(), name='getCarDetails'),
    url(r'^completetrip/$', CompleteTrip.as_view(), name='completeTrip'),
    url(r'^scheduletrip/$', ScheduleTrip.as_view(), name='scheduleTrip'),
    url(r'^carsinlocation/$', CarsInLocation.as_view(), name='getCarsInLocation'),
    url(r'^fareestimate/$', FareEstimate.as_view(), name='getFareEstimates'),
]
