
#from scrapy.contrib.pipeline import images
import os

BOT_NAME = 'Rio'

SPIDER_MODULES = ['scraper_app.spiders']

#To enable us to follow paths
# this should be set to 3 for the new car spiders and around 600 for the used car spiders.
DEPTH_LIMIT = 3
DEPTH_PRIORITY = 3

#slow down the bot so that it doesn't put too much pressure on the website
#actual delay is randomised by default with mean = DOWNLOAD_DELAY
DOWNLOAD_DELAY = 1.5

#image Pipeline
ITEM_PIPELINES = {
   'scrapy.contrib.pipeline.images.FilesPipeline': 1,
}
#image storage location (for image scrapers)
FILES_STORE = "ScrapedCarImages/NewCars"
#FILES_STORE = "ScrapedCarImages/UsedCars"
