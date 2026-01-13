# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def square_numbers(n: list):
#     result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, n)))
#     return result


# print(square_numbers(numbers))

# words = ["apple", "banana", "avocado", "blueberry", "apricot"]


# def filter_words(siquence: list[str]):
#     upper_words = list(
#         map(
#             lambda x: x.upper(),
#             filter(lambda x: x[0] == "a", siquence),
#         )
#     )
#     return sorted(upper_words, key=lambda x: len(x), reverse=False)


# print(filter_words(words))
# users = [
#     {"name": "Alice", "age": 30, "is_active": True},
#     {"name": "Bob", "age": 17, "is_active": True},
#     {"name": "Charlie", "age": 25, "is_active": False},
#     {"name": "Diana", "age": 22, "is_active": True},
#     {"name": "Eve", "age": 40, "is_active": False},
# ]


# def filter_users(siquence: list[dict]):
#     result = filter(lambda x: x["is_active"] == True, siquence)
#     return list(filter(lambda x: x["age"] >= 18, result))


# print(filter_users(users))
# numbers = [2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 3]


# def search_digit(n: list):
#     d1 = {}
#     for i in n:
#         if i not in d1.keys():
#             d1[i] = 1
#         else:
#             return i


# print(search_digit(numbers))
# ----------------СТРОКИ-----------------
# s = "  Hello,   world!  This   is  Python  "


# def make_string(s: str):
#     result = s.split()
#     return " ".join(result).lower()


# print(make_string(s))

# s = "Python is AWESOME and powerful"


# def count_chars(s: str):
#     result = s.lower().split()
#     return " ".join(map(lambda x: x.upper() if len(x) > 4 else x.lower(), result))


# print(count_chars(s))
# s = "abccba"


# def check_polindrom(s: str):
#     s = s.lower()
#     s2 = s[::-1]
#     return s == s2


# print(check_polindrom(s))

# s = "python java cplusplus go"


# # Нужно вернуть строку, где:
# # в каждом слове буквы отсортированы по алфавиту
# # порядок слов сохраняется
# def make_string(s: str):
#     words = s.split()
#     sorted_words = map(lambda w: "".join(sorted(w)), words)
#     result = " ".join(sorted_words)
#     return result


# print(make_string(s))

# s = "is2 Thi1s T4est 3a"
# # # Нужно переставить слова в правильный порядок по цифрам и убрать цифры, чтобы получить строку


# def func1(s: str):
#     words = s.split()
#     sorted_words = sorted(
#         words, key=lambda w: int(next(num for num in w if num.isdigit()))
#     )
#     filter_digit = map(
#         lambda x: "".join(char for char in x if char.isalpha()), sorted_words
#     )
#     return " ".join(filter_digit)


# print(func1(s))


# s = "py3thon ja2va go1"


# def f1(s: str):
#     words = s.split()
#     clean_words = map(lambda w: "".join(filter(str.isalpha, w)), words)
#     return " ".join(clean_words)


# print(f1(s))
