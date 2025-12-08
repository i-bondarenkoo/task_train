from f_manager import fm
from f_processor import p
import asyncio


async def main():
    result = p.count_lines(
        "C:/Users/i.bondarenko/Desktop/task_practice/ex5/example/123.txt",
    )

    result2 = await p.count_chars(
        "C:/Users/i.bondarenko/Desktop/task_practice/ex5/example/2.txt",
    )
    print(result)
    print(result2)


if __name__ == "__main__":
    asyncio.run(main())
