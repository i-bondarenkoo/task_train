import aiohttp
import asyncio


class AsyncClient:

    def __init__(self):
        self.session = None

    async def create_session(self):
        if self.session is None:
            try:
                self.session = aiohttp.ClientSession()
            except Exception as e:
                print(f"Ошибка создания сессии: {e}")

    async def get_request(
        self,
        url: str,
        path: str,
        params: dict | None = None,
    ):
        async with self.session.get(
            f"{url}{path}",
            params=params,
        ) as response:
            return await response.json()

    async def close(self):
        if self.session is not None:
            try:
                print("Сессия закрывается")
                await self.session.close()
            except Exception as e:
                print(f"Ошибка при закрытии сессии: {e}")
