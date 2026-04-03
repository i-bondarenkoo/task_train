import asyncio
import aiohttp


async def get_request(session, url):
    query = await session.get(url)
    return await query.json()


async def fetch():
    async with aiohttp.ClientSession() as session:
        list_tasks = []
        urls = [
            "https://jsonplaceholder.typicode.com/posts/1",
            "https://jsonplaceholder.typicode.com/posts/2",
            "https://jsonplaceholder.typicode.com/posts/3",
            "https://jsonplaceholder.typicode.com/users/1",
            "https://jsonplaceholder.typicode.com/todos/1",
        ]
        for u in urls:
            list_tasks.append(get_request(session, u))
        response = await asyncio.gather(*list_tasks)
        return response


asyncio.run(fetch())
