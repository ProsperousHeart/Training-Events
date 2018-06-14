import cooper_item
import logging                  # https://docs.python.org/3/library/logging.html
import pprint
import table_mod as tables
from money import Money

# create_item = cooperidge_item.CooperageItem

# https://docs.python.org/3/library/logging.html#logrecord-attributes

#fmt = '%(asctime)s | %(levelname)s %(funcname)s at line %(lineno)s:  %(message)s'
#logging.basicConfig(format=fmt, filename='CooperAppLogs.log', filemode='w',
#            level=logging.DEBUG, datefmt='%m/%d/%Y %I:%M:%S %p')

# fmt = '%(asctime)s | %(levelname)s - %(module)s line %(lineno)d, %(funcName)s:  %(message)s'
fmt = '%(asctime)s | %(levelname)s - %(module)s.py [%(lineno)d]:  %(message)s'
# fmt = '%(created)f | %(levelname)s:  %(message)s'
logging.basicConfig(format=fmt, filename='CooperAppLogs.log', filemode='w',
    level=logging.DEBUG, datefmt='%m/%d/%Y %I:%M:%S %p')
    # removing filemode will append logs vs overwrite
logger = logging.getLogger(__name__)

pp = pprint.PrettyPrinter(indent=4)

# base_wood = [{'at_cost': Money(amount=3.65, currency='USA'),
base_wood = [{'at_cost': round(3.65, 2),
                'hard_vs_soft': 'medium',
                # 'markup': Money(amount=0.00, currency='USA'),
                'markup': 0.00,
                'vip_bool': False,
                'wood_name': 'birch'},
            # {'at_cost': Money(amount=2.50, currency='USA'),
            {'at_cost': round(2.50, 2),
                'hard_vs_soft': 'hard',
                # 'markup': Money(amount=0.00, currency='USA'),
                'markup': round(0.00, 2),
                'vip_bool': False,
                'wood_name': 'oak'},
            # {'at_cost': Money(amount=2.25, currency='USA'),
            {'at_cost': round(2.25, 2),
                'hard_vs_soft': 'soft',
                # 'markup': Money(amount=0.00, currency='USA'),
                'markup': round(0.00, 2),
                'vip_bool': False,
                'wood_name': 'pine'}]

class entry_exit(object):
    """
    This decorator will add logging before and after calling a function.

    http://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html#slightly-more-useful

    """

    def __init__(self, func):
        self.func = func

    def __call__(self):
        logger.debug('Starting {} for cooper_item.py file'.format(self.func.__name__))
        self.func()
        logger.debug('Completing {} for cooper_item.py file'.format(self.func.__name__))

    # return entry_exit

# @entry_exit
def create_piece(item_num):
    """
    This function creates a new Cooperidge inventory item.

    """

    new_item = cooper_item.CooperageItem(sum_num=item_num)
    # logger.debug('Successfully created item {}!'.format(new_item.itemNum))
    logger.debug('Returning new cooper_item via create_piece()')
    # return create_item()
    return new_item

#   Create options
#   - create new cooper_item (cup, sign, furniture, etc)
#   - create new location (where they take the cups to)
def db_manip(sql_cnxn, to_do:str, data, table_name:str=None):
    """
    This function takes in a string (db_name), string (table_name) and
    data (object). It will then create a new data structure appropriate
    for the requested table.

    Current table names:
        - wood
        - items

    """

    logger.warning('Check and ensure incoming parameters match expectations')
    if to_do.lower() == 'add':
        logger.info('Adding item to DB table:  {}'.format(table_name))
        tables.add_to_table(sql_cnxn, table_name, data)
    else:
        logger.error('Called on a function not yet written!')

#   viewing options
#   - all items
#   - just cups
#   - just Furniture
#   - just signs
#   - wood inventory
#   - sold
#   - to sell
#   - what items are in what location

#   update cooperage cooperidge_item:
#   - add final piece number
#   - update artwork
#   - update price sold
#   - update notes
#   - update _completion_date
#   - update handle side, staves #, size if Wood_Cup

#   exportation ability
#   - export to Excel locally
#   - export to Google excel

#   also looking for ability to backup DB locally???

if __name__ == "__main__":
    """
    This function ensures that if this file is run, it is read as a source file.

    """

    logger.debug('Starting __init__ for cooper_app.py file')

    logger.warning('Need to create a different DB log for JUST changes...')
    logger.warning('All setter methods will eventually need to also update the DB')

    #   Database needs ...
    #   - DB check & create if none found
    #   - add to DB
    #   - update in DB (per piece, as well as wood resources)
    logger.debug('Checking for local DB...')
    sql_cnxn = tables.create_connection('cooperage')
    tables.check_4_tbls(sql_cnxn, base_wood, cooper_item.CooperageItem())

    # item_list = []
    piece_num = 1

    logger.info('Creating new item...')
    item = create_piece(piece_num)
    logger.info('New item created!')
    print('New item created - adding to DB!')
    # pp.pprint(item.get_dict())

    # replacing internal data pieces with adding to a DB
    # item_list.append(item)
    logger.debug('Calling sql_cnxn() for ADD...')
    # db_manip(sql_cnxn, 'add', 'items', item)
    rtn_tuple = tables.add_to_table(sql_cnxn, 'items', item.get_txtDict())
    if rtn_tuple[0] == True:
        print('ERROR:  There was an error adding item to the DB.')
    piece_num += 1

    print('===' * 5)

    logger.info('Updating at_cost...')
    logger.warning('Need to update DB not just local variable.')
    # item.at_cost(4.69)
    item.at_cost = 4.69
    print("Updated data after changing at_cost to $4.69:\n{}".format(pprint.pformat(item.get_dict())))

    print('===' * 5)

    logger.info('Creating new item...')
    item = create_piece(piece_num)
    print('New item created - adding to DB!')
    # pp.pprint(item.get_dict())

    # replacing internal data pieces with adding to a DB
    # item_list.append(item)
    logger.debug('Calling sql_cnxn() for ADD...')
    # db_manip(sql_cnxn, 'add', 'items', item)
    rtn_tuple = tables.add_to_table(sql_cnxn, 'items', item.get_txtDict())
    if rtn_tuple[0] == True:
        print('ERROR:  There was an error adding item to the DB.')
    piece_num += 1

    print('===' * 5)

    # print("Hardnesses:  {}".format([item.woodType.hard_vs_soft for item in item_list]))
    # print('Need to get Hardnesses of all wood of items in DB')
    logger.warning('Need to get Hardnesses of all wood of items in DB')

    # print("Wood Type:  {}".format([item.woodType.wood_name for item in item_list]))
    # print('Need to get names of all wood type of items in DB')
    logger.warning('Need to get names of all wood type of items in DB')

    logger.debug('Starting tests for SQL DB calls...')

    print('Printing full DB:')
    tables.print_tables(sql_cnxn, log_list=True)

    sql_cnxn.close()
    logger.debug('Completing __init__ for cooper_app.py file')
