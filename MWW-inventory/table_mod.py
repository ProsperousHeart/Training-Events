import sqlite3
import logging                  # https://docs.python.org/3/library/logging.html

logger = logging.getLogger(__name__)

def check_4_tbls(db_title):
    """
    This function will be called to check for tables created. If none found,
    will run create_tables in order to create the database.

    """

    logger.debug('Starting check_4_tbls()...')

    connection = sqlite3.connect('{}.db'.format(db_title))
    cursor = connection.cursor()

    # id will start at 1
    create_tbl_query = "CREATE TABLE IF NOT EXISTS wood (id INTEGER PRIMARY KEY, at_cost real, hard_vs_soft text, markup INTEGER, wood_name text, vip_bool INTEGER)"
    cursor.execute(create_tbl_query)

    # create new table for items
    create_tbl_query = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, wood INTEGER, price_sold blob, discount int, notes text, custom_bool int, completion_date blob, date_added blob, itemNum text, owner blob)"
    cursor.execute(create_tbl_query)

    # cursor.execute("INSERT INTO items VALUES ('test', 10.99)")
    # no longer needed now that we have ability to add to DB

    connection.commit()
    connection.close()
    logger.debug('Completed check_4_tbls()...')


def add_to_table(db_title:str, tbl_title:str, data_dict:dict):
    """
    This function adds data to a table.

    """

    pass
