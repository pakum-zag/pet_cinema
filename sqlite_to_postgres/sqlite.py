import sqlite3

from data_types import FilmWork, Genre

CHUNK = 500


def _dict_factory(cursor, row):
    """
    Парсинг данных из SQLite в виде словаря
    """
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def _modify_parsed_row(data_row: dict) -> dict:
    """
    Модификация строки при парсинге из таблицы
    """
    if data_row.get('created_at'):
        data_row['created'] = data_row.pop('created_at')
    if data_row.get('updated_at'):
        data_row['modified'] = data_row.pop('updated_at')
    return data_row


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
            try:
                if item.get('description') is None:
                    item['description'] = ''
                if item.get('rating') is None:
                    item['rating'] = 0.0
                item.pop('file_path')
            except:
                pass
        elif table_dataclass == Genre:
            if item.get('description') is None:
                item['description'] = ''
        d.append(table_dataclass(**_modify_parsed_row(item)))
    return d


def create_sqlite_cursor(sqlite_connection: sqlite3.Connection):
    """Основной метод загрузки данных из SQLite в Postgres"""
    sqlite_connection.row_factory = _dict_factory
    return sqlite_connection.cursor()
