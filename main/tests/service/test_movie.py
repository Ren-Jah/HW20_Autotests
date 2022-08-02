import pytest
from unittest.mock import MagicMock
from main.dao.model.movie import Movie
from main.dao.movie import MovieDAO
from main.service.movie import MovieService


@pytest.fixture
def movies_dao():
    movies_dao = MovieDAO(None)

    movie1 = Movie(id=1, title='Movie42')
    movie2 = Movie(id=2, title='Tests of tests')
    movie3 = Movie(id=3, title='some movie')

    movies_dao.get_one = MagicMock(return_value=movie1)
    movies_dao.get_all = MagicMock(return_value=[movie1, movie2, movie3])
    movies_dao.create = MagicMock(return_value=Movie(id=3))
    movies_dao.update = MagicMock()
    movies_dao.delete = MagicMock()

    return movies_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movies_dao):
        self.movies_service = MovieService(dao=movies_dao)

    def test_get_one(self):
        movie = self.movies_service.dao.get_one(2)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movie = self.movies_service.dao.get_all()
        assert len(movie) > 0

    def test_create(self):
        new_movie = {
            "title": "Definitely new movie"
        }
        movie_adding = self.movies_service.dao.create(new_movie)

        assert movie_adding.id is not None

    def test_update(self):
        upd_movie = {
            "id": 3,
            "title": "New some movie"
        }
        self.movies_service.dao.update.update(upd_movie)

    def test_delete(self):
        self.movies_service.delete(1)

