#from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose
from scrapy.contrib.spiders import CrawlSpider, Rule
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor

from scraper_app.items import UsedCars

class CarsNationalSpider(CrawlSpider):
    """Spider for regularly updated cars.brick7.co.za website"""
    name = "UsedCarsNational"
    allowed_domains = ["cars.brick7.co.za"]
    start_urls = ["http://www.cars.brick7.co.za/price/honda/"]
	
    rules = [
		Rule(LinkExtractor(restrict_xpaths='//div/div[@class="cat_bg"]/div[@id="price_list"]/ul[@class="price_list_col2"]/li[@class="pb2"]/ul/li[@class="bold"]/a'), callback="parse_items", follow=True),
    ]

    cars_list_xpath = '//div/div[@class="cat_bg"]/div[@class="fl width_70"]/div[@id="price_list"]/ul[@class="price_list_col2"]/li/ul'
    item_fields = {
		'MakeModelLocation': './/li[@class="li15 bold"]/a/@title',
		'Year': './/li[@class="li15 bold"]/a/text()',
		'Price': './/li[@class="li85"]/text()'
    }

    def parse_items(self, response):
        """
        Default callback used by Scrapy to process downloaded responses

        Testing contracts:
        @url http://www.livingsocial.com/cities/15-san-francisco
        @returns items 1
        @scrapes title link

        """
        selector = HtmlXPathSelector(response)

        # iterate over deals
        for CarsNational in selector.xpath(self.cars_list_xpath):
            loader = XPathItemLoader(UsedCars(), selector=CarsNational)

            # define processors
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            # iterate over fields and add xpaths to the loader
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()
