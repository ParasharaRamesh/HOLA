from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
 
urlpatterns = [
    # (?P<pk>[0-9]+)
    url(r'^carstatus/$', CarStatusAPI.as_view(), name='getCarStatus'),
    url(r'^canceltrip/$', CancelTripAPI.as_view(), name='cancelTrip'),
    url(r'^cardetails/$', CarDetailsAPI.as_view(), name='getCarDetails'),
    url(r'^completetrip/$', CompleteTripAPI.as_view(), name='completeTrip'),
    url(r'^scheduletrip/$', ScheduleTripAPI.as_view(), name='scheduleTrip'),
    url(r'^carsinlocation/$', CarsInLocationAPI.as_view(), name='getCarsInLocation'),
    url(r'^fareestimate/$', FareEstimateAPI.as_view(), name='getFareEstimates'),
]
