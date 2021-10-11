from datetime import datetime


class Like:
    def __init__(self, user, post):
        self.user = user
        self.post = post
        self.timestamp = datetime.now()
