import pandas as pd


# Clase DataFrameReader que lée un Dataframe
class DataFrameReader:
    # Función constructora
    def __init__(self, filename):
        self.filename = filename
        self.data = None

    # Metodo de lectura
    def read(self):
        self.data = pd.read_csv(self.filename)
        return self.data

    # Metodo format para aplicar un formatter input
    def format(self, formatter):
        self.data = formatter(self.data)
        return self.data