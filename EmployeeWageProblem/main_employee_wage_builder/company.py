
class Company:

    def __init__(self , name , max_working_days , max_monthly_hrs , emp_rate_per_hr , total_employee_wage):
        """ creates and returns instance of company with given name , maximum working days , maximum monthly hours
        and rate per hour """
        self.name = name
        self.max_working_days = max_working_days
        self.max_monthly_hrs = max_monthly_hrs
        self.emp_rate_per_hr = emp_rate_per_hr
        self.total_employee_wage = total_employee_wage

