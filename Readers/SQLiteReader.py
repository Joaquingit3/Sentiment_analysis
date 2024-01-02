import sqlite3


# Clase SQLite Reader para leer una base de datos SQLite
class SQLiteReader:
    # Función constructora
    def __init__(self):
        self.connection = None
        self.cursor = None

    # Metodo connect para conectarte con la bbdd aportada
    def connect(self, path_db):
        self.connection = sqlite3.connect(path_db)
        self.cursor = self.connection.cursor()

    # Metodo close para cerrar la conexión con la bbdd
    def close(self):
        self.connection.close()

    # Metod read para ejecutar un query en la bbdd y obtener los resultados
    def read(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()


