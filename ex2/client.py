import requests


class Client:
    def __init__(self, url_for_request: str):
        # основной url для запросов
        self.url_for_request = url_for_request

    def get_request(
        self,
        path: str,
        params: dict = None,
    ):
        # path это параметр пути/эндпоинт, куда отправится запрос
        # params это параметры запроса, все что будет указано после знака?
        response = requests.get(
            f"{self.url_for_request}{path}",
            params=params,
        )
        result = response.json()
        return result
