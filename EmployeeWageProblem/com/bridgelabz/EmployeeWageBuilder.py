import random

# Constants and Variables
IS_FULL_TIME = 2
IS_PART_TIME = 1
EMP_RATE_PER_HOUR = 20
MAX_WORKING_DAYS = 20
MAX_MONTHLY_HOURS = 100
dayCount = 0
totalEmployeeWage = 0
totalWorkHours = 0


# Determines work hours
def calculateWorkhours(attendanceStatus):
    switcher = {
        IS_FULL_TIME: 8,
        IS_PART_TIME: 4,
    }
    return switcher.get(attendanceStatus, 0)


# Calculates monthly wages
while dayCount < MAX_WORKING_DAYS and totalWorkHours <= MAX_MONTHLY_HOURS:
    attendanceStatus = random.randint(0, 2)  # checks whether employee is present
    workHours = calculateWorkhours(attendanceStatus)  # gets calculated work hours
    dayCount += 1
    totalWorkHours += workHours
    print("Day number: ", dayCount, "  Emp Hr: ", workHours)

totalEmployeeWage = totalWorkHours * EMP_RATE_PER_HOUR
print("Employee wage for the month is: ", totalEmployeeWage)
