import json
from EmployeeWageProblem.main_employee_wage_builder.compute_wage_interface import ComputeWageInterface
from EmployeeWageProblem.main_employee_wage_builder.company import Company

FULL_DAY_HOURS = 8
PART_TIME_HOURS = 4

class EmployeeWageCalculator(ComputeWageInterface):
    companies = []
    company_wage_dictionary = {}

    def create_company(self , name , **company_data):
        """ appends new company object to list and returns the object """
        company = Company(name , **company_data)
        self.add_company_to_list(company)
        return company

    def add_company_to_list(self, company):
        EmployeeWageCalculator.companies.append(company)


    def get_total_wage(self , company):
        """ returns total wage for each company passed """
        return EmployeeWageCalculator.company_wage_dictionary.get(company)


    def calculate_employee_wage(self , company , data):
        """ calculates and prints total employee wage for a given company based on maximum working days and hours """
        global FULL_DAY_HOURS , PART_TIME_HOURS
        day_count = 0
        total_work_hours = 0
        while day_count < company.max_working_days and total_work_hours < company.max_monthly_hrs:
            day_count += 1

            for emp_data in data['employee_data']:
                if (emp_data['company'] == company.name and emp_data['day'] == day_count):
                    work_hours = FULL_DAY_HOURS if emp_data['status'] == "Full" else PART_TIME_HOURS if emp_data['status'] == "Part" else 0
            total_work_hours += work_hours
            print("Wage for day " , day_count , "is: " ,work_hours * company.emp_rate_per_hr)

        company.total_employee_wage = total_work_hours * company.emp_rate_per_hr
        EmployeeWageCalculator.company_wage_dictionary[company.name] = company.total_employee_wage


def employee_wage_calculator():
    wage_builder = EmployeeWageCalculator()
    wage_builder.create_company("Dmart", 20, 100, 20, 0)
    wage_builder.create_company("Reliance", 24, 80, 30, 0)
    wage_builder.create_company("Westside", 15, 90, 30, 0)
    with open('/Users/nusrat/PycharmProjects/Python_Projects/EmployeeWageProblem/main_employee_wage_builder/employeedata.json') as file:
        data = json.load(file)
    for company in EmployeeWageCalculator.companies:
        wage_builder.calculate_employee_wage(company, data)
    print(EmployeeWageCalculator.company_wage_dictionary)


if __name__ == "__main__":
    employee_wage_calculator()
