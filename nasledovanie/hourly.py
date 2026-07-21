from employee import Employee


class HourlyEmployee(Employee):
    def __init__(self, name, base_salary, hours):
        super().__init__(name)
        self.base_salary = base_salary
        self.hours = hours

    def get_salary(self):
        result = self.base_salary * self.hours
        return result


# h_employee = HourlyEmployee("Andy", 250, 20)
# print(h_employee.get_salary())
