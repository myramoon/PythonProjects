from EmployeeWageProblem.main_employee_wage_builder.employee_wage_calculator import Employee_Wage_Calculator


class Test_Employee_Wage_Builder:

    def test_given_company_details_should_match_company_name(self):
        wage_builder = Employee_Wage_Calculator()
        company = wage_builder.add_company_details("Dmart", 20, 100, 20, 0)
        assert company.name == "Dmart"

    def test_given_company_details_should_match_company_max_work_days(self):
        wage_builder = Employee_Wage_Calculator()
        company = wage_builder.add_company_details("Dmart", 20, 100, 20, 0)
        assert company.max_working_days == 20

    def test_given_company_details_should_match_company_max_work_hours(self):
        wage_builder = Employee_Wage_Calculator()
        company = wage_builder.add_company_details("Dmart", 20, 100, 20, 0)
        assert company.max_monthly_hrs == 100

    def test_given_company_list_should_calculate_total_employee_wage_for_each_company(self):
        wage_builder = Employee_Wage_Calculator()
        dmart = wage_builder.add_company_details("Dmart",  20,  100, 20,  0)
        reliance = wage_builder.add_company_details("Reliance", 30,  80,  30, 0)
        westside = wage_builder.add_company_details("Westside",  15,  90,  30,  0)
        for company in Employee_Wage_Calculator.companies:
            wage_builder.calculate_employee_wage(company)
        print(Employee_Wage_Calculator.company_wage_dictionary)
        assert (wage_builder.get_total_wage(dmart) == Employee_Wage_Calculator.company_wage_dictionary.get('Dmart') )








