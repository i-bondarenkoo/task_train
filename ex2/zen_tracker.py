from quote import QuoteBase
from client import Client


class ZenTracker(QuoteBase):
    def __init__(self, base_url_api):
        super().__init__(base_url_api)
        self.list_quotes = []
        self.client = Client(self.base_url_api)

    def get_quote(self):
        response = self.client.get_request("/api/random")
        # result = response.json()
        # return response
        quote = response[0]["q"]
        author = response[0]["a"]
        return quote + "\n" + author
