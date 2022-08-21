import pytest
from unittest.mock import MagicMock

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    d1 = Director(id=1, name="Jonh")
    d2 = Director(id=2, name="Alex")
    d3 = Director(id=3, name="Sasha")

    director_dao.get_one = MagicMock(return_value=d1)
    director_dao.get_all = MagicMock(return_value=[d1, d2])
    director_dao.create = MagicMock(return_value=d3)
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    g1 = Genre(id=1, name="Action")
    g2 = Genre(id=2, name="Horror")
    g3 = Genre(id=3, name="Documentary")

    genre_dao.get_one = MagicMock(return_value=g1)
    genre_dao.get_all = MagicMock(return_value=[g1, g2])
    genre_dao.create = MagicMock(return_value=g3)
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    m1 = Movie(id=1, title="Harry Potter", description='Family Movie', year=2020)
    m2 = Movie(id=2, title="Star Wars", year=2019, rating=10)
    m3 = Movie(id=3, title="Pulp Fiction", genre_id=1, trailer='s7EdQ4FqbhY')

    movie_dao.get_one = MagicMock(return_value=m1)
    movie_dao.get_all = MagicMock(return_value=[m1, m2])
    movie_dao.create = MagicMock(return_value=m3)
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao



