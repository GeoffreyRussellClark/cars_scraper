#for Postgresql Pipeline
from sqlalchemy.orm import sessionmaker
from models import Cars, db_connect, create_cars_table

#for Mongo Pipeline
import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log

class NewCarsPipeline(object):
    """Cars pipeline for storing scraped items in the database"""
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates CarsNational table.
        """
        engine = db_connect()
        create_cars_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save cars in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        NewCarsItem = Cars(**item)

        try:
            session.add(NewCarsItem)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item

class MongoPipeline(object):
	
	def __init__(self):
		connection = pymongo.MongoClient(settings['MONGODB_SERVER'],settings['MONGODB_PORT'])
		db = connection[settings['MONGODB_DB']]
		self.collection = db[settings['MONGODB_COLLECTION']]
	
	def process_item(self,item,spider):
		valid = True
		for data in item:
			if not data:
				valid = False
				raise DropItem('Missing {0}!'.format(data))
		if valid:
			self.collection.insert(dict(item))
			log.msg("car added to MongoDB Database!", level=log.DEBUG, spider=spider)
		return item
		