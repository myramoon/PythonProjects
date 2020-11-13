import random


class Company:
    IS_FULL_TIME = 2
    IS_PART_TIME = 1
    FULL_DAY_HOURS = 8
    PART_TIME_HOURS = 4

    def __init__(self , name , max_working_days , max_monthly_hrs , emp_rate_per_hr):
        """ creates and returns instance of company with given name , maximum working days , maximum monthly hours
        and rate per hour """
        self.name = name
        self.max_working_days = max_working_days
        self.max_monthly_hrs = max_monthly_hrs
        self.emp_rate_per_hr = emp_rate_per_hr

    def calculate_work_hours(self , attendance_status):
        """ determines working hours for the day on the basis of attendance and returns work hours """
        work_hour_setter = {
            self.IS_FULL_TIME: self.FULL_DAY_HOURS,
            self.IS_PART_TIME: self.PART_TIME_HOURS,
        }
        return work_hour_setter.get(attendance_status, 0)

    def calculate_employee_wage(self):
        """ calculates and prints total employee wage for a given company based on maximum working days and hours """
        day_count = 0
        total_work_hours = 0
        while day_count < self.max_working_days and total_work_hours < self.max_monthly_hrs:
            attendance_status = random.randint(0, 2)
            work_hours = self.calculate_work_hours(attendance_status)
            day_count += 1
            total_work_hours += work_hours
            print("Wage for day " , day_count , "is: " ,work_hours * self.emp_rate_per_hr)

        self.total_employee_wage = total_work_hours * self.emp_rate_per_hr
        print("Total wage of the company " , self.name , " for the month is ", self.total_employee_wage)
