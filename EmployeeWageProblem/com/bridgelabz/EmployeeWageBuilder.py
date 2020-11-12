import random

class EmployeeWage:
    EMP_RATE_PER_HOUR = 20
    MAX_WORKING_DAYS = 20
    MAX_MONTHLY_HOURS = 100

    # Determines work hours
    def calculateWorkhours(self , attendanceStatus):

        IS_FULL_TIME = 2
        IS_PART_TIME = 1
        FULL_DAY_HOURS = 8
        PART_TIME_HOURS = 4
        switcher = {
            IS_FULL_TIME: FULL_DAY_HOURS,
            IS_PART_TIME: PART_TIME_HOURS,
        }
        return switcher.get(attendanceStatus, 0)

    def calculateEmployeeWage(self):

        dayCount = 0
        totalWorkHours = 0
        while dayCount < self.MAX_WORKING_DAYS and totalWorkHours < self.MAX_MONTHLY_HOURS:  # Calculating work hours for month based on conditions
            attendanceStatus = random.randint(0, 2)  # gets attendance status of employee
            workHours = self.calculateWorkhours(attendanceStatus)  # gets calculated work hours
            dayCount += 1
            totalWorkHours += workHours

        totalEmployeeWage = totalWorkHours * self.EMP_RATE_PER_HOUR
        print("Total wage of the month is ", totalEmployeeWage)


employeeWage = EmployeeWage()
employeeWage.calculateEmployeeWage()
