import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print e
    return None


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print e


def run():
    database = 'pdf.db'
    sql_create_pdf_table = """ CREATE TABLE IF NOT EXISTS pdf_info (
                                    id integer PRIMARY KEY,
                                    text_box text NOT NULL,
                                    x0 float NOT NULL,
                                    x1 float NOT NULL,
                                    y0 float NOT NULL,
                                    y1 float NOT NULL
                                    );"""

    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_pdf_table)
    else:
        print "Connection Error"


if __name__ == '__main__':
    run()
