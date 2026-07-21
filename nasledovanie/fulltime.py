from employee import Employee


class FullTimeEmployee(Employee):
    def __init__(self, name, post, age, salary):
        super().__init__(name)
        self.post = post
        self.age = age
        self.salary = salary

    def get_salary(self):
        return self.salary


# ft_employee = FullTimeEmployee("Igor", "backend developer", 25, 150000)
# print(ft_employee.get_salary())
