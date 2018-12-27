from django.urls import re_path, include
from rest import views

urlpatterns = [
    re_path('^carsinlocation/$', views.CarsInLocationAPI.as_view()),
    re_path('^fareestimates/$', views.FareEstimatesAPI.as_view()),
    re_path('^scheduletrip/$', views.ScheduleTripAPI.as_view()),
    re_path('^cardetails/$', views.CarDetailsAPI.as_view()),
    re_path('^carstatus/$', views.CarStatusAPI.as_view()),
    re_path('^completetrip/$', views.CompleteTripAPI.as_view()),
    re_path('^ratetrip/$', views.RateTripAPI.as_view()),
    re_path(r'^auth/', include('rest_auth.urls')),
    re_path('auth/registration/', include('rest_auth.registration.urls')),
]
