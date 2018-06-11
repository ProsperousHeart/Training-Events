import cooper_item
import logging                  # https://docs.python.org/3/library/logging.html
import pprint

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

    logger.debug('Returning new cooper_item via create_piece()')
    new_item = cooper_item.CooperageItem(sum_num=item_num)
    logger.debug('Successfully created item ... returning ...')
    # return create_item()
    return new_item

if __name__ == "__main__":
    """
    This function ensures that if this file is run, it is read as a source file.

    """

    logger.debug('Starting __init__ for cooper_app.py file')

    item_list = []
    piece_num = 1

    logger.info('Creating new item...')
    item = create_piece(piece_num)
    print('New item created:')
    logger.info('New item created!')
    pp.pprint(item.get_dict())
    logger.info('The new item is shown as:\n{}'.format(pprint.pformat(item.get_dict())))
    item_list.append(item)
    piece_num += 1

    print('===' * 5)

    logger.info('Updating at_cost...')
    item.chg_atCost(4.69)
    print("Updated data after changing at_cost to $4.69:\n{}".format(pprint.pformat(item.get_dict())))
    logger.info('The item is snow updated as:\n{}'.format(pprint.pformat(item.get_dict())))
    logger.info('Current at_cost:  {}'.format(item.at_cost))

    print('===' * 5)

    logger.info('Creating new item...')
    item = create_piece(piece_num)
    print('New item created:')
    pp.pprint(item.get_dict())
    logger.info('The new item is shown as:\n{}'.format(pprint.pformat(item.get_dict())))
    item_list.append(item)
    piece_num += 1

    print('===' * 5)

    logger.info('Final list is:\n{}'.format(pprint.pformat([item.get_dict() for item in item_list])))

    print('Final list is:\n{}'.format(pprint.pformat([item.get_dict() for item in item_list])))

    print('===' * 5)

    logger.info("Hardnesses:  {}".format([item.get_Hardness() for item in item_list]))
    print("Hardnesses:  {}".format([item.get_Hardness() for item in item_list]))

    logger.info("Wood Type:  {}".format([item.get_WoodType() for item in item_list]))
    print("Wood Type:  {}".format([item.get_WoodType() for item in item_list]))

    logger.debug('Completing __init__ for cooper_app.py file')
