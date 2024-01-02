import pandas as pd


# Clase para dar formato a datos OHLCV (Open High Low Close Volume)
class OHLCVFormatter:
    # Metodo format, para dar el formato correcto al df
    def format(self, df):
        # Limpiamos los NA
        df = df.dropna()

        # Renombramos las columnas
        columnas = ["datetime", "symbol", "open", "high", "low", "close", "volume"]
        df.columns = columnas

        # Cambiamos el tipo a la columna 'datetime' por datetime
        df["datetime"] = pd.to_datetime(df["datetime"])

        # Ajustamos datetime para no tener días
        df["datetime"] = df["datetime"].dt.floor("D")

        # Asignamos como indice del df la columna 'datetime'
        df = df.set_index("datetime")

        # Devolvemos df con solo unas columnas importantes
        return df[["open", "high", "low", "close", "volume"]]