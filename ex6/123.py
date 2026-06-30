# # a = [1, 2, 3]
# # b = a
# # b.append(4)

# # print(a)
# # print(b)


# a = [1, 2, 3]
# b = a
# b += [4]  # вот это
# print(a)
# print(b)


# def has_duplicates(nums: list[int]) -> bool:
#     s1 = set(nums)
#     return len(s1) != len(nums)


# print(has_duplicates([4, 2, 3, 1, -5]))
# print(has_duplicates([0, 0]))


# def is_polindrom(nums: list[int]):
#     left_ind = 0
#     right_ind = len(nums) - 1
#     while left_ind < right_ind:
#         if nums[left_ind] != nums[right_ind]:
#             return False
#         left_ind += 1
#         right_ind -= 1
#     return True


# print(is_polindrom([1, 2, 3, 2, 1]))
# print(is_polindrom([1, 2, 3]))

# t1 = [2, 4, 5, 1, 2, 11, 4, 1]
# print(t1.remove(4))
# print(t1)


# def instersection(a: list[int], b: list[int]) -> list[int]:
#     s1 = set(a)
#     result = []
#     for x in b:
#         if x in s1:
#             result.append(x)
#             s1.remove(x)
#     return result


# print(instersection([1, 2, 3], [2, 5, 7, 9]))
# print(instersection([2, 4, 4], [5, 9, 12, 2, 1, 4]))


# def gen():
#     print("старт")
#     for i in range(3):
#         print(f"отдаю {i}")
#         yield i


# g = gen()
# print("генератор создан")
# first = next(g)
# print(f"получили {first}")


# class Singleton:
#     __instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)

#         return cls.__instance

#     def __init__(
#         self,
#         name: str,
#         email: str,
#     ):
#         if not hasattr(self, "check_obj"):
#             self.name = name
#             self.email = email
#             self.check_obj = True

#     def __str__(self):
#         return f"Singleton(name={self.name}, email={self.email})"


# s1 = Singleton("Игорь", "igor@example.com")
# print(type(s1))
# print(id(s1))
# s2 = Singleton("Jenya", "jenya@example.com")
# print(type(s2))
# print(id(s2))
# print(s1)
# print(s2)

import threading

counter = 0


def increment():
    global counter
    for _ in range(10000000):
        counter += 1


threads = [threading.Thread(target=increment) for _ in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter)
