from _IDGen import ID_generator


"""
Privacy level:
1: Only Me
2: Select Group
3: Frients
4: Public
"""


class BucketListItem:
    def __init__(self, name: str, description: str, privacy_level: int, completed: bool = False):
        self.id = ID_generator("bli", name)
        self.name = name
        self.description = description
        self.privacy_level = privacy_level
        self.completed = completed
        self.likes = []
        self.comments = []

    def add_like(self, like):
        self.likes.append(like)

    def add_comment(self, comment):
        self.comments.append(comment)
