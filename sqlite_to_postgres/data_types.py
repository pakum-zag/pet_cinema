import inspect
import uuid
from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class FilmWorkType(Enum):
    MOVIE = 'movie'
    TV_SHOW = 'tv_show'

    @classmethod
    def as_choices(cls):
        return (
            (cls.MOVIE.value, "Кино"),
            (cls.TV_SHOW.value, "ТВ шоу"),
        )


@dataclass
class GenericTable:
    id: uuid

    @staticmethod
    def get_constrain_fields():
        return 'id'

    @classmethod
    def from_dict(cls, env):
        return cls(**{
            k: v for k, v in env.items()
            if k in inspect.signature(cls).parameters
        })


@dataclass
class GenericCreatedClass:
    created: datetime


@dataclass
class GenericModifiedClass:
    modified: datetime


@dataclass
class FilmWork(GenericTable, GenericCreatedClass, GenericModifiedClass):
    title: str
    release_date: datetime.date
    type: FilmWorkType
    rating: float = 0.0
    description: str = ''

    @staticmethod
    def get_table_name():
        return 'film_work'


@dataclass
class Genre(GenericTable, GenericCreatedClass, GenericModifiedClass):
    name: str
    description: str = ''

    @staticmethod
    def get_table_name():
        return 'genre'


@dataclass
class GenreFilmWork(GenericTable, GenericCreatedClass):
    genre_id: uuid
    film_work_id: uuid

    @staticmethod
    def get_table_name():
        return 'genre_film_work'


@dataclass
class Person(GenericTable, GenericCreatedClass, GenericModifiedClass):
    full_name: str

    @staticmethod
    def get_table_name():
        return 'person'


@dataclass
class PersonFilmWork(GenericTable, GenericCreatedClass):
    film_work_id: uuid
    person_id: uuid
    role: str

    @staticmethod
    def get_table_name():
        return 'person_film_work'

    @staticmethod
    def get_constrain_fields():
        return 'film_work_id, person_id, role'
