import os
import sys
import json
curr_path=os.path.dirname(__file__)
lib_path = os.path.abspath(os.path.join(curr_path, '..',"location"))
sys.path.append(lib_path)
from GeoLocation import GeoLocation


#whenever deserializing a JSON to a Geolocation say
#geoLocationObj=json.dumps(obj,object_hook=decodeGeoLocation)
def decodeGeoLocation(o):
    if "latitude" in o and "longitude" in o:
        geoLocation = GeoLocation(0.0,0.0)#setting dummy values 
        if type(o["latitude"])==float and type(o["longitude"])==float:
            geoLocation.setLatitude(o["latitude"])
            geoLocation.setLongitude(o["longitude"])
        else:
            raise Exception("latitude and/or longitude is not of type float!")
        return geoLocation
    else:
        raise Exception("JSON doesnt have latitude and/or longitude")
    return o
