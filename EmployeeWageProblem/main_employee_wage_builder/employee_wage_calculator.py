import random
from EmployeeWageProblem.main_employee_wage_builder.compute_wage_interface import ComputeWageInterface
from EmployeeWageProblem.main_employee_wage_builder.company import Company

IS_FULL_TIME = 2
IS_PART_TIME = 1
FULL_DAY_HOURS = 8
PART_TIME_HOURS = 4

class Employee_Wage_Calculator(ComputeWageInterface):
    companies = []
    company_wage_dictionary = {}

    def add_company_details(self , name , max_working_days , max_monthly_hrs , emp_rate_per_hr , total_employee_wage):
        """ appends new company object to list and returns the object """
        company = Company(name , max_working_days = max_working_days , max_monthly_hrs = max_monthly_hrs, emp_rate_per_hr = emp_rate_per_hr , total_employee_wage =total_employee_wage)
        Employee_Wage_Calculator.companies.append(company)
        return company

    def get_total_wage(self , company):
        """ returns total wage for each company passed """
        return Employee_Wage_Calculator.company_wage_dictionary.get(company.name)


    def calculate_employee_wage(self , company):
        """ calculates and prints total employee wage for a given company based on maximum working days and hours """
        global IS_FULL_TIME , IS_PART_TIME , FULL_DAY_HOURS , PART_TIME_HOURS
        day_count = 0
        total_work_hours = 0
        while day_count < company.max_working_days and total_work_hours < company.max_monthly_hrs:
            attendance_status = random.randint(0, 2)
            work_hours = FULL_DAY_HOURS if attendance_status == IS_FULL_TIME else PART_TIME_HOURS if attendance_status == IS_PART_TIME else 0
            day_count += 1
            total_work_hours += work_hours
            print("Wage for day " , day_count , "is: " ,work_hours * company.emp_rate_per_hr)

        company.total_employee_wage = total_work_hours * company.emp_rate_per_hr
        Employee_Wage_Calculator.company_wage_dictionary[company.name] = company.total_employee_wage


def main():
    wage_builder = Employee_Wage_Calculator()
    wage_builder.add_company_details("Dmart", 20, 100, 20, 0)
    wage_builder.add_company_details("Reliance", 30, 80, 30, 0)
    wage_builder.add_company_details("Westside", 15, 90, 30, 0)
    for company in Employee_Wage_Calculator.companies:
        wage_builder.calculate_employee_wage(company)
    print(Employee_Wage_Calculator.company_wage_dictionary)
if __name__ == "__main__":
    main()
