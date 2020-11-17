import json
from EmployeeWageProblem.main_employee_wage_builder.employeewagecalculator import EmployeeWageCalculator


class Test_Employee_Wage_Builder:

    def test_given_company_details_should_match_company_name(self):
        wage_builder = EmployeeWageCalculator()
        company = wage_builder.add_company_details("Dmart", 20, 100, 20, 0)
        assert company.name == "Dmart"

    def test_given_company_details_should_match_company_max_work_days(self):
        wage_builder = EmployeeWageCalculator()
        company = wage_builder.add_company_details("Dmart", 20, 100, 20, 0)
        assert company.max_working_days == 20

    def test_given_company_details_should_match_company_max_work_hours(self):
        wage_builder = EmployeeWageCalculator()
        company = wage_builder.add_company_details("Dmart", 20, 100, 20, 0)
        assert company.max_monthly_hrs == 100

    def test_given_company_name_should_return_total_employee_wage_for_company(self):
        wage_builder = EmployeeWageCalculator()
        wage_builder.add_company_details("Dmart",  20,  100, 20,  0)
        wage_builder.add_company_details("Reliance", 30,  80,  30, 0)
        wage_builder.add_company_details("Westside",  15,  90,  30,  0)
        with open('/Users/nusrat/PycharmProjects/Python_Projects/EmployeeWageProblem/main_employee_wage_builder/employeedata.json') as file:
            data = json.load(file)
        for company in EmployeeWageCalculator.companies:
            wage_builder.calculate_employee_wage(company , data)
        assert wage_builder.get_total_wage("Reliance") == 2520









