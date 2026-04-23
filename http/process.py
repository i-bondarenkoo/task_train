import multiprocessing
import requests
import math
import time

urls = [
    "https://example.com",
    "https://example.com",
    "https://example.com",
    "https://example.com",
]


def get_data(urls: list[str]):
    for u in urls:
        response = requests.get(u)
        print(response.status_code)


def pow_range(start: int, end: int) -> int:
    result = 0
    for i in range(start, end):
        result += i * i
    return result


if __name__ == "__main__":
    total = 50_000_000
    workers = 4
    start = time.time()
    # get_data(urls=urls)
    pow_range(0, total)
    stop = time.time()
    print(f"Последовательное выполнение - {stop - start}")
    # process1 = multiprocessing.Process(target=get_data, args=(urls[:2],))
    # process2 = multiprocessing.Process(target=get_data, args=(urls[2:4],))
    chunk = total // workers
    ranges = [
        (0, chunk),
        (chunk, chunk * 2),
        (chunk * 2, chunk * 3),
        (chunk * 3, total),
    ]
    # process2 = multiprocessing.Process(target=pow_number, args=(3,))
    start2 = time.time()
    processes = []

    for r in ranges:
        p = multiprocessing.Process(target=pow_range, args=(r[0], r[1]))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    stop2 = time.time()
    print(f"Время работы в отдельных процессах - {stop2-start2}")
