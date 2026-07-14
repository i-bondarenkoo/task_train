# import math
# from functools import wraps


# def repeat(n: int):
#     def real_decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(0, n):
#                 result = func(*args, **kwargs)
#             return result

#         return wrapper

#     return real_decorator


# # @repeat(4)
# def greet(name):
#     print("jopa")
#     return f"Привет, {name}"


# greet = repeat(4)(greet)
# print(greet("Саша"))
# print(greet.__name__)


# def print_name(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"Имя вызываемой функции - {func.__name__}")
#         result = func(*args, **kwargs)
#         return result

#     return wrapper


# # @print_name
# def sum_two(a: int, b: int):
#     return a + b


# sum_two = print_name(sum_two)
# print(sum_two(2, 5))
# print(sum_two.__name__)

# d = {
#     10: 1,
#     20: 2,
#     30: 3,
# }

# d2 = {
#     10: 4,
#     20: 1,
#     35: 3,
# }


# def join_dict(d1: dict, d2: dict):
#     result = d1.copy()
#     for k, v in d2.items():
#         if k in result:
#             result[k] += v
#         else:
#             result[k] = v
#     return result


# print(join_dict(d1=d, d2=d2))
# print(d)
# print(d2)
# # from collections import Counter

# # print(Counter(d) + Counter(d2))
# print("---")
# w = d.update(d2)
# print(type(d))
# print(d)

# nums = [1, 2, 3, 4, 5]

# m = map(lambda x: x**2, nums)
# print(list(m))
# print(list(m))


# def square_nums(items: list):
#     return [x**2 for x in items]


# def other_square(items: list):
#     result = []
#     for x in items:
#         result.append(x**2)
#     return result


# print(square_nums(nums))
# print(other_square(nums))

# nums = [1, 2, 3, 4, 5, 6, 7, 8]


# def filter_nums(items: list):
#     result = map(lambda y: y * 10, filter(lambda x: x % 2 == 0, items))
#     return list(result)


# print(filter_nums(nums))

# sort_lst = [x * 10 for x in nums if x % 2 == 0]
# print(sort_lst)

# users = [
#     {"name": "Игорь", "age": 30, "city": "Москва"},
#     {"name": "Аня", "age": 25, "city": "Казань"},
#     {"name": "Борис", "age": 35, "city": "Москва"},
#     {"name": "Вера", "age": 25, "city": "Сочи"},
# ]

# sort_by_age = sorted(users, key=lambda x: x["age"])
# print(sort_by_age)
# sort_by_age_reverse = sorted(users, key=lambda x: x["age"], reverse=True)
# print(sort_by_age_reverse)
# sort_by_age_and_name = sorted(users, key=lambda x: (x["age"], x["name"]))
# print(sort_by_age_and_name)
# s = "Is2 The3n a5nd 1sentence thi4s"


# def restore_sentence(s: str) -> str:
#     words = s.split()
#     words.sort(key=lambda w: [c for c in w if c.isdigit()])
#     return " ".join("".join(c for c in w if not c.isdigit()) for w in words)


# print(restore_sentence(s))

orders = [
    {"user": "Игорь", "amount": 1500},
    {"user": "Аня", "amount": 2300},
    {"user": "Игорь", "amount": 700},
    {"user": "Борис", "amount": 5000},
    {"user": "Аня", "amount": 1200},
]


def get_full_amount(items: list):
    result = {}
    for order in items:
        name = order["user"]
        amount = order["amount"]
        if name in result:
            result[name] += amount
        else:
            result[name] = amount
    return result


print(get_full_amount(orders))
