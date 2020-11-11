import random

IS_FULL_TIME = 2
IS_PART_TIME = 1
EMP_RATE_PER_HOUR = 20
attendanceStatus = random.randint(0,2)   #checks whether employee is present
if attendanceStatus == IS_FULL_TIME:
    workHours = 8
elif attendanceStatus == IS_PART_TIME:
    workHours = 4
else:
    workHours = 0
employeeWage = workHours * EMP_RATE_PER_HOUR   #calculate wages
print ("Employee wage for the day is: " , employeeWage)




