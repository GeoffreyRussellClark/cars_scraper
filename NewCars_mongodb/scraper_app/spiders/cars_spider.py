from scrapy import Selector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
import time

from scraper_app.items import NewCarsItem

import logging
logger = logging.getLogger()

class NewCarsSpider(CrawlSpider):

    name = "NewCarsSpider"
    allowed_domains = ["www.cars.co.za"]#don't add "http" otherwise will give "filtered offsite request error"
    start_urls = ["http://www.cars.co.za/newcars"]
	
	#links to be followed stating with the outermost link
    rules = [
        Rule(LinkExtractor(restrict_xpaths='//div[@class="makesDropdown"]/div[@class="dropdown_label"]/div'), callback="parse_items", follow=True),
		Rule(LinkExtractor(allow=(), restrict_xpaths='//div[@class="col_main jq_submit"]/div[@class="box"]'), callback="parse_items", follow=True),
		Rule(LinkExtractor(allow=(), restrict_xpaths='//table[@id="variant_table"]/tbody/tr/td[@style="width:200px;"]/strong/a'), callback="parse_items", follow=True),
		#Rule(LinkExtractor(allow=()), callback="parse_items", follow=True),
    ]
    
    '''cars_list_xpath = '//div/div[@class="cat_bg"]/div[@class="fl width_70"]/div[@id="price_list"]/ul[@class="price_list_col2"]/li/ul'
    item_fields = {
		'price': './/li[@class="li85"]/text()',
		'intro_date' = 
		'model_intro_date' = 
    }'''
		    
    def parse_items(self, response):
        
        #Default callback used by Scrapy to process downloaded responses
        
        selector = Selector(response)
		
        
        #the make and model and version will be the same for all data on a page 
		#put into try/except so that intermediate car make pages don't give errors 
        try:
			car_make = selector.xpath('//div[@id="breadcrumb"]/ul/li/a/text()').extract()[2]
			car_model = selector.xpath('//div[@id="breadcrumb"]/ul/li[@class="second-last"]/a/text()').extract()
			car_version = selector.xpath('//div[@id="breadcrumb"]/ul/li[@class="last"]/text()').extract()
			#car_price = selector.xpath('//div[@id="details"]/div[@class="left"]/div[@class="box vehicledetails"]/div[@class="price black"]/text()').extract()
						
        except Exception:
			pass
	    #after features: 53. 40 after warranty. 93
	    #after features: 83. 42 after warranty. 125
	    #after features: 60. 34 after warranty. 94
		
        # iterate over cars
        for NewCarsSelector in selector.xpath('//div[@id="details"]/div[@class="left"]/div[@class="box vehicledetails"]'):
			loader = ItemLoader(NewCarsItem(), selector=NewCarsSelector)

			# define processors
			loader.default_input_processor = MapCompose(unicode.strip)
			loader.default_output_processor = Join()
			
			loader.add_value('make', car_make)
			loader.add_value('model', car_model)
			loader.add_value('version', car_version)
			loader.add_xpath('price', './/div[@class="price black"]/text()')
			loader.add_value('curr_date', unicode(time.strftime("%Y/%m/%d"),"utf-8"))
			
			field_counter = 1
			break_ind = False
			for i in range(2,11):
				field_data = selector.xpath('//div[@class="box vehicledetails"]/div[@class="box"]/div[@class="tab_panels"]/div[@id="tabs-'+str(i)+'"]/table[@class="table"]')
				
				
				fNameValue = []
				for i_data in field_data.xpath('.//td/text()'):
					f = i_data.extract()
					#if the value is actually a tick then rather make the value something easier to work with later on.
					if f == u'\u2714':
						f = u'true'
					fNameValue.append(f) 
								
				odd_ind = True
				for nameValue in fNameValue:
					if odd_ind:
						loader.add_value('f'+str(field_counter)+'name', nameValue)
						odd_ind = False
					else:
						loader.add_value('f'+str(field_counter)+'value', nameValue)
						odd_ind = True
						field_counter = int(field_counter) + 1
						if field_counter > 150:#this number is the max number of items that we can have.
							break_ind = True
							break
				
				if break_ind == True:
					break
			#fname = field_data.xpath('.//td/text()').extract()[0]
			#fvalue = field_data.xpath('.//td/text()').extract()[1]
			
			yield loader.load_item()
			
			
