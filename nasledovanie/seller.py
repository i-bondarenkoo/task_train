from employee import Employee


class SellerEmployee(Employee):
    def __init__(self, name, base_salary, sales_amount, precent_sale):
        super().__init__(name)
        self.base_salary = base_salary
        self.sales_amount = sales_amount
        self.precent_sale = precent_sale

    def get_salary(self):
        result = self.base_salary + self.sales_amount * self.precent_sale
        return result


# s_employee = SellerEmployee("Masha", 10000, 2500, 0.35)
# print(s_employee.get_salary())
