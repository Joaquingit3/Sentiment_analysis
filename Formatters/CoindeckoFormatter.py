import pandas as pd
import re
import datetime


# Clase para dar el formato correcto a los datos extraídos de Coindecko
class CoindeckoFormatter:
    # Metodo para dar el formato correcto a la fecha v1
    def format_date(date_str):
        # Split date en 3 trozos
        date_split = date_str.split(' ')

        # Seleccion de fecha y hora
        fecha = date_split[0]
        hora = date_split[1]

        # Extraer año, mes y dia de fecha
        fecha_split = fecha.split('-')
        year = int(fecha_split[0])
        month = int(fecha_split[1])
        day = int(fecha_split[2])

        # Return la fecha en formato datetime
        return datetime.datetime(year, month, day)

    # Metodo para dar el formato correcto a la fecha v2
    def format_date2(date_str):
        # Quitar UTC de date_str
        date_str = re.sub(' UTC', '', date_str)

        # Definimos el formato esperado
        date_format = "%Y-%m-%d %H:%M:%S"

        return datetime.datetime.strptime(date_str, date_format)

    # Metodo principal para dar formato correcto al DF
    def format(self, df):
        # Limpiamos los NA
        df = df.dropna()

        # Renombramos las columnas
        columnas = ["datetime", "price", "market_cap", "total_volume"]
        df.columns = columnas

        # Cambiamos el tipo a la columna 'datetime' por datetime
        #df["datetime"] = pd.to_datetime(df["datetime"])
        df["datetime"] = df["datetime"].apply(lambda x: CoindeckoFormatter.format_date2(x))

        # Ajustamos las horas a '00:00:00'
        df["datetime"] = df["datetime"].dt.floor("D")

        # Asignamos como indice del df la columna 'datetime'
        df = df.set_index("datetime")

        # Devolvemos df con solo unas columnas importantes
        return df[["price", "market_cap", "total_volume"]]