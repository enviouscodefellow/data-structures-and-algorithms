# from Challenge_28._movies import movies, movies2
import re

def get_first_word_after_article(title):
    title = re.sub(r"^(The|A|An)\s", "", title)
    return title.split(" ")[0]

def sort_by_year(movies):
    sorted_movies = sorted(movies, key=lambda x: (x["year"], x["title"]), reverse=True)
    # sorted_movies = sorted(movies, key=lambda x: (-x["year"], x["title"]))
    return [movie["title"] for movie in sorted_movies]


def sort_by_title(movies):
    sorted_movies = sorted(movies, key=lambda x: get_first_word_after_article(x["title"]))
    return [movie["title"] for movie in sorted_movies]


# print(sort_by_year(movies2))
# Expected test output of function #1
# ["The Intouchables", "Valkyrie", "Stardust", "Ratatouille", "City of God", "Memento", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]

# print(sort_by_title(movies2))
# Expected test output of function #2
# ["Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee", "The Intouchables", "Memento", "Ratatouille", "The Shawshank Redemption", "Stardust", "Valkyrie"]
