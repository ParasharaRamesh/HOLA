#constant for showing the carsinlocation around a specific lat,long point
import os
import sys
curr_path=os.path.dirname(__file__)
lib_path =os.path.abspath(os.path.join(curr_path,'datatypes','location'))
sys.path.append(lib_path)
from GeoUtils import GeoUtils

SEARCH_RADIUS = 3

#use this formula for carsinlocation api
def isNearLocation(inputLat,inputLong,DBLat,DBLong):
    geoUtils = GeoUtils()
    distance=geoUtils.haversine(lat1=inputLat,lon1=inputLong,lat2=DBLat,lon2=DBLong)
    # print("Distance in isNearLocation is ==>",distance)
    if distance<=SEARCH_RADIUS:
        return True
    return False


#use this for getting the perkm cost of each car while calculating fareestimates
fare_estimates = {"UNKNOWN":0.0,"CAR_TYPE_HATCHBACK":7.0,"CAR_TYPE_SEDAN":15.0,"CAR_TYPE_MINIVAN":10.0,"CAR_TYPE_AUTO":6.0}
#use this for assigning discount to streak based on these values
STREAK_THRESHOLD = {"NORMAL":4,"SPECIAL":7,"MASTER":14,"GOD":21}