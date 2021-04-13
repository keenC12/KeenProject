from datetime import datetime
from datetime import time 

startTime=time(6, 52)
print("Start time is \n{} am".format(startTime))


easyPace=(2*(8*60)+15)
fastPace=(3*(7*60)+12)

timeElapsed=easyPace+fastPace

minutes=timeElapsed//60 #time elapsed from seconds to mins
seconds=timeElapsed%60 #remainder seconds

endHour=6
endMinutes=52+minutes

if endMinutes>=60:
    endHour=endHour+1
    endMinutes=endMinutes-60

    print("Time to take breakfast: ")
    print(endHour, ":",endMinutes, ":", seconds,"am")
