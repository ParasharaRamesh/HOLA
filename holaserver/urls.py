from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
 
urlpatterns = [
    # (?P<pk>[0-9]+)
    url(r'^carstatus/$', CarStatus.as_view(), name='getCarStatus'),
    url(r'^canceltrip/$', CancelTrip.as_view(), name='cancelTrip'),
]
