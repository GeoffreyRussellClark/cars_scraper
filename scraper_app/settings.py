
BOT_NAME = 'UsedCarsNational'

SPIDER_MODULES = ['scraper_app.spiders']

ITEM_PIPELINES = ['scraper_app.pipelines.CarsNationalPipeline']

DATABASE = {
	'drivername': 'postgres',
	'host': 'localhost',
	'port': '5432',
	'username': 'geoffrey',
	'password': 'SouthernCross',
	'database': 'scrape'
}

#To enable us to follow paths
DEPTH_LIMIT = 1
DEPTH_PRIORITY = 1

#slow down the bot so that it doesn't put too much pressure on the website
DOWNLOAD_DELAY = 2
#RANDOMIZE_DOWNLOAD_DELAY
