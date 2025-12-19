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
numbers = [2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 3]


def search_digit(n: list):
    d1 = {}
    for i in n:
        if i not in d1.keys():
            d1[i] = 1
        else:
            return i


print(search_digit(numbers))
