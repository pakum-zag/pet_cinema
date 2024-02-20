import os
from dataclasses import fields, astuple
from environs import Env

env = Env()
env.read_env()

PG_DSL = {
    'dbname': env.str('dbname', 'movies_database'),
    'user': env.str('user', 'app'),
    'password': env.str('password', '123qwe'),
    'host': env.str('host', '127.0.0.1'),
    'port': env.int('port', 5432)
}


def insert_data_to_postgres_table(pg_cursor, table_data, table_dataclass):
    """
    Импорт данных в конкретную таблицу
    """
    records_list_template = ','.join(['%s'] * len(table_data))
    query = f"""
        INSERT INTO content.{table_dataclass.get_table_name()} ({",".join([str(field.name) for field in fields(table_dataclass)])})
        VALUES {records_list_template}
        ON CONFLICT ({table_dataclass.get_constrain_fields()}) DO NOTHING;
    """
    pg_cursor.execute(query, [astuple(row) for row in table_data])
