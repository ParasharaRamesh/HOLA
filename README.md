
Sequence of API calls:

//still have to write






API Definition/ Pseudocode:

1.CarDetails API:
    Input :{"carId":...}
    Output:{"car":CarDT,"carDriver":CarDriverDT}
    Pseudocode:
        .check input json ka all fields and check for NULL object passed and return appropriate error code.
        .use CarId and query the CarDetailsTable to get the carType,carModel,CarLicense for creating the CarDT in the response object
        .follow driverId and go to driverDetailsTable to get the name,phone&avg_ratings for creating the CarDriverDT
        .for getting the feedbacks go to the triptable and search for specific driverId and sort by triprating and get the top5 feedbacks and store it in a list
            and use that list to fill the CarDriverDT in the responseDT
        .Note:if driver has no feedbacks yet we return empty list.

2.CarStatus API:
    Input :{"carId":...}
    Output:{"carStatus":CarStatusDT}
    Pseudocode:
        .check input json ka all fields and check for NULL object passed and return appropriate error code.
        .use Carid to get caravailability and geolocation from CarStatusTable

3.CarsInLocation API:
    Input:{"geoLocation":geoLocationDT}//users current geolocation
    Output:{"carStatuses":List of CarStatusDT}
    Pseudocode:
        .check input json ka all fields and check for NULL object passed and return appropriate error code.
        .Return list of cars that are CarStatus.CarAvailability.CAR_AVAILABLE &
                       within GlobalConstants.SEARCH_RADIUS(inclusive) from CarStatusTable.
        .Use GlobalConstants.HAVER_SINE_FORMULA to calculate the distance between two lat/longs.
        .Note:there is no GlobalConstants file as of now , but if you want to create it you can refer datatypes.loction.GeoUtils for HAVER_SINE_FORMULA,also have a threshold for FareEstimate discount


4.FareEstimates API:
    Input:{"customerId":...,"sourceLocation":geoLocationDT,"destinationLocation":geoLocationDT}
    Output:{"estimatesForCarTypes":list of estimatesForCarType DT}
    Pseudocode:
        .check input json ka all fields and check for NULL object passed and return appropriate error code.
        .use datatypes.loction.GeoUtils.getDistanceBetweenLocationInKms to get the distance between source and destination Location.
        .create a List<estimatesForCarType DT> for each type of car:ie hatch_back,sedan etc
        .use the customerId to go to CustomerDetails table and get the streakfor past7 days let it be k.
        .if k > GlobalConstants.threshold(not yet created!) then assign a discount of say x%
        .for each estimatesForCarTypeDT assign the tripPrice as the distance*perkmcost for that carType
        .for each estimatesForCarTypeDT assign the discountedTripPrice as tripPrice(1-(x/100))
        .return this list of estimatesForCarTypes
        .Note : for the perkmcost of each cartype have a dictionary<cartype,perkmcost> in global constants !(to be created)


5.ScheduleTrip API:
    Input:{"carType":..,"tripPrice":..,sourceLocation":geoLocationDT,"destinationLocation":geoLocationDT}//this is the ScheduleTripTransactionInput DT
    Output:{"scheduleTripStatus":..,"trip":TripDT}//this is the ScheduleTripTransactionResult DT
    Pseudocode:
        .check input json ka all fields and check for NULL object passed and return appropriate error code.
        try:
            . Get cars of this specific carType near the sourceLocation that are CarStatus.CarAvailability.AVAILABLE
             sorted by distance from the sourceLocation from carstatustable
        catch:
            . set ScheduleTripStatus to scheduletriptransactionstatus.DATABASE_ERROR and trip to None and return to customer

        .if cars not AVAILABLE from the sql query:
            .set ScheduleTripStatus to scheduletriptransactionstatus.NO_CARS_AVAILABLE and trip to None and return to customer
        .else:
            .choose the first car and do the following:
                .Update the status of this selected car to CAR_ON_TRIP in the CarStatusTable.(we will only be using UNKNOWN,CAR_AVAILABLE,CAR_ON_TRIP as the CarStatuses others can be used in "FUTURE WORK")
                .Create a Trip entry and set paymentMode to UNKNKOWN(we will set in completeTrip API) & set tripStatus to TRIP_STATUS_SCHEDULED,set startTime to current time and set endTime to something like -1 which we will set in completetrip API
            .if both these DB transactions were succesful set the scheduletrip status to SUCCESSFULLY_BOOKED and return the json after setting the tripDT stuff

        .Note in client side if we get either one of the 2 errors the customer is sent back to the screen which has the carsinlocation api being called.


6.CancelTrip API://called on the case if the user presses the cancel button after the driver details are shown
    Input:{"tripId":..}
    Output:{"result":success/failure}//either way go back to 
    Pseudocode:
        .use the tripID and check the status 
        .if status ==TRIP_STATUS_SCHEDULED:
            that means that this trip was scheduled before and we have to cancel it so set the status to TRIP_STATUS_CANCELLED
            return the success/failure of this operation and take the user back to the getCarsInLocation screen.


7.CompleteTrip API:
    Input:{"tripId":..,"finishLocation":geolocationDT,"paymentMode":..,"rating":..,"feedback":..}//completeTripTransactionInput  DT along with extra stuff..>therefore maybe change the completeTripTransactionInputDT itself to accomodate this????(see later)
    Output:{"completeTripTransactionStatus":..,"trip":TripDT}//completeTripTransactionResultDT
    Pseudocode:
        .check input json ka all fields and check for NULL object passed and return appropriate error code.

//steps to be filled!!! by maru or para //remember to take the average rating for that driver and update in the driver table also as an additional step!!

        .calculateCurrentStreak_for_customer() and update the streak count of the user in the customer table:
            .NOTE ADD A FIELD to the customer table which includes last ride taken on what date.
            .check if current date falls within that week the last riden date belongs to then increment streak and update the lastriden date
            .else initialize the streak to 1(i.e. new streak) and set the last riden date













General Notes:


.All the Datatypes are in the folder holaserver.datatypes

.All the models/tables are in the models.py folder

.To run test cases use the command:
    python manage.py test path.to.testClass

.If making changes to the models.py then:
    make sure to add new tables in the admin.py file
    python manage.py makemigrations holaserver
    python manage.py migrate
    then test CRUD using the admin gui:
        1.runserver and go to localhost:port/admin
        2.test the CRUD on all tables
        3.then do python manage.py flush to remove all the temporary instances created

.If making changes to datatypes then:
    make sure to update/create a corresponding serializer class as well in the serializers folder
    make sure to write a test case in the tests.datatypes folder and run all the tests by saying
        python manage.py test tests.datatypes

.To run server
    python manage.py runserver

To createsuperuser
    python manage.py createsuperuser
