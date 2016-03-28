from scrapy.item import Item, Field

class UsedCars(Item):
    """UsedCars container (dictionary-like object) for scraped data"""
    Make = Field()
    Model = Field()
    TitleLocation = Field()
    Year = Field()
    Price = Field()
