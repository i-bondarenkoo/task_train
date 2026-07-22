class Bonus:
    def __init__(self, amount):
        self.amount = amount

    def get_salary(self):
        salary = super().get_salary()
        return salary + self.amount
