import aiofiles
from dec_time import count_runtime
import asyncio


class Processor:
    @count_runtime
    async def count_lines(self, path):
        lines = 0
        async with aiofiles.open(
            file=path,
            mode="r",
            encoding="utf-8",
        ) as file:
            async for s1 in file:
                lines += 1
        return lines

    @count_runtime
    async def count_chars(self, path):
        async with aiofiles.open(
            file=path,
            mode="r",
            encoding="utf-8",
        ) as file:
            content = await file.read()
            await asyncio.sleep(3)
            return len(content)


p = Processor()
