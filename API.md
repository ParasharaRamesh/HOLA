# Hola REST API Endpoints
Following are the supported REST API endpoint URIs and their corresponding HTTP methods, request and response formats.

#### 1. Car Details
`POST /hola/v1/cardetails`<br>
Input: Car ID
```json
{
  "carId": 1
}
```
Output: Car & Car Driver details
 ```json
{
    "car": {
        "carId": 1,
        "carType": 2,
        "carModel": "PUSHPAKA VIMANA HYBRID",
        "carLicense": "KA 41 M 1212"
    },
    "carDriver": {
        "driverId": 1,
        "name": "RAVANA",
        "phone": "9876543210"
    }
}
```
#### 2. Cars in Location
`POST /hola/v1/carsinlocation`<br>
Input: User's current location
```json
{
    "geoLocation": {
        "latitude": 12.918486,
        "longitude": 77.546386
    }
}
```
Output: Array of Car Statuses
```json
{
    "carStatuses": [
        {
            "carStatus": {
                "carId": 1,
                "geoLocation": {
                    "latitude": 12.913486,
                    "longitude": 77.543386
                },
                "carAvailability": "CAR_AVAILABLE"
            }
        },
        {
        "carStatus": {
            "carId": 2,
            "geoLocation": {
                "latitude": 12.913486,
                "longitude": 77.542386
            },
            "carAvailability": "CAR_AVAILABLE"
        }
    }]
}
```
#### 3. Car Status
`POST /hola/v1/carstatus`<br>
Input: car ID
```json
{
  "carId": 1
}
```
Output: Current location & availability of the car
```json
{
    "carStatus": {
        "carId": 1,
        "geoLocation": {
            "latitude": 77.998799,
            "longitude": 56.079089
        },
        "carAvailability": "CAR_AVAILABLE"
    }
}
```
#### 4. Complete Trip
`PUT /hola/v1/complete_trip`<br>
Input: Trip ID, finishing location & a confirmation of the payment mode
```json
{
    "tripId": 1,
    "finishLocation": {
        "latitude": 12.908486,
        "longitude": 77.536386
    },
    "paymentMode": 3
}
```
Output: Entire trip info as a confirmation
Note that endTimeInEpochs is now populated & tripStatus is updated to 4 (TRIP_STATUS_COMPLETED).
If the client doesn't receive this back or receives an error in completeTripStatus, it will retry the request.
```json
{
    "completeTripStatus": 2,
    "trip": {
        "tripId": 1,
        "carId": 1,
        "driverId": 1,
        "sourceLocation": {
            "latitude": 12.908486,
            "longitude": 77.536386
        },
        "destinationLocation": {
            "latitude": 12.908486,
            "longitude": 77.536386
        },
        "startTimeInEpochs": 1512152782,
        "endTimeInEpochs": 1512170782,
        "tripPrice": 129.00,
        "tripStatus": 4,
        "paymentMode": 2
    }
}
```
#### 5. Fare Estimates
`POST /hola/v1/fareestimates`<br>
Input: Source location & destination location
```json
{
    "sourceLocation": {
        "latitude": 12.908486,
        "longitude": 77.536386
    },
    "destinationLocation": {
        "latitude": 12.908486,
        "longitude": 77.536386
    }
}
```
Output: Array of EstimateForCarType
```json
{
    "estimatesForCarTypes": [
        {
            "estimateForCarType": {
                "carType": 1,
                "tripPrice": 129.00,
                "discountAmount": 0.00
            }
        },
        {
            "estimateForCarType": {
                "carType": 2,
                "tripPrice": 140.00,
                "discountAmount": 0.00
            }
        }, 
        {
            "estimateForCarType": {
                "carType": 3,
                "tripPrice": 181.00,
                "discountAmount": 0.00
            }
        }
    ]
}
```
#### 6. Schedule Trip
`POST /hola/v1/scheduletrip`<br>
Input: carType, tripPrice, start/end locations
```json
{
    "carType": 1,
    "tripPrice": 129.00,
    "sourceLocation": {
        "latitude": 12.908486,
        "longitude": 77.536386
    },
    "destinationLocation": {
        "latitude": 12.908486,
        "longitude": 77.536386
    }
}
```
Output: Whether we were able to find cars & if so the trip details
```json
{
    "scheduleTripStatus": 2,
    "trip": {
        "tripId": 1,
        "carId": 1,
        "driverId": 1,
        "sourceLocation": {
            "latitude": 12.908486,
            "longitude": 77.536386
        },
        "destinationLocation": {
            "latitude": 12.908486,
            "longitude": 77.536386
        },
        "startTimeInEpochs": 1512152782,
        "tripPrice": 129.00,
        "tripStatus": 2
    }
}
```
#### 7. Rate Trip
`POST /hola/v1/ratetrip`<br>
To be decided
