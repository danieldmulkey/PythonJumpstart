# DICTIONARIES FOR DISPARATE TYPES OF RELATED DATA:
lookup = {}
lookup = dict()
lookup = {'age':42, 'loc': 'Italy'}
lookup = dict(age=42, loc='Italy')

class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level

gandalf = Wizard('Gandalf', 42)

print(gandalf.__dict__)  # NB! Dictionaries basis of objects in Python!

print(lookup)
print(lookup['loc'])  # says dict value lookup is extremely fast

if 'cat' in lookup:
    print(lookup['cat'])

lookup['cat'] = 'Fun code demos'

if 'cat' in lookup:
    print(lookup['cat'])


# DICTIONARIES FOR DIFFERENT INSTANCES OF HOMOGENEOUS DATA:
# Store a homogeneous set of data and find it by key. So use the dictionary as a
# temporary structure in order to more quickly find your answer.
# Original data type --> dict --> find by key. Want to find it by a different key? Make a
# new dictionary.
# NB: Can only use one field at a time (id, or name, or email) since dict takes key
# and value only, but it's extremely fast if you know which one you want to search with.
# Suppose these came from a data source (database, web service, etc.) and we want to
# randomly access them
import collections

User = collections.namedtuple('user', 'id, name, email')
users = [
    User(1, 'user1', 'user1@talkpython.fm'),
    User(2, 'user2', 'user2@talkpython.fm'),
    User(3, 'user3', 'user3@talkpython.fm'),
    User(4, 'user4', 'user4@talkpython.fm')
]

# build search dict from namedtuple content:
lookup = dict()
for u in users:
    lookup[u.id] = u

print(lookup[3])

for u in users:
    lookup[u.email] = u
print(lookup['user4@talkpython.fm'])