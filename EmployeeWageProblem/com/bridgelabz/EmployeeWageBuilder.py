import random

IS_FULL_TIME = 1
EMP_RATE_PER_HOUR = 20
attendanceStatus = random.randint(0,1)   #checks whether employee is present
if attendanceStatus == IS_FULL_TIME:
    workHours = 8
else:
    workHours = 0
employeeWage = workHours * EMP_RATE_PER_HOUR   #calculate wages
print ("Employee wage for the day is: " , employeeWage)




