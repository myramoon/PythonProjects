import random

IS_FULL_TIME = 2
IS_PART_TIME = 1
EMP_RATE_PER_HOUR = 20
attendanceStatus = random.randint(0,2)   #checks whether employee is present
def calculateWorkhours(attendanceStatus):
    switcher = {
        IS_FULL_TIME: 8 ,
        IS_PART_TIME: 4 ,
    }
    return switcher.get(attendanceStatus , 0)

workHours = calculateWorkhours(attendanceStatus) #gets calculated work hours
employeeWage = workHours * EMP_RATE_PER_HOUR   #calculate wages
print ("Employee wage for the day is: " , employeeWage)




