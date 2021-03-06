from abc import ABC , abstractmethod

class ComputeWageInterface(ABC):
    @abstractmethod
    def create_company(self , name , max_working_days , max_monthly_hrs , emp_rate_per_hr , total_employee_wage):
        pass
    @abstractmethod
    def calculate_employee_wage(self , company , file):
        pass
    @abstractmethod
    def get_total_wage(self,company):
        pass