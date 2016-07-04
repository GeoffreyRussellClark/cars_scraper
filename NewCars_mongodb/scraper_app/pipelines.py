from sqlalchemy.orm import sessionmaker
from models import Cars, db_connect, create_cars_table


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
