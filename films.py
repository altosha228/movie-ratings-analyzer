from typing import Callable, Dict, List, Optional

Movie = Dict[str, object]
FilterStrategy = Callable[[Movie], bool]

# Dictionary of movies
movies: List[Movie] = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"},
]


# Strategy predicates for movie filtering
def rating_above_strategy(threshold: float = 5.5) -> FilterStrategy:
    return lambda movie: float(movie["imdb"]) > threshold


def category_strategy(category_name: str) -> FilterStrategy:
    return lambda movie: movie["category"] == category_name


def filter_movies(movie_list: List[Movie], strategy: FilterStrategy) -> List[Movie]:
    return [movie for movie in movie_list if strategy(movie)]


def isRatingAbove5(name: str, movie_list: Optional[List[Movie]] = None) -> Optional[bool]:
    catalog = movies if movie_list is None else movie_list
    selected_movie = next((m for m in catalog if m["name"] == name), None)
    if selected_movie is None:
        print("No movie with name " + name)
        return None
    result = float(selected_movie["imdb"]) > 5.5
    print(result)
    return result


def getSublistOfRatingAbove5(movie_list: List[Movie]) -> List[Movie]:
    return filter_movies(movie_list, rating_above_strategy(5.5))


def getSublistOfCategory(movie_list: List[Movie], categoryName: str) -> List[Movie]:
    return filter_movies(movie_list, category_strategy(categoryName))


def calculateAverage(movie_list: List[Movie]) -> float:
    total = 0.0
    cnt = 0
    for movie in movie_list:
        total += float(movie["imdb"])
        cnt = cnt + 1
    if cnt == 0:
        return 0.0
    return total / cnt


def calculateAverageInCategory(movie_list: List[Movie], categoryName: str) -> float:
    total = 0.0
    cnt = 0
    for movie in movie_list:
        if movie["category"] == categoryName:
            total += float(movie["imdb"])
            cnt = cnt + 1
    if cnt == 0:
        return 0.0
    return total / cnt


if __name__ == "__main__":
    isRatingAbove5("AlphaJet")
    isRatingAbove5("Joking muck")
    print(calculateAverageInCategory(movies, "Thriller"))