from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from scraper_app.items import UsedCars

#need to comment out one of the spiders - can only run one spider at a time.

class CarsNationalSpider(CrawlSpider):
    #Spider for regularly updated cars.brick7.co.za website
    name = "UsedCarsNational"
    allowed_domains = ["cars.brick7.co.za"]
    start_urls = ["http://www.cars.brick7.co.za/price"]
	
    rules = [
        Rule(LinkExtractor(restrict_xpaths='//div/div[@class="cat_bg"]/ul[@class="list_col4"]/li/a'), callback="parse_items", follow=True),
		Rule(LinkExtractor(restrict_xpaths='//div/div[@class="cat_bg"]/div[@id="price_list"]/ul[@class="price_list_col2"]/li[@class="pb2"]/ul/li[@class="bold"]/a'), callback="parse_items", follow=True),
    ]
    
    cars_list_xpath = '//div/div[@class="cat_bg"]/div[@class="fl width_70"]/div[@id="price_list"]/ul[@class="price_list_col2"]/li/ul'
    item_fields = {
		'TitleLocation': './/li[@class="li15 bold"]/a/@title',
		'Year': './/li[@class="li15 bold"]/a/text()',
		'Price': './/li[@class="li85"]/text()'
    }
		    
    def parse_items(self, response):
        
        #Default callback used by Scrapy to process downloaded responses
        
        selector = HtmlXPathSelector(response)
		
		#the make and model will be the same for all data on a page 
		#put into try/except so that intermediate car make pages don't give errors 
        try:
			car_make = selector.xpath('//div[@class="bread_cum fl"]/a/text()').extract()[2]
			car_model = selector.xpath('//div[@class="bread_cum fl"]/a/text()').extract()[3]
        except Exception:
			pass
	    
        # iterate over deals
        for CarsNational in selector.xpath(self.cars_list_xpath):
            loader = XPathItemLoader(UsedCars(), selector=CarsNational)

            # define processors
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            # iterate over fields and add xpaths to the loader
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            
            loader.add_value('Make', car_make)
            loader.add_value('Model', car_model)
            
            yield loader.load_item()
"""            
class CarsCitySpider(CrawlSpider):
    #Spider for regularly updated cars.brick7.co.za website
    name = "UsedCarsNational"
    allowed_domains = ["cars.brick7.co.za"]
    start_urls = ["http://www.cars.brick7.co.za/price"]
	
    rules = [
        Rule(LinkExtractor(restrict_xpaths='//div/div[@class="cat_bg"]/ul[@class="list_col4"]/li/a'), callback="parse_items", follow=True),
		Rule(LinkExtractor(restrict_xpaths='//div/div[@class="cat_bg"]/div[@id="price_list"]/ul[@class="price_list_col2"]/li[@class="pb2"]/ul/li[@class="bold"]/a'), callback="parse_items", follow=True),
    ]
    
    car_base_xpath = '//div/div[@class="cat_bg"]/div[@class="fl width_70"]/div[@id="price_list"]/div'
    
    def parse_items(self, response):
        
        #Default callback used by Scrapy to process downloaded responses
        
        selector = HtmlXPathSelector(response)
        CarsCities = selector.xpath('//div/div[@class="cat_bg"]/div[@class="fl width_70"]/div[@id="price_list"]/div')
        
        #the make and model will be the same for all data on a page 
        #put into try/except so that intermediate car make pages don't give errors 
        try:
		    car_make = selector.xpath('//div[@class="bread_cum fl"]/a/text()').extract()[2]
		    car_model = selector.xpath('//div[@class="bread_cum fl"]/a/text()').extract()[3]
        except Exception:
		    pass
			
        # iterate over cars
        for CarsCity in CarsCities:
            
            #the location is only mentioned once for all the years and prices.		
			location_heading = CarsCity.xpath('.//div[@class="pt10"]/h2/a/@title').extract()
			
			for CarsCityLoc in CarsCity.xpath('.//ul/li/ul'):
				loader = XPathItemLoader(UsedCars(), selector=CarsCityLoc)

				# define processors
				loader.default_input_processor = MapCompose(unicode.strip)
				loader.default_output_processor = Join()
            
				loader.add_xpath('Year', './/li[@class="li15 bold"]/text()')
				loader.add_xpath('Price', './/li[@class="li85"]/text()')
				loader.add_value('TitleLocation', location_heading)
				loader.add_value('Make', car_make)
				loader.add_value('Model', car_model)
				
				yield loader.load_item()
"""
