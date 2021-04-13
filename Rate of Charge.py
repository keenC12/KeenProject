import time #import time

print("This will calculate the payment for the babysitter ")

regularRate=float(2.50)
discountedRate=float(1.75)

#To convert hours to 24hr format
def militaryTime(TimeHour, clock ): 
    if clock =="PM":    
        if TimeHour == 12:
            return TimeHour
        else:
            TimeHour = TimeHour + 12
            return TimeHour
    elif clock == "AM":
        return TimeHour

#to convert hour to minutes and have the overall minutes
def hourToMinutes(hour, minutes):
    cvt_time = (hour*60) + minutes
    return cvt_time



#Ask users input for Hour:Minutes and AM or PM
startTimeHour, startTimeMinutes=(int(startTimeHour) for startTimeHour in input("\nInput babysitter starting time: ").split(":"))    
startClock=input("AM or PM: ")
endTimeHour, endTimeMinutes=(int(endTimeHour) for endTimeHour in input("Input babysitter end time: ").split(":"))
endClock=input("AM or PM: ")

#Initializa variables for testing here
#startTimeHour = 9
#startTimeMinutes = 20
#startClock = 'AM'

#endTimeHour = 10
#endTimeMinutes = 40
#endClock = 'PM'

#print(startTimeHour)
#print(endTimeHour)


#To catch invalid time input
if startTimeHour >12 or endTimeHour > 12:
    print("Error!! Enter time in 12hr format") 
    if startTimeHour <= 0 or endTimeHour <= 0:
            print("Error!!")
elif startTimeMinutes > 59 or endTimeMinutes > 59:
    print("Error!! Enter minutes less than 60")
    if startTimeHour <= 0 or endTimeHour <= 0:
        print("Error!!")



#Value after conversion to 24hr format   
newStartTimeHour = militaryTime(startTimeHour, startClock)
newEndTimeHour = militaryTime(endTimeHour, endClock)

#Value overall minutes
convertedStartTime = hourToMinutes(newStartTimeHour, startTimeMinutes)
convertedEndTime = hourToMinutes(newEndTimeHour, endTimeMinutes)

#rates for payment before and after 9:00 PM
rateForPass9 = (convertedEndTime-convertedStartTime)*(discountedRate/60)
rateForBefore9 = (convertedEndTime-convertedStartTime)*(regularRate/60)

#Checking of output
#print(convertedStartTimePass9)
#print(convertedEndTimePass9)
#print(rateForPass9)
#print(rateForBefore9)
#print(total_Bill)

#determining on what the rate is based on time frame
countDown = [3,2,1]
print("\nCalculating...")
if newStartTimeHour >= 21 and newEndTimeHour >= 21:
    for i in countDown:
        time.sleep(1)
        print(i,"...")
    time.sleep(1)    
    print("\nBill is $ %.2f"%rateForPass9)
elif newStartTimeHour < 21 and newEndTimeHour < 21:
    for i in countDown:
        time.sleep(1)
        print(i,"...")
    time.sleep(1) 
    print("\nBill is $ %.2f"%rateForBefore9)
elif newStartTimeHour < 21 and newEndTimeHour >= 21:
    timePass9 = convertedEndTime - (21*60)
    extraRate = timePass9*(discountedRate/60)
    noExtraRate = ((convertedEndTime-timePass9)-convertedStartTime)*(regularRate/60)
    total_Bill = noExtraRate + extraRate
    for i in countDown:
        time.sleep(1)
        print(i,"...")
    time.sleep(1)
    print ("\nBill is $ %.2f"%total_Bill)
    
