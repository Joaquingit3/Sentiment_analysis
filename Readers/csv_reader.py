import csv


# Clase CSVReader para leer los .csv
class CSVReader:
    # Funcion constructora
    def __init__(self, filename):
        self.filename = filename
        self.data = None

    # Metodo de lectura
    def read(self):
        # Abrir el archivo, leerlo y guardarlo en listas
        with open(self.filename, 'r', newline='') as f:
            reader = csv.reader(f, delimiter=';')
            self.data = [row for row in reader]

        return self.data

    # Metodo format que aplica un formatter
    def format(self, formatter):
        self.data = formatter(self.data)
        return self.data

