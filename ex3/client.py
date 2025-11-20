import requests


class Client:

    def get_request(
        self,
        url: str,
        path: str,
        params: dict | None = None,
    ):

        response = requests.get(
            f"{url}{path}",
            params=params,
        )

        result = response.json()
        return result
