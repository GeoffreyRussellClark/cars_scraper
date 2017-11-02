# README #

### What is this repository for? ###

* This repo houses a web-scraper coded in python using the scrapy library. It contains four spiders that scrape data from the cars.co.za website. This website is a used by individuals and dealers to buy and sell used cars. As such it contains vast amount of car metadata as well as images of vehicles. It also has a section where it advertises new cars and shows their specs. The four spiders scrape either images or vehicle meta data for either new or used vehicles.

### To start: ###

* Pull this repository to your local machine using git.
* Create a virtual environment (I favour virtualEnvWrapper)
* Install the required libraries with: "pip install -r requirements.txt"

### Directory Overview: ###

* NewCars_mongodb: This is where the magic has been happening. It contains 5 spiders at the time of writing. 4 of them are for the cars.co.za website which get all the new car information, used car information and the images for both. There is also a scraper that gets imformation and images from autotrader, however the website has been giving issues like it seems to be able to block the scrpaer or the user IP address. The file name is somewhat misleading. It does not actually scrape into mongodb rather it is better to simply scrape into a csv file.

### Recommended Tutorial ###

http://newcoder.io/scrape/

### Sources/inspiration for the code ###

* http://newcoder.io/scrape/
* http://www.pyimagesearch.com/2015/10/12/scraping-images-with-python-and-scrapy/
* http://mherman.org/blog/2012/11/08/recursively-scraping-web-pages-with-scrapy/#.V788f60dbYA

### The website that we scrape ###

* http://www.cars.co.za/

### Recommended Web-scraping debugging method ###

Use the scrapy shell. Call the webpage and inspect the elements manually to see what scrapy can see. This really helps to test xpaths.

#### Syntax: ####

* scrapy shell <url>
* data = response.xpath('<xpath to element>')
* for i in data.xpath('.//<sub-level xpath to element>'):
*     print i.extract()

### Who do I talk to? ###

Geoffrey Clark
