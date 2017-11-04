## How to scrape with the spiders ##

### NewCarsSpider ###

This scrapes all the data the website has about new cars on the market e.g. make, model, number of airbags, etc.

#### In a text editor: ####
open cars_scraper/scraper_app/settings.py

Ensure that both depth limit and depth priority are set to 3 as follows:
DEPTH_LIMIT = 3
DEPTH_PRIORITY = 3

We need a depth limit of 3 because the spider will first follow links to each car make, then to each make's models and then each model's submodels.

#### In the terminal: ####
cd cars_scraper
workon </virtualenvname/>
scrapy crawl NewCarsSpider -o NewCars.csv

It takes approximately an hour and a half to run on my computer

### NewCarsImageSpider ###

This scrapes all the images of new vehicles that the website hosts. The scraper will output a csv file that has some of the vehicle's meta data such as make and model as well as the file name of the associated image. The images will be stored in a seperate specified location.

#### In a text editor: ####
open cars_scraper/scraper_app/settings.py

Ensure that both depth limit and depth priority are set to 3 as follows:
DEPTH_LIMIT = 3
DEPTH_PRIORITY = 3

We need a depth limit of 3 because the spider will first follow links to each car make, then to each make's models and then each model's submodels.

Also in settings.py set the location where the actual images will be saved e.g. :
FILES_STORE = "ScrapedCarImages/NewCars"

#### In the terminal: ####
cd cars_scraper
workon </virtualenvname/>
scrapy crawl NewCarsImageSpider -o NewCarsImage.csv

It takes approximately x minutes to run on my computer

### UsedCarsSpider ###

This scrapes all the data the website has about advertised used cars e.g. make, model, number of airbags, etc.

#### In a text editor: ####
open cars_scraper/scraper_app/settings.py

Ensure that both depth limit and depth priority are set to a large number say 750 as follows:
DEPTH_LIMIT = 750
DEPTH_PRIORITY = 750

We need a depth limit large enough to crawl through all the vehicles associated with a particular manufacturer. At the time of writing Volkswagen had over 12 000 vehicles advertised. Since each page has 20 vehicles, a depth of 750 will let you scrape up to 15000 vehicles.

#### In the terminal: ####
cd cars_scraper
workon </virtualenvname/>
scrapy crawl UsedCarsSpider -o UsedCars.csv

It takes approximately x hours to run on my computer. Note that since the scraper takes so long to scrape the wedsite will most like be updated while the spider is crawling. This is fine though as the spider will just keep scraping throught he pages sequentially. However, it is likely that either some vehicles will be missed duplicated because of this.

### UsedCarsImageSpider ###

This scrapes all the images of used vehicles that the website hosts. The scraper will output a csv file that has some of the vehicle's meta data such as make and model as well as the file name of the associated image. The images will be stored in a seperate specified location.

#### In a text editor: ####
open cars_scraper/scraper_app/settings.py

Ensure that both depth limit and depth priority are set to a large number say 750 as follows:
DEPTH_LIMIT = 750
DEPTH_PRIORITY = 750

We need a depth limit large enough to crawl through all the vehicles associated with a particular manufacturer. At the time of writing Volkswagen had over 12 000 vehicles advertised. Since each page has 20 vehicles, a depth of 750 will let you scrape up to 15000 vehicles.

#### In the terminal: ####
cd cars_scraper
workon </virtualenvname/>
scrapy crawl UsedCarsImageSpider -o UsedCarsImages.csv

It takes approximately x hours to run on my computer. Note that since the scraper takes so long to scrape the wedsite will most like be updated while the spider is crawling. This is fine though as the spider will just keep scraping throught he pages sequentially. However, it is likely that either some vehicles will be missed duplicated because of this.
