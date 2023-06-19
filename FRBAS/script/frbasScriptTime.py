import datetime
import pytz
from dateutil import tz

class FrbasScriptTimeDate:
    def __init__(self) -> None:
         self.time_zone     = pytz.timezone('Africa/Addis_Ababa')

#   Time Add zero if less than 10
    def timeAddZero(self,value):
        return f"0{value[0]}" if int(value[0]) < 10 else  value[0]

#   Time created from string value 
    def timeAjustValue(self,strtime):
        value = strtime.split(":")
        if int(value[0]) == 00: value[0] = 12
        value[0] = self.timeAddZero(value[0])
        return datetime.time(int(value[0]),int(value[1]),00)
    
#   Time Split to dictionary value
    def timeSplitValue(self,timeValue):
     return { "hour":f"0{timeValue.hour}", "minute":timeValue.minute}