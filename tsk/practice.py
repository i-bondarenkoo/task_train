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

# ------------СПИСКИ-----------------
# Сумма элементов списка
# [1, 2, 3, 4, 5] → 15
# lst = [1, 2, 3, 4, 5]


# def sum_digit(l: list):
#     # return sum(lst)
#     counter = 0
#     for elements in l:
#         counter += elements
#     return counter


# print(sum_digit(lst))

# # Найти максимальный элемент (НЕ через max)
# l1 = [-3, -1, -9, -2]


# def search_maximum(l: list):
#     maxi = l[0]
#     for element in l[1:]:
#         if element > maxi:
#             maxi = element
#     return maxi


# print(search_maximum(l1))
# # Подсчитать количество чётных чисел
# l2 = [1, 2, 3, 4, 6, 2]


# def count_digit(l: list):
#     counter = 0
#     for element in l:
#         if element % 2 == 0:
#             counter += 1
#     return counter


# print(count_digit(l2))
# # Создать новый список только из положительных чисел
# # [-1, 3, 0, -5, 7] → [3, 7]
# l3 = [-1, 3, 0, -5, 7]


# def gen_list(l: list):
#     return [num for num in l if num > 0]


# print(gen_list(l3))

# развернуть список в ручную
# [1, 2, 3, 4] → [4, 3, 2, 1]
# lst = [1, 2, 3, 4]


# def rev_list(l: list):
#     new_list = []
#     # for element in l:
#     #     new_list.insert(0, element)
#     # return new_list
#     ind = range(len(l) - 1, -1, -1)
#     print(type(ind))
#     for el in ind:
#         new_list.append(l[el])

#     return new_list


# print(rev_list(lst))

# Найти второй максимум
# [5, 1, 9, 7, 9] → 7
# ls = [5, 1, 9, 7, 9, 8]


# def search_second_max(l: list):
#     max_1 = l[0]
#     max_2 = l[1]
#     if max_2 > max_1:
#         m3 = max_2
#         max_2 = max_1
#         max_1 = m3
#     for elem in l[2:]:
#         if elem > max_1:
#             max_2 = max_1
#             max_1 = elem
#         elif elem < max_1 and elem > max_2:
#             max_2 = elem
#     return max_2


# print(search_second_max(ls))

# проверить отсортирован ли список
# [1, 2, 3, 5] → True
# [1, 3, 2] → False
# [5] → True
# [] → True

# l1 = [1, 2, 3, 5]
# l2 = [1, 3, 2]
# l3 = [5]
# l4 = []


# def check_sorted_list(l: list):
#     if len(l) == 0 or len(l) == 1:
#         return True
#     for i in range(len(l) - 1):
#         if l[i] > l[i + 1]:
#             return False
#     return True


# print(check_sorted_list(l1))
# print(check_sorted_list(l2))
# print(check_sorted_list(l3))
# print(check_sorted_list(l4))

# -------------------Операторы и циклы------------------
# words = ["a1", "b1", "c2", "d2", "e1"]


# def func1(w: list):
#     for ind, value in enumerate(w):
#         if "1" in value:
#             print(ind, value)
#         elif "2" in value:
#             continue
#         elif "3" in value:
#             break
#     else:
#         print("Цикл завершился корректно, без break")


# print(func1(words))
# text = "ab1cd2efgh"


# def func2(t: str):
#     for ind, value in enumerate(t):
#         if value.isdigit():
#             if value == "1":
#                 print(value)
#             elif value == "2":
#                 continue
#             elif value == "3":
#                 break

#     else:
#         print("Цифра 3 не найдена")


# func2(text)

# nums = [4, 7, 2, 9, 5, 1, 8]


# def f3(n: list):
#     i = 0
#     while i < len(n):
#         if n[i] % 2 == 0:
#             print(f"Число:{n[i]}, индекс в последовательности:{i}")
#         elif n[i] == 5:
#             i += 1
#             continue
#         elif n[i] == 1:
#             break
#         i += 1
#     else:
#         print("Число 1 не было найдено")


