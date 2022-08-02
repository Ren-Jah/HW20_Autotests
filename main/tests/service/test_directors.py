import pytest
from unittest.mock import MagicMock
from main.dao.director import DirectorDAO
from main.dao.model.director import Director
from main.service.director import DirectorService


@pytest.fixture
def directors_dao():
    dao = DirectorDAO(None)

    director1 = Director(id=1, name='Квентин Трыньтруньтино')
    director2 = Director(id=2, name='Стенли Кубик-рубик')
    director3 = Director(id=3, name='Кристофер Нулан')

    dao.get_one = MagicMock(return_value=director2)
    dao.get_all = MagicMock(return_value=[director1, director2, director3])
    dao.create = MagicMock(return_value=Director(id=1))
    dao.update = MagicMock()
    dao.delete = MagicMock()

    return dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, movies_dao):
        self.director_service = DirectorService(dao=movies_dao)

    def test_get_one(self):
        director = self.director_service.dao.get_one(2)

        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        director = self.director_service.dao.get_all()
        assert len(director) > 0

    def test_create(self):
        new_director = {
            "name": "Безумный Джордж"
        }
        director_adding = self.director_service.dao.create(new_director)

        assert director_adding.id is not None

    def test_update(self):
        upd_director= {
            "id": 2,
            "name": "Врядли Скотт"
        }
        self.director_service.dao.update.update(upd_director)

    def test_delete(self):
        self.director_service.delete(1)