from _IDGen import ID_generator
from datetime import date, datetime


class Comment:
    def __init__(self, user, post, content):
        self.user = user
        self.post = post
        self.content = content
        self.timestamp = datetime.now()
        self.likes = []
        self.comments = []

    def add_like(self, like):
        self.likes.append(like)

    def add_comment(self, comment):
        self.comments.append(comment)
