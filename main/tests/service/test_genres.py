import pytest
from unittest.mock import MagicMock
from main.dao.model.genre import Genre
from main.dao.genre import GenreDAO
from main.service.genre import GenreService


@pytest.fixture
def genres_dao():
    dao = GenreDAO(None)

    genre1 = Genre(id=1, name='Научная фантастика')
    genre2 = Genre(id=2, name='Боевик')
    genre3 = Genre(id=3, name='Детектив')

    dao.get_one = MagicMock(return_value=genre3)
    dao.get_all = MagicMock(return_value=[genre1, genre2, genre3])
    dao.create = MagicMock(return_value=Genre(id=2))
    dao.update = MagicMock()
    dao.delete = MagicMock()

    return dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, movies_dao):
        self.genre_service = GenreService(dao=movies_dao)

    def test_get_one(self):
        genre = self.genre_service.dao.get_one(2)

        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genre = self.genre_service.dao.get_all()
        assert len(genre) > 0

    def test_create(self):
        new_genre = {
            "name": "Триллер"
        }
        genre_adding = self.genre_service.dao.create(new_genre)

        assert genre_adding.id is not None

    def test_update(self):
        upd_genre = {
            "id": 2,
            "name": "Драмма"
        }
        self.genre_service.dao.update.update(upd_genre)

    def test_delete(self):
        self.genre_service.delete(1)
