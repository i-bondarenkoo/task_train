from quote_base import QuoteBase
from client import Client
from quote import Quote


class ZenTracker(QuoteBase):
    def __init__(self, base_url_api):
        super().__init__(base_url_api)
        self.list_quotes = []
        self.client = Client(self.base_url_api)

    def get_quote(self):
        response = self.client.get_request("/api/random")
        # result = response.json()
        # return response
        return self._convert_data_to_dict(response)

    def _convert_data_to_dict(self, siquence):
        d1 = {}
        d1["quote"] = siquence[0]["q"]
        d1["author"] = siquence[0]["a"]
        return d1

    def add_quote(self):
        quote: dict = self.get_quote()
        quote_object: Quote = Quote(
            text=quote["quote"],
            author=quote["author"],
        )
        for q in self.list_quotes:
            # if q.text == quote_object.text and q.author == quote_object.author:
            if q == quote_object:
                raise ValueError("Цитата уже есть в списке")
        self.list_quotes.append(quote_object)

    # def __str__(self):
    #     list_string = []
    #     for q in self.list_quotes:
    #         new_str: str = f"Цитата: {q['quote']}, Автор: {q['author']}"
    #         list_string.append(new_str)
    #     return "\n".join(list_string)
    def __str__(self):
        return "\n".join(str(q) for q in self.list_quotes)

    def __repr__(self):
        return str([q for q in self.list_quotes])
