import pytest
from comparison_sort.comparison_sort import sort_by_title, sort_by_year
from comparison_sort._movies import movies, movies2


# @pytest.mark.skip("TODO")
def test_sort_by_year_normal():
    # Test normal case
    assert sort_by_year(movies) == ["The Intouchables", "Valkyrie", "Stardust", "Ratatouille", "City of God", "Memento", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]

# @pytest.mark.skip("TODO")
def test_sort_by_year_duplicate():
    # Test edge case with duplicate years
    movies_with_duplicate_years = movies + [{"title": "Another Movie", "year": 2008, "genres": ["Drama"]}]
    assert sort_by_year(movies_with_duplicate_years) == ["The Intouchables", "Valkyrie", "Another Movie", "Stardust", "Ratatouille", "City of God", "Memento", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]

# @pytest.mark.skip("TODO")
def test_sort_by_year_empty():
    # Test edge case with no movies
    assert sort_by_year([]) == []

# @pytest.mark.skip("TODO")
def test_sort_by_year_special_chars():
    assert sort_by_year(movies2) == [
        "The 100-Year-Old Man Who Climbed Out the Window and Disappeared", "The Intouchables", "Valkyrie",
        "Stardust", "Ratatouille", "3:10 to Yuma", "City of God", "Memento", "The 5th Element", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"
    ]

# @pytest.mark.skip("TODO")
def test_sort_by_title_normal():
    # Test normal case
    assert sort_by_title(movies) == ["Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee", "The Intouchables", "Memento", "Ratatouille", "The Shawshank Redemption", "Stardust", "Valkyrie"]

# @pytest.mark.skip("TODO")
def test_sort_by_title_no_leading_article():
    # Test edge case with no leading articles
    movies_without_articles = [{"title": "Zoo", "year": 2008, "genres": ["Drama"]}, {"title": "Apple", "year": 2010, "genres": ["Comedy"]}]
    assert sort_by_title(movies_without_articles) == ["Apple", "Zoo"]

# @pytest.mark.skip("TODO")
def test_sort_by_title_empty():
    # Test edge case with no movies
    assert sort_by_title([]) == []

# @pytest.mark.skip("TODO")
def test_sort_by_title_special_chars():
    assert sort_by_title(movies2) == [
        'The 100-Year-Old Man Who Climbed Out the Window and Disappeared', '3:10 to Yuma', 'The 5th Element', 'Beetlejuice', 'City of God', 'The Cotton Club', 'Crocodile Dundee', 'The Intouchables', 'Memento', 'Ratatouille', 'The Shawshank Redemption', 'Stardust', 'Valkyrie'
        ]
