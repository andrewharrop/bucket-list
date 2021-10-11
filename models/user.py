
from datetime import datetime
from _IDGen import ID_generator
from bucketList import BucketList

"""
Passwords are not hashed here because they should be closer to a UI layer. This is only a data model

"""


class User:

    def __init__(self, name, email, password):
        self.id = ID_generator("user", email)
        self.name = name
        self.email = email
        self.password = password
        self.registered_time = datetime.now()
        self.bucket_lists = {}
        self.comments = []
        self.likes = []
        self.followers = []

    def create_bucket_list(self, name):
        self.bucket_lists[name] = BucketList(name)

    def add_to_bucket_list(self, bucket_list, item):
        self.bucket_lists[bucket_list].add_item(item)

    def comment(self, item, comment):
        self.comments.append(comment)
        item.add_comment(comment)

    def like(self, item, like):
        self.likes.append(like)
        item.add_like(like)

    def change_name(self, name):
        self.name = name
