
BOT_NAME = 'CarsBot'

SPIDER_MODULES = ['scraper_app.spiders']

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


#To enable us to follow paths
DEPTH_LIMIT = 550
DEPTH_PRIORITY = 1

#slow down the bot so that it doesn't put too much pressure on the website - actual delay is randomised by default
DOWNLOAD_DELAY = 1.5
