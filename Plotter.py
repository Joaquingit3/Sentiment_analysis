import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots


class Plotter:
    def plot_candlestick_and_articles(candlesticks, articles):
        # Generar subplots
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.02)

        # Añadir el grafico de velas
        fig.add_trace(go.Candlestick(x=candlesticks.index,
                                     open=candlesticks['open'],
                                     high=candlesticks['high'],
                                     low=candlesticks['low'],
                                     close=candlesticks['close']), row=1, col=1)


        # Añadir los artículos
        for article in articles:
            fig.add_trace(go.Scatter(x=[article.datetime],
                                     y=[article.sentiment],
                                     text=[article.title],
                                     mode="markers",
                                     marker=dict(
                                         color="red",
                                         size=article.confidence * 100,
                                         opacity=0.8,
                                         line=dict(
                                             color='DarkSlateGrey',
                                             width=1
                                         )
                                     )), row=2, col=1)
        # Ejes y titulos
        fig.update_yaxes(title_text='Precio ($)', row=1, col=1)
        fig.update_yaxes(title_text='Sentimiento', row=2, col=1)
        fig.update_xaxes(title_text='Fecha', row=2, col=1)
        fig.update_layout(title_text='Precio de Bitcoin con el Sentimiento de las noticias', title_font_size=25,
                          xaxis_rangeslider_visible=False)

        # Mostramos la figura
        fig.show()