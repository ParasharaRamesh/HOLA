import os
import enum
import sys
curr_path=os.path.dirname(__file__)
# print("currpath is ",curr_path)
lib_path = os.path.abspath(os.path.join(curr_path, '..','trip'))
print("in conpletetriresult lib path is ",lib_path)
sys.path.append(lib_path)
import Trip

class CompleteTripTransactionStatus(enum.Enum):
        UNKNOWN=1
        SUCCESS=2
        PAYMENT_ERROR=3
        DATABASE_ERROR=4
        TRIP_ID_NOT_FOUND=5    

class CompleteTripTransactionResult:
    def _init__(self,completeTripTransactionStatus,trip):
        if type(completeTripTransactionStatus)!=int:
            Exception("completeTripTransactionStatus must be an integer between 1-5")
        if completeTripTransactionStatus<1 or completeTripTransactionStatus>5:
            Exception("completeTripTransactionStatus must be between 1 and 5")
        self._completeTripTransactionStatus=str(CompleteTripTransactionStatus(completeTripTransactionStatus))[31:]

        if isinstance(trip,Trip.Trip) == True:
            self._trip=trip
        else:
            Exception('The rvalue is of not of trip type!')

    #getters and setters
    @property
    def completeTripTransactionStatus(self):
        return self._completeTripTransactionStatus
    
    @completeTripTransactionStatus.setter
    def completeTripTransactionStatus(self,completeTripTransactionStatus):
        if type(completeTripTransactionStatus)!=int:
            Exception("completeTripTransactionStatus must be an integer between 1-5")
        if completeTripTransactionStatus<1 or completeTripTransactionStatus>5:
            Exception("completeTripTransactionStatus must be between 1 and 5")
        self._completeTripTransactionStatus=str(CompleteTripTransactionStatus(completeTripTransactionStatus))[31:]

    @property
    def trip(self):
        return self._trip

    @trip.setter
    def trip(self,trip):
        if isinstance(trip,Trip.Trip) == True:
            self._trip=trip
        else:
            Exception('The rvalue is of not of trip type!')  


