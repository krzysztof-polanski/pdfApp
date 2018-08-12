import sqlite3

class DBHelper:
    def connect(self,database='pdf.db'):
        return sqlite3.connect(database)

    def get_all_inputs(self):
        connection = self.connect()
        try:
            query = "SELECT text_box, x0, x1, y0, y1 FROM pdf_info;"
            c = connection.cursor()
            c.execute(query)
            return c.fetchall()
        finally:
            connection.close()

    def add_input(self, data):
        connection = self.connect()
        try:
            query = """INSERT INTO pdf_info (text_box, x0, x1, y0, y1)
                       VALUES (?,?,?,?,?);"""
            c = connection.cursor()
            c.execute(query, data)
            connection.commit()
        finally:
            connection.close()
