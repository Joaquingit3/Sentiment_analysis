import scrapy


# Clase ArticleItem para la conversión interna a un objeto de scrapy
class ArticleItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    datetime = scrapy.Field()
    content = scrapy.Field()
    sentiment = scrapy.Field()
