import requests


class Client:
    def __init__(self, api_url: str):
        self.api_url = api_url

    def get_request(self):
        try:
            response = requests.get(
                url=self.api_url,
            )
        except Exception:
            print("Что-то пошло не так")
