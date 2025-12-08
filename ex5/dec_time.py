import time


def count_runtime(func):
    async def wrapper(*args, **kwargs):
        start = time.time()
        result = await func(*args, **kwargs)
        stop = time.time() - start
        print(f"Время работы функции - {stop}")
        return result

    return wrapper
