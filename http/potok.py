import requests
import time
import threading

urls = [
    "https://example.com",
    "https://example.com",
    "https://example.com",
]


def get_data(url):
    # for u in urls:
    result = requests.get(url)
    print(result.status_code)


if __name__ == "__main__":
    list_thrds = []
    for u in urls:
        thrd = threading.Thread(target=get_data, args=(u,))
        list_thrds.append(thrd)
    start = time.time()
    for elements in list_thrds:
        elements.start()
    for elem in list_thrds:
        elem.join()
    end = time.time()

    print(f"Время запросов - {end - start}")
