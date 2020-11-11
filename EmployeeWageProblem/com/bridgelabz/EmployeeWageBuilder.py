import random

IS_FULL_TIME = 1
attendanceStatus = random.randint(0,1)   #checks whether employee is present
if attendanceStatus == IS_FULL_TIME:
    print("Employee is present")
else:
    print("Employee is absent")



