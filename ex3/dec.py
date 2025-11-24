import time
import inspect


def count_time(func):
    if inspect.iscoroutinefunction(func):
        # ДЛЯ АСИНХРОННОЙ ФУНКЦИИ
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            result = await func(*args, **kwargs)
            stop_time = time.time() - start_time
            print(f"Время работы запроса - {stop_time}")
            return result

        return wrapper

    else:
        # ДЛЯ СИНХРОННОЙ ФУНКЦИИ
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            stop_time = time.time() - start_time
            print(f"Время работы запроса - {stop_time}")
            return result

        return wrapper
