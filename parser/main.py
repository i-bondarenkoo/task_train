import aiohttp
import asyncio
from pydantic import BaseModel
from pydantic_core import ValidationError


class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str


async def fetch(
    session: aiohttp.ClientSession,
    url_in: str,
    obj_name: str,
    user_data: dict | None = None,
    method: str = "GET",
    obj_id: int | None = None,
):
    if obj_id is None:
        edit_url = f"{url_in}/{obj_name}"
    else:
        edit_url = f"{url_in}/{obj_name}/{str(obj_id)}"
    try:
        if method == "GET":
            response = await session.get(edit_url)
        else:
            response = await session.post(
                url=edit_url,
                json=user_data,
                headers={"Content-type": "application/json"},
            )
        if response.status == 200 or response.status == 201:
            print(response.status)
            content = await response.json()
            return Post(
                **content,
            )
    except aiohttp.ClientError:
        print("Проблема с сетью")
    except ValidationError:
        print("Поля модели не соответствуют схеме")
    else:
        print(f"Ответ сервера - {response.status}")


async def get_http_session():
    session = aiohttp.ClientSession()
    return session


if __name__ == "__main__":

    async def main():
        # coroutins: list = []
        url = "https://jsonplaceholder.typicode.com"
        session = await get_http_session()
        # for _ in range(5):
        #     coroutins.append(fetch(url_in=url, session=session))
        # result = await asyncio.gather(*coroutins)
        # print(result)
        task1 = asyncio.create_task(
            fetch(
                url_in=url,
                session=session,
                obj_name="posts",
                method="POST",
                user_data={
                    "userId": 2121,
                    "title": "test123",
                    "body": "example post request",
                },
            )
        )
        task2 = asyncio.create_task(
            fetch(
                url_in=url,
                session=session,
                obj_name="posts",
                method="GET",
                obj_id=24,
            )
        )
        result = await task1
        result2 = await task2
        print(result)
        print(result2)
        await session.close()


asyncio.run(main())
