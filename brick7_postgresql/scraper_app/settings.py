
BOT_NAME = 'UsedCarsNational'

SPIDER_MODULES = ['scraper_app.spiders']

ITEM_PIPELINES = {'scraper_app.pipelines.CarsNationalPipeline': 100}

DATABASE = {
	'drivername': 'postgres',
	'host': 'localhost',
	'port': '5432',
	'username': 'geoffrey',
	'password': 'SouthernCross',
	'database': 'scrape'
}

#To enable us to follow paths
DEPTH_LIMIT = 2
DEPTH_PRIORITY = 2

#slow down the bot so that it doesn't put too much pressure on the website - actual delay is randomised by default
DOWNLOAD_DELAY = 1.5