import time


def count_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        stop_time = time.time() - start_time
        print(f"Время работы запроса - {stop_time}")
        return result

    return wrapper
