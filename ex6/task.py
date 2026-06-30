import math
from functools import wraps


def repeat(n: int):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(0, n):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return real_decorator


# @repeat(4)
def greet(name):
    return f"Привет, {name}"


greet = repeat(4)(greet)
print(greet("Саша"))


def print_name(func):
    def wrapper(*args, **kwargs):
        print(f"Имя вызываемой функции - {func.__name__}")
        result = func(*args, **kwargs)
        return result

    return wrapper


# @print_name
def sum_two(a: int, b: int):
    return a + b


sum_two = print_name(sum_two)
print(sum_two(2, 5))
