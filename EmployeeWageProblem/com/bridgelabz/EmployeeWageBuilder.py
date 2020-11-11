import random

#Constants and Variables
IS_FULL_TIME = 2
IS_PART_TIME = 1
EMP_RATE_PER_HOUR = 20
MAX_WORKING_DAYS = 20
count = 0
totalEmployeeWage = 0

#Determines work hours
def calculateWorkhours(attendanceStatus):
    switcher = {
        IS_FULL_TIME: 8,
        IS_PART_TIME: 4,
    }
    return switcher.get(attendanceStatus, 0)

#Calculates monthly wages
while count < MAX_WORKING_DAYS:
    attendanceStatus = random.randint(0, 2)  # checks whether employee is present
    workHours = calculateWorkhours(attendanceStatus)  # gets calculated work hours
    employeeWage = workHours * EMP_RATE_PER_HOUR  # calculate wages
    totalEmployeeWage += employeeWage
    count += 1

print("Employee wage for the month is: ", totalEmployeeWage)
