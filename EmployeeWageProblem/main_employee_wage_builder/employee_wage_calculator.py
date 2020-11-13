import random


class Employee_Wage_Calculator:
    """ calculates and returns total wage for each company passed """
    IS_FULL_TIME = 2
    IS_PART_TIME = 1
    FULL_DAY_HOURS = 8
    PART_TIME_HOURS = 4

    def calculate_work_hours(self , attendance_status):
        """ determines working hours for the day on the basis of attendance and returns work hours """
        work_hour_setter = {
            self.IS_FULL_TIME: self.FULL_DAY_HOURS,
            self.IS_PART_TIME: self.PART_TIME_HOURS,
        }
        return work_hour_setter.get(attendance_status, 0)

    def calculate_employee_wage(self , company):
        """ calculates and prints total employee wage for a given company based on maximum working days and hours """
        day_count = 0
        total_work_hours = 0
        while day_count < company.max_working_days and total_work_hours < company.max_monthly_hrs:
            attendance_status = random.randint(0, 2)
            work_hours = self.calculate_work_hours(attendance_status)
            day_count += 1
            total_work_hours += work_hours
            print("Wage for day " , day_count , "is: " ,work_hours * company.emp_rate_per_hr)

        company.total_employee_wage = total_work_hours * company.emp_rate_per_hr
        print("Total wage of the company " , company.name , " for the month is ", company.total_employee_wage)
