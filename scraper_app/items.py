from scrapy.item import Item, Field

class UsedCars(Item):
    """UsedCars container (dictionary-like object) for scraped data"""
    MakeModelLocation = Field()
    Year = Field()
    Price = Field()
