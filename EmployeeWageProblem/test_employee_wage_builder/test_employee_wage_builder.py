from EmployeeWageProblem.main_employee_wage_builder.employee_wage_builder import Company

class Test_Employee_Wage_Builder:

    def test_init_company_name(self):
        dmart = Company("Dmart", 20, 100, 20)
        assert dmart.name == "Dmart"

    def test_init_company_max_work_days(self):
        dmart = Company("Dmart", 20, 100, 20)
        assert dmart.max_working_days == 20

    def test_init_company_max_work_hours(self):
        dmart = Company("Dmart", 20, 100, 20)
        assert dmart.max_monthly_hrs == 100

    def test_calculate_work_hours(self):
        dmart = Company("Dmart", 20, 100, 20)
        assert dmart.calculate_work_hours(2) == 8

    def test_calculate_employee_wage(self):
        dmart = Company("Dmart", 20, 100, 20)
        reliance = Company("Reliance", 30, 80, 30)
        westside = Company("Westside", 15, 90, 30)
        dmart.calculate_employee_wage()
        reliance.calculate_employee_wage()
        westside.calculate_employee_wage()
        assert True





