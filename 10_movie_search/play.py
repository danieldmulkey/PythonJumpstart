import requests
import collections


MovieResult = collections.namedtuple(
    "MovieResult",
    "imdb_code, title, duration, director, year, rating, imdb_score, keywords, genres")

search = input("Enter search term: ")
url = "http://movie_service.talkpython.fm/api/search/{}".format(search)

resp = requests.get(url)
resp.raise_for_status()

movie_data = resp.json()
movies_list = movie_data.get('hits')

# movies = []
# for md in movies_list:
#     # First - Ugly way:
#     m = MovieResult(
#         imdb_code=md.get('imdb_code'),
#         title=md.get('title'),
#         duration=md.get('duration'),
#         director=md.get('director'),
#         year=md.get('year', 0),
#         rating=md.get('rating', 0),
#         imdb_score=md.get('imdb_score', 0.0),
#         keywords=md.get('keywords'),
#         genres=md.get('genres')
#     )
#     movies.append(m)

# Can use **kwargs to auto-convert args to dictionary:
# def method(x, y, z, **kwargs):
#     print("kwargs=", kwargs)
#
# method(3, 54, z=2, format=True, age=16)
# >>> kwargs= {'format': True, 'age': 16}

# movies = []
# for md in movies_list:
#     # Now - better way IFF dict keys and function args are identical (as done in MovieResult definition):
#     m = MovieResult(**md)
#     movies.append(m)

# Finally - best way, again relies on keys and args matching
movies = [MovieResult(**md) for md in movies_list]


print("Found {} movies for search {}".format(len(movies), search))
for m in movies:
    print("{} -- {}".format(m.year, m.title))