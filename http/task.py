# import asyncio
# import aiohttp


# async def get_request(session, url):
#     query = await session.get(url)
#     return await query.json()


# async def fetch():
#     async with aiohttp.ClientSession() as session:
#         list_tasks = []
#         urls = [
#             "https://jsonplaceholder.typicode.com/posts/1",
#             "https://jsonplaceholder.typicode.com/posts/2",
#             "https://jsonplaceholder.typicode.com/posts/3",
#             "https://jsonplaceholder.typicode.com/users/1",
#             "https://jsonplaceholder.typicode.com/todos/1",
#         ]
#         for u in urls:
#             list_tasks.append(get_request(session, u))
#         response = await asyncio.gather(*list_tasks)
#         return response


# asyncio.run(fetch())

# сделать функцию-замыкание которая перемножает 2 числа
# def mul_num(x):
#     def mul1(y):
#         return x * y

#     return mul1


# nul_num = mul_num(2)
# print(nul_num(5))
# print(nul_num.__closure__)


# сделать функцию-счетчик через замыкание
# def make_counter(x: int = 0):
#     def counter():
#         # nonlocal x
#         x += 1
#         return x

#     return counter


# c1 = make_counter(2)
# print(c1())
# print(c1())
# print(c1())
# print(c1())

# from functools import wraps


# def print_name(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(func.__name__)
#         return func(*args, **kwargs)

#     return wrapper


# @print_name
# def test():
#     pass


# # test = print_name(test)
# print(test)
# print(test.__name__)
# print(test.__wrapped__)


# from typing import Callable
# from functools import wraps


# def repeat(n: int):
#     def real_decorator(func: Callable):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             result = None
#             for _ in range(0, n):
#                 result = func(*args, **kwargs)
#             return result

#         return wrapper

#     return real_decorator


# # @repeat(5)
# def hello(name: str):
#     print(f"hi, {name}")


# print(hello("jopa"))
# hello = repeat(5)(hello)
# print(hello())
# print(hello.__name__)
# from functools import wraps


# def debug(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(
#             f"Функция вызвана с аргументами args=({args}), и именованными аргументами kwargs=({kwargs}, имя функции: {func.__name__})"
#         )
#         result = func(*args, **kwargs)
#         # print(f"Result: {result}")
#         return result

#     return wrapper


# # @debug
# def add(a, b):
#     return a + b


# add = debug(add)
# print(add(2, 3))
# # print(add.__name__)
