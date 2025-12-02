from task import Task


if __name__ == "__main__":
    t1 = Task("download")
    print(t1)
    t2 = Task("download")
    t3 = Task("download")
    print(t2)
    print(t3.status)
