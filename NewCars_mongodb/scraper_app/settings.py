
#from scrapy.contrib.pipeline import images
import os

BOT_NAME = 'CarsBot'

SPIDER_MODULES = ['scraper_app.spiders']

#To enable us to follow paths
# this should be set to 3 for the new car spiders and around 600 for the used car spiders.
DEPTH_LIMIT = 3
DEPTH_PRIORITY = 3

#slow down the bot so that it doesn't put too much pressure on the website - actual delay is randomised by default
DOWNLOAD_DELAY = 1.2

#Postgresql Pipeline
'''ITEM_PIPELINES = {'scraper_app.pipelines.NewCarsPipeline': 100}

DATABASE = {
	'drivername': 'postgres',
	'host': 'localhost',
	'port': '5432',
	'username': 'geoffrey',
	'password': 'SouthernCross',
	'database': 'scrape'
}'''

#Mongo Pipeline
'''ITEM_PIPELINES = {'scraper_app.pipelines.MongoPipeline': 100}

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "scrape"
MONGODB_COLLECTION = "new_carscoza"'''


#image Pipeline
ITEM_PIPELINES = {
   'scrapy.contrib.pipeline.images.FilesPipeline': 1,
}
#image storage location (for image scrapers)
#FILES_STORE = "ScrapedCarImages/NewCars"
#FILES_STORE = "ScrapedCarImages/UsedCars"
FILES_STORE = "ScrapedCarImages/UsedCarsAT"

