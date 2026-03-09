class Comment:
    def __init__(self, text: str, author: str):
        self.text = text
        self.author = author

    def __str__(self):
        return f"Comment=(text:{self.text}, author:{self.author})"


class Post:
    def __init__(self, name: str):
        self.name = name
        self.comments = []

    def add_comment(self, text: str, author: str):
        comment = Comment(text, author)
        self.comments.append(comment)

    def show_comments(self):
        for com in self.comments:
            print(com)


post = Post("My first post")
post.add_comment("Nice post!", "Alex")
post.add_comment("Thanks", "Igor")
post.show_comments()
