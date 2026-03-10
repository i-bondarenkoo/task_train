class Comment:
    def __init__(self, text: str, author: str):
        self.text = text
        self.author = author

    def __str__(self):
        return f"Comment=({self.text}, {self.author})"


class Post:
    def __init__(self, name: str):
        self.name = name
        self.comments = []

    def add_comment(self, text: str, author: str):
        user = User(author)
        comment = Comment(text, user)
        self.comments.append(comment)

    def show_comments(self):
        for com in self.comments:
            print(com)


class User:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"{self.name}"


post = Post("My first post")
alex = User("Alex")
igor = User("Igor")
post.add_comment("Nice post!", alex)
post.add_comment("Thanks", igor)
post.show_comments()
