import requests
import time
import threading
import math

urls = [
    "https://example.com",
    "https://example.com",
    "https://example.com",
    "https://example.com",
    "https://example.com",
    "https://example.com",
    "https://example.com",
    "https://example.com",
    "https://example.com",
    "https://example.com",
    "https://example.com",
    "https://example.com",
    "https://example.com",
    "https://example.com",
    "https://example.com",
]


def pow_number(number: int):
    count = 0
    for _ in range(0, 10_000_000):
        count += int(math.pow(number, 2))
    return count


def get_data(url):
    # for u in urls:
    result = requests.get(url)
    print(result.status_code)


# i/o bound
# if __name__ == "__main__":
#     list_thrds = []
#     for u in urls:
#         thrd = threading.Thread(target=get_data, args=(u,))
#         list_thrds.append(thrd)
#     start = time.time()
#     for elements in list_thrds:
#         elements.start()
#     for elem in list_thrds:
#         elem.join()
#     end = time.time()

#     print(f"Время запросов - {end - start}")

# cpu bound
if __name__ == "__main__":
    start = time.time()
    print(pow_number(3))
    stop = time.time()
    print(f"Время работы последовательного кода - {stop - start}")
    list_threads = []
    for _ in range(0, 3):
        thrd = threading.Thread(target=pow_number, args=(3,))
        list_threads.append(thrd)
    start2 = time.time()
    for el in list_threads:
        el.start()
    for el in list_threads:
        el.join()
    stop2 = time.time()
    print(f"Время работы cpu задачи в 3 потоках - {stop2 - start2}")
