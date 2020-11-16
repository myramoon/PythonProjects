class Company:

    def __init__(self, name, **company_data):
        """ creates and returns instance of company with given name , maximum working days , maximum monthly hours
        and rate per hour """
        self.name = name
        self.__dict__.update(company_data)
