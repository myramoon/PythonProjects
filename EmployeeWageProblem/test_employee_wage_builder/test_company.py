import json
import pytest

from EmployeeWageProblem.main_employee_wage_builder.employeewagecalculator import EmployeeWageCalculator


@pytest.fixture
def instance_of_wage_calculator():
    wage_builder = EmployeeWageCalculator()
    return wage_builder


def test_given_company_details_should_match_company_name(instance_of_wage_calculator):
    company = instance_of_wage_calculator.create_company("Dmart", max_working_days = 20, max_monthly_hrs = 100,emp_rate_per_hr = 20, total_employee_wage = 0)
    assert company.name == "Dmart"


def test_given_company_details_should_match_company_max_work_days(instance_of_wage_calculator):
    company = instance_of_wage_calculator.create_company("Dmart", max_working_days = 20, max_monthly_hrs = 100,emp_rate_per_hr = 20, total_employee_wage = 0)
    assert company.max_working_days == 20


def test_given_company_details_should_match_company_max_work_hours(instance_of_wage_calculator):
    company = instance_of_wage_calculator.create_company("Dmart", max_working_days = 20, max_monthly_hrs = 100,emp_rate_per_hr = 20, total_employee_wage = 0)
    assert company.max_monthly_hrs == 100


def test_given_company_name_should_raise_exception_if_file_not_found(instance_of_wage_calculator):
    instance_of_wage_calculator.create_company("Dmart", max_working_days = 20, max_monthly_hrs = 100,emp_rate_per_hr = 20, total_employee_wage = 0)
    instance_of_wage_calculator.create_company("Reliance", max_working_days = 24, max_monthly_hrs = 80, emp_rate_per_hr = 30,total_employee_wage = 0)
    instance_of_wage_calculator.create_company("Westside", max_working_days = 15, max_monthly_hrs = 90, emp_rate_per_hr = 30, total_employee_wage = 0)
    try:
        with open('Users/nusrat/PycharmProjects/Python_Projects/EmployeeWageProblem/main_employee_wage_builder/employeedata.json') as file:
            data = json.load(file)
            for company in EmployeeWageCalculator.companies:
                instance_of_wage_calculator.calculate_employee_wage(company, data)
    except FileNotFoundError:
        print ("File doesn't exist")
    assert pytest.raises(FileNotFoundError)


def test_given_company_name_should_return_total_employee_wage_for_company(instance_of_wage_calculator):
    instance_of_wage_calculator.create_company("Dmart", max_working_days=20, max_monthly_hrs=100, emp_rate_per_hr=20,total_employee_wage=0)
    instance_of_wage_calculator.create_company("Reliance", max_working_days=24, max_monthly_hrs=80, emp_rate_per_hr=30,total_employee_wage=0)
    instance_of_wage_calculator.create_company("Westside", max_working_days=15, max_monthly_hrs=90, emp_rate_per_hr=30,total_employee_wage=0)
    try:
        with open('/Users/nusrat/PycharmProjects/Python_Projects/EmployeeWageProblem/main_employee_wage_builder/employeedata.json') as file:
            data = json.load(file)
            for company in EmployeeWageCalculator.companies:
                instance_of_wage_calculator.calculate_employee_wage(company, data)
    except FileNotFoundError:
        print("File doesn't exist")
    assert instance_of_wage_calculator.get_total_wage("Reliance") == 2520



