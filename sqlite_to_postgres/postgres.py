import os
from dataclasses import fields, astuple

from dotenv import load_dotenv

load_dotenv()

PG_DSL = {
    'dbname': os.environ.get('dbname') or 'movies_database',
    'user': os.environ.get('user') or 'app',
    'password': os.environ.get('password') or '123qwe',
    'host': os.environ.get('host') or '127.0.0.1',
    'port': os.environ.get('port') or 5432
}


def insert_data_to_postgres_table(pg_cursor, table_data, table_dataclass):
    """
    Импорт данных в конкретную таблицу
    """
    records_list_template = ','.join(['%s'] * len(table_data))
    query = """
        INSERT INTO content.{0} ({1})
        VALUES {2}
        ON CONFLICT ({3}) DO NOTHING;
    """.format(
        table_dataclass.get_table_name(),
        ",".join([str(field.name) for field in fields(table_dataclass)]),
        records_list_template,
        table_dataclass.get_constrain_fields()
    )
    pg_cursor.execute(query, [astuple(row) for row in table_data])
