import datetime


# Clase Article casteando el formato de sus parámetros
class Article:
    # Función constructora
    def __init__(self,
                 id: int,
                 url: str,
                 title: str,
                 author: str,
                 datetime: datetime.datetime,
                 content: str,
                 sentiment: float):
        self.id = id
        self.url = url
        self.title = title
        self.author = author
        self.datetime = datetime
        self.content = content
        self.sentiment = sentiment
    '''
    -------------------- Version anterior de la función constructora --------------------------
    def __init__(self,
                 url: str,
                 title: str,
                 author: str,
                 datetime: datetime.datetime,
                 content: str,
                 confidence: float,
                 sentiment: float):
        self.url = url
        self.title = title
        self.author = author
        self.datetime = datetime
        self.content = content
        self.confidence = confidence
        self.sentiment = sentiment
    '''
