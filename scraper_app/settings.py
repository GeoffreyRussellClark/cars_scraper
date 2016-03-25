
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
