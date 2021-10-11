from reImport import *
"""
Create three users
"""

bart = User("Bart Simpson", "bart@thesimpsons.com", "eatmyshorts")
harry = User("Harry Potter", "hp@hogwarts.uk", "iluvginny")
luke = User("Luke Skywalker", "luke@jedi.gov", "heismyfather")


"""
Create some lists
"""

bart.create_bucket_list("Pranks")
bart.create_bucket_list("Not pranks")

harry.create_bucket_list("Spells")

luke.create_bucket_list("Sith 2 slay")
luke.create_bucket_list("Planets")

"""
    Add to the lists
"""

bart.add_to_bucket_list("Pranks", BucketListItem(
    "Homer prank", "Swap duff with sewage", 3))
bart.add_to_bucket_list("Pranks", BucketListItem(
    "Marge prank", "Steal car", 4))

bart.add_to_bucket_list("Not pranks", BucketListItem(
    "Homework", "Do not do any homework", 4))

harry.add_to_bucket_list("Spells", BucketListItem(
    "Tarantallegra", "Consult Hermione", 1))

luke.add_to_bucket_list("Sith 2 slay", BucketListItem(
    "Darth Vader", "Location unknown", 2))

"""
    Add some likes
"""
