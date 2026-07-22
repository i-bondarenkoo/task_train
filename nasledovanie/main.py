from fulltime import FullTimeEmployee, FullTimeWithBonus
from hourly import HourlyEmployee
from seller import SellerEmployee

if __name__ == "__main__":
    list_employee = []
    ft_employee = FullTimeEmployee("Igor", "backend developer", 25, 150000)
    list_employee.append(ft_employee)
    h_employee = HourlyEmployee("Andy", 250, 20)
    list_employee.append(h_employee)
    s_employee = SellerEmployee("Masha", 10000, 2500, 0.35)
    list_employee.append(s_employee)
    result = 0
    for e in list_employee:
        salary = e.get_salary()
        result += salary
        print(f"{e.name} : {salary}")
    print(f"Общая сумма зарплат = {result}")
    ft_bonus_emp = FullTimeWithBonus("Sasha", "hr", 22, 15000, 500)
    print(FullTimeWithBonus.__mro__)
    print(ft_bonus_emp.get_salary())
    # print(ft_bonus_emp.__dict__)
    # print(FullTimeWithBonus.__dict__)
    print(ft_employee.__dict__)
    print(FullTimeEmployee.__dict__)
