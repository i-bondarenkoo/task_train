import threading
import time

counter = 0
lock = threading.Lock()


def worker():
    global counter
    for _ in range(10_000):
        # делаем еще 1 ссылку на глобальную переменную, чтобы разорвать операцию += на 2, сначала ссылка, потом присваивание
        # так же добавили небольшую паузу, чтобы поток успел переключиться
        # temp = counter
        time.sleep(0.00001)
        # counter = temp + 1
        with lock:
            counter += 1


if __name__ == "__main__":
    list_threads = []
    for _ in range(0, 100):
        thrd = threading.Thread(target=worker)
        list_threads.append(thrd)
    start = time.time()
    for el in list_threads:
        el.start()
    for el in list_threads:
        el.join()
    print(counter)
    stop = time.time()
    print(f"Время выполнения в 100 потоках - {stop -start}")
