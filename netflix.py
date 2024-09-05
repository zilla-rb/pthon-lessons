movies = [
    {"title": "The shawshank Redemption", "genre": "Drama", "rating ": "9.3" },
    {"title": "The Godfather", "genre": "crime", "rating ": "9.2" },
    {"title": "Pulp Fiction", "genre": "crime", "rating ": "8.9" },
    {"title": "Fight Club", "genre": "Drame", "rating ": "8.8" },
    {"title": "The Dark Knight", "genre": "Action", "rating ": "9.0"},
]


#count the number of movies in each genre using a dictionary comprehension
genre_count = {genre:sum(1 for movie in movies if movie['genre'] == genre) for genre in
                {movie['genre']: None for movie in movies}}
print(genre_count )# 
