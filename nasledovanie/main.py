from fulltime import FullTimeEmployee
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
        print(f"{e.name} : {salary}")
    print(f"Общая сумма зарплат = {result}")
