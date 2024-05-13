import sqlite3

from data_types import FilmWork, Genre

CHUNK = 500


def _dict_factory(cursor, row):
    """
    Парсинг данных из SQLite в виде словаря
    """
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}


def _modify_parsed_row(data_row: dict) -> dict:
    """
    Модификация строки при парсинге из таблицы
    """
    modify_data = data_row.copy()
    if data_row.get("created_at"):
        modify_data["created"] = data_row["created_at"]
    if data_row.get("updated_at"):
        modify_data["modified"] = data_row["updated_at"]
    modify_data["release_date"] = data_row.get("creation_date")
    return modify_data


def cursor_execute_query(cursor, table_name):
    """
    Выполняет запрос выборки всех данных из БД
    """
    cursor.execute("SELECT * FROM {0};".format(table_name))


def load_data_from_sqlite_table(cursor, table_dataclass):
    """
    Получение данных из запроса
    """
    d = []
    for item in cursor.fetchmany(CHUNK):
        if table_dataclass == FilmWork:
            item["description"] = item.get("description") or ""
            item["rating"] = item.get("rating") or 0.0
        elif table_dataclass == Genre:
            item["description"] = item.get("description") or ""
        d.append(table_dataclass.from_dict(_modify_parsed_row(item)))
    return d


def create_sqlite_cursor(sqlite_connection: sqlite3.Connection):
    """Основной метод загрузки данных из SQLite в Postgres"""
    sqlite_connection.row_factory = _dict_factory
    return sqlite_connection.cursor()
