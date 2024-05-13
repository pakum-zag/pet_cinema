import sqlite3
from contextlib import closing, contextmanager

import psycopg2
from psycopg2.extras import DictCursor

from data_types import FilmWork, Genre, Person, GenreFilmWork, PersonFilmWork
from postgres import insert_data_to_postgres_table, PG_DSL
from sqlite import (
    create_sqlite_cursor,
    load_data_from_sqlite_table,
    cursor_execute_query,
)


@contextmanager
def get_connection():
    with closing(sqlite3.connect("db.sqlite")) as sqlite_conn, closing(
        psycopg2.connect(**PG_DSL, cursor_factory=DictCursor)
    ) as pg_conn:
        with pg_conn, pg_conn.cursor() as pg_cursor:
            yield sqlite_conn, pg_cursor


# Скрипт предполагает, что таблицы были ранее созданы
# Для переноса данных в пустую БД, стоит запустить SQL скрипт из файла schema_design/schema.ddl
if __name__ == "__main__":
    with get_connection() as (sqlite_conn, pg_cursor):
        table_dataclases = [
            FilmWork,
            Genre,
            GenreFilmWork,
            Person,
            PersonFilmWork,
        ]
        sqlite_cursor = create_sqlite_cursor(sqlite_conn)
        for table_dataclass in table_dataclases:
            cursor_execute_query(sqlite_cursor, table_dataclass.get_table_name())
            while data := load_data_from_sqlite_table(sqlite_cursor, table_dataclass):
                insert_data_to_postgres_table(pg_cursor, data, table_dataclass)
    print("Done")
