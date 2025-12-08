from f_manager import fm
from f_processor import p
import asyncio


async def main():
    # result1 = p.count_lines(
    #     "C:/Users/i.bondarenko/Desktop/task_practice/ex5/example/1.txt",
    # )

    # result2 = p.count_chars(
    #     "C:/Users/i.bondarenko/Desktop/task_practice/ex5/example/2.txt",
    # )
    # task1 = asyncio.create_task(result1)
    # task2 = asyncio.create_task(result2)
    # await task1
    # await task2
    result = await p.count_lines(
        "C:/Users/i.bondarenko/Desktop/task_practice/ex5/example/1.txt",
    )
    print(result)
    result2 = await p.count_chars(
        "C:/Users/i.bondarenko/Desktop/task_practice/ex5/example/2.txt",
    )
    print(result2)


if __name__ == "__main__":
    asyncio.run(main())