# f3(nums)

# nums = [10, 20, 30]
# try:
#     it = iter(nums)
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
# except StopIteration:
#     print("Итератор закончился")

# matrix = [[1, 2, 3], [4, 5], [6]]


# # посчитать сумму всех чисел
# def list_sum(l: list):
#     s = 0
#     for row in matrix:
#         for num in row:
#             s += num
#     return s


# print(list_sum(matrix))
# 1 2 3
# 2 4 6
# 3 6 9
# вывести таблицу в виде 3х3
# def get_siquence(M: int = 3, N: int = 3):
#     # lst = []
#     for i in range(1, M + 1):
#         for j in range(1, N + 1):
#             print(i * j, end=" ")
#         print()


# print(get_siquence(5, 5))


# def foo():
#     result = []
#     row = []

#     for i in range(3):
#         row.append(i)
#         result.append(row)

#     return result


# x = foo()
# print(x)

# Напиши генератор pairs(n), который для n = 4 выдаёт:
# (0, 1)
# (1, 2)
# (2, 3)


# def make_gen(n: int):
#     for i in range(n):
#         yield (i, i + 1)


# g = make_gen(4)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# # print(next(g))

# s = "a1b22c333d4"


# def make_list(s: str):
#     l = []
#     for i in range(1, len(s) - 1):
#         if s[i].isdigit() and s[i - 1].isalpha() and s[i + 1].isalpha():
#             l.append(s[i])
#     if s[0].isdigit() and s[1].isalpha():
#         l.insert(0, s[0])
#     if s[len(s) - 1].isdigit() and s[len(s) - 2].isalpha():
#         l.append(s[len(s) - 1])
#     return [int(num) for num in l if int(num) % 2 == 0]


# print(make_list(s))
# ------------СЛОВАРИ, КОРТЕЖИ, НАБОРЫ -------------
# Дан список слов.
# Нужно вернуть словарь, где ключ — слово,
# значение — сколько раз оно встречается.

# l1 = ["apple", "banana", "apple", "orange", "banana", "apple"]


# def count_words(l: list):
#     d1 = {}
#     for word in l:
#         d1[word] = d1.get(word, 0) + 1
#     return d1


# print(count_words(l1))

# Дан список слов.
# Нужно вернуть первое слово, которое не повторяется.
# l1 = ["apple", "banana", "apple", "orange", "banana", "apple"]


# def get_word(l: list):
#     # result = [w for w in l1 if l1.count(w) == 1]
#     # return result[0]
#     d = {}
#     for word in l:
#         d[word] = d.get(word, 0) + 1
#     for word in l:
#         if d[word] == 1:
#             return word


# print(get_word(l1))

# nums = [4, 5, 6, 4, 7, 5, 8]


# def get_new_list(n: list):
#     dictionary = {}
#     for num in nums:
#         dictionary[num] = dictionary.get(num, 0) + 1
#     return [num for num in nums if dictionary[num] == 1]


# print(get_new_list(nums))
# list1 = [4, 4, 5, 6, 7, 5, 8]
# list2 = [5, 6, 9, 4]
# # Нужно вернуть список чисел, которые встречаются в обоих списках, в порядке первого списка.
# # Каждое число должно встречаться в результате только один раз.


# def sorted_nums(l1: list, l2: list):
#     set_other = set(l1) & (set(l2))
#     result = []
#     for num in l1:
#         if num in set_other and num not in result:
#             result.append(num)
#     return result


# print(sorted_nums(list1, list2))
from collections import defaultdict

words = ["hi", "hello", "a", "world", "to", "python"]


# Нужно вернуть словарь, где:
# ключ — длина строки
# значение — список строк этой длины
# порядок строк внутри списков должен сохраниться (как в исходном списке)


def make_dictionary(l: list[str]):
    d1 = defaultdict(list)
    print(d1)
    for w in l:
        d1[len(w)].append(w)
    return d1


print(make_dictionary(words))
