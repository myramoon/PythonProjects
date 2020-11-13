from EmployeeWageProblem.main_employee_wage_builder.company import Company
from EmployeeWageProblem.main_employee_wage_builder.employee_wage_calculator import Employee_Wage_Calculator


class Test_Employee_Wage_Builder:

    def test_given_company_details_should_match_company_name(self):
        dmart = Company("Dmart", 20, 100, 20, 0)
        assert dmart.name == "Dmart"

    def test_given_company_details_should_match_company_max_work_days(self):
        dmart = Company("Dmart", 20, 100, 20, 0)
        assert dmart.max_working_days == 20

    def test_given_company_details_should_match_company_max_work_hours(self):
        dmart = Company("Dmart", 20, 100, 20, 0)
        assert dmart.max_monthly_hrs == 100

    def test_given_attendance_status_should_return_work_hours(self):
        wage_builder = Employee_Wage_Calculator()
        assert wage_builder.calculate_work_hours(2) == 8

    def test_given_company_details_should_calculate_employee_wage(self):
        wage_builder = Employee_Wage_Calculator()
        dmart = Company("Dmart", 20, 100, 20, 0)
        reliance = Company("Reliance", 30, 80, 30, 0)
        westside = Company("Westside", 15, 90, 30, 0)
        wage_builder.calculate_employee_wage(dmart)
        wage_builder.calculate_employee_wage(reliance)
        wage_builder.calculate_employee_wage(westside)
        assert True

    def test_given_company_list_should_calculate_total_employee_wage_for_each_company(self):
        companies = []
        wage_builder = Employee_Wage_Calculator()
        dmart = Company("Dmart", 20, 100, 20, 0)
        reliance = Company("Reliance", 30, 80, 30, 0)
        westside = Company("Westside", 15, 90, 30, 0)
        companies.append(dmart)
        companies.append(reliance)
        companies.append(westside)
        for company in companies:
            wage_builder.calculate_employee_wage(company)
        assert True







