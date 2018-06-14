import sqlite3      # http://www.sqlitetutorial.net/sqlite-python
import logging                  # https://docs.python.org/3/library/logging.html
import pprint

logger = logging.getLogger(__name__)
pp = pprint.PrettyPrinter(indent=4)

def create_connection(db_title:str):
    """
    This function returns the sqlite3 connection.

    """

    try:
        conn = sqlite3.connect('{}.db'.format(db_title))
        return conn
    except Exception as excptn:
        err_msg = r'An exception of type {0} occurred. Arguments:\n{1!r}'
        logger.warning('err_msg'.format(type(excptn).__name__, excptn.args))
        logger.error('err_msg'.format(type(excptn).__name__, excptn.args))

def check_4_tbls(connection, wood_dict:dict, empty_CI):
    """
    This function will be called to check for tables created. If none found,
    will run create_tables in order to create the database.

    """

    logger.debug('Starting check_4_tbls()...')

    cursor = connection.cursor()

    # id will start at 1
    create_tbl_query = "CREATE TABLE IF NOT EXISTS wood (id INTEGER PRIMARY KEY, at_cost real, hard_vs_soft text, markup INTEGER, wood_name text, vip_bool INTEGER)"
    cursor.execute(create_tbl_query)

    # https://stackoverflow.com/questions/14108162/python-sqlite3-insert-into-table-valuedictionary-goes-here
    # https://docs.python.org/2.7/library/sqlite3.html#sqlite3.Cursor.execute
    # https://stackoverflow.com/questions/33636191/insert-a-list-of-dictionaries-into-an-sql-table-using-python
    wood_dict_keys = wood_dict[0].keys()
    print('Wood dict keys:  {}'.format(wood_dict_keys))
    cols = ', '.join(wood_dict_keys)
    placeholders = ':' + ', :'.join(wood_dict_keys)
    cursor.executemany('INSERT INTO wood ({}) VALUES ({})'.format(cols, placeholders), wood_dict)

    # create new table for items
    # create_tbl_query = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, wood INTEGER, price_sold blob, discount int, notes text, custom_bool int, completion_date blob, date_added blob, itemNum text, owner blob)"
    cols = ', '.join([item for item, val in empty_CI.get_dict().items()])
    print('cols:  {}'.format(cols))
    create_tbl_query = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, {})".format(cols)
    cursor.execute(create_tbl_query)

    # cursor.execute("INSERT INTO items VALUES ('test', 10.99)")
    # no longer needed now that we have ability to add to DB

    connection.commit()
    # connection.close()
    logger.debug('Completed check_4_tbls()...')


def print_tables(connection, tbl_title:str=None, num_rows=None, log_list:bool=False):
    """
    This function will print all rows of all tables, up to optional INT input.

    ADditional links:
        - http://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
        - https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html#querying-the-database---selecting-rows
        - https://stackoverflow.com/questions/14108162/python-sqlite3-insert-into-table-valuedictionary-goes-here
        - https://stackoverflow.com/questions/25049332/insert-values-from-dictionary-into-sqlite-database
        - https://www.quora.com/How-do-I-save-a-Python-list-to-MySQL-database

    """

    logger.debug('Starting print_tables()...')

    cursor = connection.cursor()

    if tbl_title is None:
        logger.info('No table name provided - getting all...')
        # all_items = cursor.fetchall()   # returns a list
        # print('All Items:  {}'.format(all_items))

        cursor.execute('SELECT * FROM items')
        all_items = cursor.fetchall()    # returns a list
        # print('All Items:  {}'.format(all_items))

    else:
        print('BROKEN in table_mod')
        logger.error('This part not yet scripted...')
        cursor.close()
        return

    if len(all_items) == 0:
        logger.warning('No items in DB!')
        print('No items in DB! Please add more to show tables.')
    else:
        # http://www.learningaboutelectronics.com/Articles/How-to-show-all-tables-of-a-MySQL-database-in-Python.php
        # for item in range(len(all_items)):
        for item in all_items:
            # print(pprint.pformat(result[item]))
            # print(pprint.pformat(item))
            print(item)
            if log_list == True:
                # logger.info('ROW:  {}'.format(result[item]))
                logger.info('ROW:  {}'.format(item))

    cursor.close()
    # connection.close()
    return


def add_to_table(connection, tbl_title:str, data_dict:dict):
    """
    This function adds data to a table.

    """

    logger.debug('Starting add_to_table()...')

    cursor = connection.cursor()

    # need to create the function to insert data into the table
    if tbl_title == 'items':
        cols = ', '.join(data_dict.keys())
        placeholders = ':' + ', :'.join(data_dict.keys())
        cursor.execute("INSERT INTO items ({}) VALUES({})".format(cols, placeholders), data_dict)
        connection.commit()
        logger.info('Committed add to items DB')
        print('Supposedly added...')

    else:
        logger.error('Not yet scripted for adding to other tables...')
        print('Not yet scripted for adding to other tables...')
        cursor.close()
        return (True, 'Not yet scripted for adding to other tables...')

    cursor.close()
    return (False, None)
