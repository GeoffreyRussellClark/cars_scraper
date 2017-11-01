from scrapy import Selector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
import time

from scraper_app.items import NewCarsItem
from scraper_app.items import NewCarsImagesItem
from scraper_app.items import UsedCarsItem
from scraper_app.items import UsedCarsImagesItem

class UsedCarsSpider(CrawlSpider):

    name = "UsedCarsSpider"
    allowed_domains = ["www.cars.co.za"]#don't add "http" otherwise will give "filtered offsite request error"
    start_urls = ["http://www.cars.co.za/usedcars.php"]

	#links to be followed stating with the outermost link
    rules = [
        Rule(LinkExtractor(restrict_xpaths='//div[@class="dropdown_label used"]/div[2]'), callback="parse_items", follow=True),
		Rule(LinkExtractor(allow=(), restrict_xpaths='//div[@id="results"]/div[@class="item clearfix"]/div[@class="left_block"]/h2/a'), callback="parse_items", follow=True),
		Rule(LinkExtractor(allow=(), restrict_xpaths='//div[@class="box box-tighter clearfix"]/ul[@class="pagination pagination_right"]/li[@class="next"]/a'), callback="parse_items", follow=True),
		#Rule(LinkExtractor(allow=()), callback="parse_items", follow=True), #this will follow all links found
    ]


    def parse_items(self, response):

        #Default callback used by Scrapy to process downloaded responses
        selector = Selector(response)

        #the make and model and version will be the same for all data on a page
		#put into try/except so that intermediate car make pages don't give errors
        try:
			car_make = selector.xpath('//div[@id="breadcrumb"]/ul/li/a/text()').extract()[2]
			car_model = selector.xpath('//div[@id="breadcrumb"]/ul/li[@class="second-last"]/a/text()').extract()
			car_description = selector.xpath('//div[@id="breadcrumb"]/ul/li[@class="last"]/text()').extract()
			car_price = selector.xpath('//div[@id="details"]/div[@class="left"]/div[@class="box vehicledetails"]/div[@class="price"]/text()').extract()
        except Exception:
			pass

        # iterate over cars
        for UsedCarsSelector in selector.xpath('//div[@id="details"]/div[@class="left"]/div[@class="box vehicledetails"]/table[1]'):
			loader = ItemLoader(UsedCarsItem(), selector=UsedCarsSelector)

			# define processors
			loader.default_input_processor = MapCompose(unicode.strip)
			loader.default_output_processor = Join()

			loader.add_value('make', car_make)
			loader.add_value('model', car_model)
			loader.add_value('description', car_description)
			loader.add_value('price', car_price)
			loader.add_value('curr_date', unicode(time.strftime("%Y/%m/%d"),"utf-8"))

			try:
				loader.add_xpath('f1name', './/tr[1]/td[1]/label/text()')
				loader.add_xpath('f1value', './/tr[1]/td[2]/text()')
				loader.add_xpath('f2name', './/tr[2]/td[1]/label/text()')
				loader.add_xpath('f2value', './/tr[2]/td[2]/text()')
				loader.add_xpath('f3name', './/tr[3]/td[1]/label/text()')
				loader.add_xpath('f3value', './/tr[3]/td[2]/text()')
				loader.add_xpath('f4name', './/tr[4]/td[1]/label/text()')
				loader.add_xpath('f4value', './/tr[4]/td[2]/text()')
				loader.add_xpath('f5name', './/tr[5]/td[1]/label/text()')
				loader.add_xpath('f5value', './/tr[5]/td[2]/text()')
				loader.add_xpath('f6name', './/tr[6]/td[1]/label/text()')
				loader.add_xpath('f6value', './/tr[6]/td[2]/text()')
				loader.add_xpath('f7name', './/tr[7]/td[1]/label/text()')
				loader.add_xpath('f7value', './/tr[7]/td[2]/text()')
				loader.add_xpath('f8name', './/tr[8]/td[1]/label/text()')
				loader.add_xpath('f8value', './/tr[8]/td[2]/text()')
				loader.add_xpath('f9name', './/tr[9]/td[1]/label/text()')
				loader.add_xpath('f9value', './/tr[9]/td[2]/text()')
				loader.add_xpath('f10name', './/tr[10]/td[1]/label/text()')
				loader.add_xpath('f10value', './/tr[10]/td[2]/text()')
				loader.add_xpath('f11name', './/tr[11]/td[1]/label/text()')
				loader.add_xpath('f11value', './/tr[11]/td[2]/text()')
				loader.add_xpath('f12name', './/tr[12]/td[1]/label/text()')
				loader.add_xpath('f12value', './/tr[12]/td[2]/text()')
			except Exception:
				pass

			yield loader.load_item()


