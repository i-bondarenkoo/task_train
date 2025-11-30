import asyncio


async def slow(name: str, delay: int):
    print(f"Старт функции {name}")
    await asyncio.sleep(delay)
    print(f"Остановка функции")


async def main():
    a = await slow("A", 1)
    b = await slow("B", 1)
    print(a)
    print(b)
    print("-----")
    t1 = asyncio.create_task(slow("A", 3))
    t2 = asyncio.create_task(slow("B", 3))
    await t1
    await t2


if __name__ == "__main__":

    asyncio.run(main())
