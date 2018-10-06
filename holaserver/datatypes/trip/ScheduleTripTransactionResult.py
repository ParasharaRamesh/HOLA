import os
import enum
import sys
curr_path=os.path.dirname(__file__)
# print("currpath is ",curr_path)
#lib_path = os.path.abspath(os.path.join(curr_path, '..','..'))
# print("in trip lib path is ",lib_path)
#sys.path.append(lib_path)
from trip.Trip import Trip

class ScheduleTripTransactionStatus(enum.Enum):
        UNKNOWN=1
        SUCCESSFULLY_BOOKED=2#only gonna use this
        PRICE_CHANGED=3
        NO_CARS_AVAILABLE=4#gonna use this
        DATABASE_ERROR=5#gonna use this

class ScheduleTripTransactionResult:
    def __init__(self,scheduleTripTransactionStatus,trip):
        if type(scheduleTripTransactionStatus)!=int:
            Exception("scheduleTripTransactionStatus must be an integer between 1-5")
        if scheduleTripTransactionStatus<1 or scheduleTripTransactionStatus>5:
            Exception("scheduleTripTransactionStatus must be between 1 and 5")
        self._scheduleTripTransactionStatus=str(ScheduleTripTransactionStatus(scheduleTripTransactionStatus))[30:]

        if isinstance(trip,Trip) == True:
            self._trip=trip
        else:
            Exception('The rvalue is of not of trip type!')

    def __str__(self):
        return '%s(%s)' % (type(self).__name__,', '.join('%s=%s' % item for item in vars(self).items()))

   #getters and setters
    @property
    def scheduleTripTransactionStatus(self):
        return self._scheduleTripTransactionStatus
    
    @scheduleTripTransactionStatus.setter
    def scheduleTripTransactionStatus(self,scheduleTripTransactionStatus):
        if type(scheduleTripTransactionStatus)!=int:
            Exception("scheduleTripTransactionStatus must be an integer between 1-5")
        if scheduleTripTransactionStatus<1 or scheduleTripTransactionStatus>5:
            Exception("scheduleTripTransactionStatus must be between 1 and 5")
        self._scheduleTripTransactionStatus=str(ScheduleTripTransactionStatus(scheduleTripTransactionStatus))[30:]

    @property
    def trip(self):
        return self._trip

    @trip.setter
    def trip(self,trip):
        if isinstance(trip,Trip) == True:
            self._trip=trip
        else:
            Exception('The rvalue is of not of trip type!')  


