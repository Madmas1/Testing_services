import pytest

from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert isinstance(movie.id, int)
        assert movie.title == "Harry Potter"
        assert movie.description == "Family Movie"
        assert movie.year == 2020

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        data = {'title': "New Movie"}
        new_movie = self.movie_service.create(data)
        assert new_movie.id is not None
        assert new_movie.title == "Pulp Fiction"
        assert new_movie.genre_id == 1
        assert new_movie.trailer == "s7EdQ4FqbhY"

    def test_update(self):
        self.movie_service.update(1)

    def test_delete(self):
        res = self.movie_service.delete(1)
        assert res is None