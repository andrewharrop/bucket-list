from datetime import datetime


class BucketList:
    def __init__(self, name) -> None:
        self.bucket_list = []
        self.name = name
        self.timestamp = datetime.now()
        self.comments = []
        self.likes = []

    def add_item(self, item):
        self.bucket_list.append(item)

    def add_like(self, like):
        self.likes.append(like)

    def add_comment(self, comment):
        self.comments.append(comment)
