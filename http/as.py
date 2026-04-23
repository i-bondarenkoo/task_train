import asyncio
import threading
import requests
import aiohttp
import time

urls = [
    "https://ya.ru",
    "https://ya.ru",
    "https://ya.ru",
    "https://ya.ru",
    "https://ya.ru",
]


async def fetch_data(session, url):
    response = await session.get(url)

    print(response.status)


async def main():
    start = time.time()
    list_tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            coro = fetch_data(session, url)
            list_tasks.append(coro)
        result = await asyncio.gather(*list_tasks)
    stop = time.time()
    print(f"Асинхронное выполнение - {stop - start}")


def get_data(url: str):
    response = requests.get(url)
    print(response.status_code)


if __name__ == "__main__":
    start = time.time()
    for url in urls:
        get_data(url)
    stop = time.time()
    print(f"Последовательное выполнение 5 запросов - {stop - start}")
    # -------------------------------
    list_threads = []
    for url in urls:
        thrd = threading.Thread(target=get_data, args=(url,))
        list_threads.append(thrd)
    start2 = time.time()
    for e in list_threads:
        e.start()
    for e in list_threads:
        e.join()
    # ----------------------------------------
    stop2 = time.time()
    print(f"Многопоточное выполнение 5 запросов - {stop2 - start2}")
    asyncio.run(main())
