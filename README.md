# README #

### What is this repository for? ###

* Help Orion create a dynamic depreciation model that will enable us to put a value on any car regardless of it's make, model, year, millage, etc.
* The repo makes extensive use of web-scrapers, primarily in python's scrapy library though might use selenium in the future. 

### To start: ###

* Pull this repository to your local machine.
* Create a virtual environment
* Install the required libraries with: "pip install -r requirements.txt"

### Directory Overview: ###

* brick7_postgresql: the first car scraper. It scrapes the brick7 website which claims to be a car search engine, though I'm not sure how up to date the information is. the data get's scraped into a postgresql database
* depModle: Geoff's initial workings to create a depreciation model
* MattWorking: self explanatory
* Selenium: Test workings of a different scraper that mimics a human. Often used to test webpages. Looks like a promising way to scrape in the future.
* NewCars_mongodb: This is where the magic has been happening. It contains 5 spiders at the time of writing. 4 of them are for the cars.co.za website which get all the new car information, used car information and the images for both. There is also a scraper that gets imformation and images from autotrader, however the website has been giving issues like it seems to be able to block the scrpaer or the user IP address. The file name is somewhat misleading. It does not actually scrape into mongodb rather it is better to simply scrape into a csv file.

### Recommended Tutorial ###

http://newcoder.io/scrape/

### Sources/inspiration for the code ###

* http://newcoder.io/scrape/
* http://www.pyimagesearch.com/2015/10/12/scraping-images-with-python-and-scrapy/
* http://mherman.org/blog/2012/11/08/recursively-scraping-web-pages-with-scrapy/#.V788f60dbYA

### Websites that have been scraped ###

* http://www.cars.co.za/
* http://www.autotrader.co.za/
* http://cars.brick7.co.za/

### Websites that could be scraped possibly ###

* http://www.zoopa.co.za/
* https://www.santam.co.za/calculators/vehicle-calculator/

### Recommended Web-scraping debugging method ###

Use the scrapy shell. Call the webpage and inspect the elements manually to see what scrapy can see.

#### Syntax: ####

* scrapy shell <url>
* data = response.xpath('<xpath to element>')
* for i in data.xpath('.//<sub-level xpath to element>'):
*     print i.extract()

### Who do I talk to? ###

Geoffrey Clark