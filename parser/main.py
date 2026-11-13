import aiohttp
import asyncio


async def fetch(
    session: aiohttp.ClientSession,
    url_in: str,
    posts_id: int = 2,
):
    edit_url = f"{url_in}/{str(posts_id)}"
    try:
        response = await session.get(edit_url)
    except aiohttp.ClientError:
        print("Проблема с сетью")
    else:
        if response.status == 200:
            return await response.json()
        else:
            print(f"Ответ сервера - {response.status}")


async def get_http_session():
    session = aiohttp.ClientSession()
    return session


if __name__ == "__main__":

    async def main():
        # coroutins: list = []
        url = "https://jsonplaceholder.typicode.com/posts123"
        session = await get_http_session()
        # for _ in range(5):
        #     coroutins.append(fetch(url_in=url, session=session))
        # result = await asyncio.gather(*coroutins)
        # print(result)
        task1 = asyncio.create_task(fetch(url_in=url, session=session))
        task2 = asyncio.create_task(fetch(url_in=url, session=session))
        task3 = asyncio.create_task(fetch(url_in=url, session=session))

        res1 = await task1
        res2 = await task2
        res3 = await task3
        print(res1)
        print(res2)
        print(res3)
        await session.close()


asyncio.run(main())
