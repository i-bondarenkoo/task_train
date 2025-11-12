class Quote:
    def __init__(self, text, author):
        self.text = text
        self.author = author

    def __str__(self):
        return f"Объект: {self.__class__.__name__}, Цитата: {self.text}, Автор: {self.author}"

    def __eq__(self, other):
        if not isinstance(other, Quote):
            return NotImplemented
        return self.author == other.author and self.text == other.text