#NewCarsSpider
class NewCarsSpider(CrawlSpider):

    name = "NewCarsSpider"
    allowed_domains = ["www.cars.co.za"]#don't add "http" otherwise will give "filtered offsite request error"
    start_urls = ["http://www.cars.co.za/newcars"]

	#links to be followed stating with the outermost link
    rules = [
        Rule(LinkExtractor(restrict_xpaths='//div[@class="makesDropdown"]/div[@class="dropdown_label"]/div'), callback="parse_items", follow=True),
		Rule(LinkExtractor(allow=(), restrict_xpaths='//div[@class="col_main jq_submit"]/div[@class="box"]'), callback="parse_items", follow=True),
		Rule(LinkExtractor(allow=(), restrict_xpaths='//table[@id="variant_table"]/tbody/tr/td[@style="width:200px;"]/strong/a'), callback="parse_items", follow=True),
		#Rule(LinkExtractor(allow=()), callback="parse_items", follow=True), #this will follow all links found
    ]

    def parse_items(self, response):

        #Default callback used by Scrapy to process downloaded responses
        selector = Selector(response)

        #the make and model and version will be the same for all data on a page
		#put into try/except so that intermediate car make pages don't give errors
        try:
			car_make = selector.xpath('//div[@class="breadcrumb-bar"]/div[@class="container"]/ul/li/a/text()').extract()[2]
			car_model = selector.xpath('//div[@class="breadcrumb-bar"]/div[@class="container"]/ul/li[@class="second-last"]/a/text()').extract()
			car_version = selector.xpath('//div[@class="breadcrumb-bar"]/div[@class="container"]/ul/li[@class="last"]/text()').extract()
        except Exception:
			pass

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

			yield loader.load_item()



class UsedCarsImageSpider(CrawlSpider):

    name = "UsedCarsImageSpider"
    allowed_domains = ["www.cars.co.za"]#don't add "http" otherwise will give "filtered offsite request error"
    start_urls = ["http://www.cars.co.za/usedcars.php"]

	#links to be followed stating with the outermost link
    rules = [
        Rule(LinkExtractor(restrict_xpaths='//div[@class="dropdown_label used"]/div[2]'), callback="parse_items", follow=True),
		Rule(LinkExtractor(allow=(), restrict_xpaths='//div[@id="results"]/div[@class="item clearfix"]/div[@class="left_block"]/h2/a'), callback="parse_items", follow=True),
		Rule(LinkExtractor(allow=(), restrict_xpaths='//div[@class="box box-tighter clearfix"]/ul[@class="pagination pagination_right"]/li[@class="next"]/a'), callback="parse_items", follow=True),
		#Rule(LinkExtractor(allow=()), callback="parse_items", follow=True), #this will follow all links found
    ]


    def parse_items(self, response):

        #Default callback used by Scrapy to process downloaded responses

        selector = Selector(response)
        CarImgSrc = selector.xpath('.//*[@id="carousel"]')

        #the make and model and version will be the same for all data on a page
		#put into try/except so that intermediate car make pages don't give errors
        try:
			car_make = selector.xpath('//div[@id="breadcrumb"]/ul/li/a/text()').extract()[2]
			car_model = selector.xpath('//div[@id="breadcrumb"]/ul/li[@class="second-last"]/a/text()').extract()
			car_description = selector.xpath('//div[@id="breadcrumb"]/ul/li[@class="last"]/text()').extract()
        except Exception:
			pass

        # iterate over cars
        for scr in CarImgSrc.xpath('.//@src'):
			#print('Enter')
			loader = ItemLoader(UsedCarsImagesItem(), selector=CarImgSrc)

			#Image URLs need to be lists
			imgURL = []
			imgURL = scr.extract()
			loader.add_value('file_urls', [imgURL])

			loader.add_value('make', car_make)
			loader.add_value('model', car_model)
			loader.add_value('description', car_description)
			loader.add_value('curr_date', unicode(time.strftime("%Y/%m/%d"),"utf-8"))

			yield loader.load_item()

#NewCarsImageSpider
class NewCarsImageSpider(CrawlSpider):

    name = "NewCarsImageSpider"
    allowed_domains = ["www.cars.co.za"]#don't add "http" otherwise will give "filtered offsite request error"
    start_urls = ["http://www.cars.co.za/newcars"]

	#links to be followed stating with the outermost link
    rules = [
        Rule(LinkExtractor(restrict_xpaths='//div[@class="makesDropdown"]/div[@class="dropdown_label"]/div'), callback="parse_items", follow=True),
		Rule(LinkExtractor(allow=(), restrict_xpaths='//div[@class="col_main jq_submit"]/div[@class="box"]'), callback="parse_items", follow=True),
		Rule(LinkExtractor(allow=(), restrict_xpaths='//table[@id="variant_table"]/tbody/tr/td[@style="width:200px;"]/strong/a'), callback="parse_items", follow=True),
		#Rule(LinkExtractor(allow=()), callback="parse_items", follow=True),#this will follow all links found
    ]

    def parse_items(self, response):

        #Default callback used by Scrapy to process downloaded responses
        selector = Selector(response)
        CarImgSrc = selector.xpath('.//*[@id="carousel"]')

        #the make and model and version will be the same for all data on a page
		#put into try/except so that intermediate car make pages don't give errors
        try:
			car_make = selector.xpath('//div[@class="breadcrumb-bar"]/div[@class="container"]/ul/li/a/text()').extract()[2]
			car_model = selector.xpath('//div[@class="breadcrumb-bar"]/div[@class="container"]/ul/li[@class="second-last"]/a/text()').extract()
			car_version = selector.xpath('//div[@class="breadcrumb-bar"]/div[@class="container"]/ul/li[@class="last"]/text()').extract()
        except Exception:
			pass

        # iterate over cars
        for scr in CarImgSrc.xpath('.//@src'):
			loader = ItemLoader(NewCarsImagesItem(), selector=CarImgSrc)

			#Image URLs need to be lists
			imgURL = []
			imgURL = scr.extract()
			loader.add_value('file_urls', [imgURL])

			loader.add_value('make', car_make)
			loader.add_value('model', car_model)
			loader.add_value('version', car_version)
			loader.add_value('curr_date', unicode(time.strftime("%Y/%m/%d"),"utf-8"))

			yield loader.load_item()
