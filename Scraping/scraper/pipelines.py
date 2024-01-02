import sqlite3
from . items import ArticleItem
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# Clase para calcular el sentimiento del article procesandolo
class SentimentIntensityAnalyzerPipeline:
    def process_article(item):
        # Definimos el objeto Analyzer
        analyzer = SentimentIntensityAnalyzer()

        # Calculamos el sentimiento de la frase con el polarity_scores
        sentiment = analyzer.polarity_scores(item['content'])

        # Redefinimos el campos sentiment de item como el compound de sentiment
        item['sentiment'] = sentiment['compound']

        return item


# Clase para la creación de la bbdd insertando nuevos articulos
class SQLitePipeline:
    # Metodo para Conectarse a la bbdd
    def open_spider(self, spider):
        path_db = 'news_analyzer.db'
        self.connection = sqlite3.connect(path_db)
        self.cursor = self.connection.cursor()

    # Metodo para cerrar la conexión con la bbdd
    def close_spider(self, spider):
        self.connection.close()

    # Metodo para revisar que un articulo este en la bbdd
    def article_exists(self, url):
        # Revisar la bbdd si esta definida la url
        self.cursor.execute("SELECT * FROM articles WHERE url=?", (url,))

        # Devolvemos fetchone si existe sino None
        return self.cursor.fetchone() is not None

    # Metodo para añadir un artículo a la bbdd
    def insert_article(self, item):
        # Insertar el artículo con la info de item
        self.cursor.execute("""
            INSERT INTO articles (url, title, author, datetime, content, sentiment)
            VALUES (?,?,?,?,?,?)
            """, (
                item['url'],
                item['title'],
                item['author'],
                item['datetime'],
                item['content'],
                item['sentiment']
            ))

        # Hacer el commit
        self.connection.commit()

    # Metodo para procesar un item
    def process_item(self, item, spider):
        # Chequear si el item es del tipo de la clase ArticleItem
        if isinstance(item, ArticleItem):
            # Revisar que el artículo no esté en la bbdd
            if not self.article_exists(item['url']):
                # Calculamos su sentimiento
                item = SentimentIntensityAnalyzerPipeline.process_article(item)

                # Insertamos el artículo nuevo a la bbdd
                self.insert_article(item)

        return item
