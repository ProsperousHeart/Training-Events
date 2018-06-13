import datetime
from money import Money
from resources.artwork import Artwork
from resources.wood import Wood
from pieces.furniture import Furniture
from pieces.sign import Sign
from pieces.wood_cup import Wood_Cup
import logging                  # https://docs.python.org/3/library/logging.html

logger = logging.getLogger(__name__)

def entry_exit(object):
    """
    This decorator will add logging before and after calling a function.

    http://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html#slightly-more-useful

    """

    def __init__(self, func):
        self.func = func

    def __call__(self):
        logger.debug('Starting {} for cooperidge_item.py file'.format(self.func.__name__))
        self.func()
        logger.debug('Completing {} for cooperidge_item.py file'.format(self.func.__name__))

    return entry_exit

# class CooperageItem(Wood):
class CooperageItem:
    """
    This class is the item that will be used to put into the database.

    """

    def __init__(self, sum_num = 1, price_sold = 0.00, discount = 0,
                    notes = "",  custom_bool = False, vip_bool = False,
                    wood_name = "", hard_vs_soft = False):
        """
        This will instantiate a CooperageItem instance.

        """
        logger.debug('Starting __init__ for CooperageItem')

        def get_today():
            """
            This function returns today's date as a datetime object.

            https://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/


            """

            logger.debug('Returning datetime')
            return datetime.datetime.now()

        # logger.warning('Need to remove Wood as inheritance and import as class')
        # Wood.__init__(self, vip_bool = False, wood_type = "",
        # super().__init__(vip_bool, wood_type, hard_vs_soft, at_cost)
        logger.warning('Need to have Wood point to a place in the DB for autoupdating')
        self._woodType = Wood()
        logger.warning('Need to have Artwork point to a place in the DB for autoupdating')
        self._artwork = Artwork()
        self._price_sold = Money(amount=price_sold, currency='USA')
        self._discount = discount
        self._notes = notes
        self._custom_bool = custom_bool
        self._completion_date = None
        self._date_added = get_today()
        # self._itemNum = str(sum_num) + str(self._date_added.year)[2:]
        self._itemNum = None
        logger.warning('Need to create class for Owner...')
        self._owner = None
        self._vip_bool = vip_bool

        self._at_cost = self._woodType.at_cost + self._artwork.at_cost
        logger.warning('Test if at_cost will update after base wood or art does')

        self._markup = self._woodType.markup + self._artwork.markup
        logger.warning('Test if markup will update after base wood or art does')

    @property
    def at_cost(self):
        """
        This function returns the "private" attribute at_cost.

        """

        # logger.debug("Getting at_cost")
        return self._at_cost

    @at_cost.setter
    def at_cost(self, value):
        """
        This function will add value to the self.__at_cost value

        Returns new _at_cost attribute value.

        """

        logger.debug("Adding {} to {} for at_cost".format(self._at_cost, value))
        self._at_cost += Money(amount=value, currency='USA')
        logger.info('New at_cost:  {}\tRETURNING DATA NOW'.format(self._at_cost))
        return self._at_cost

    @property
    def price_sold(self):
        """
        This function returns the attribute info of price_sold.

        """

        # logger.debug("Getting price_sold")
        return self._price_sold

    @price_sold.setter
    def price_sold(self, value):
        """
        This function will set value as the self.price_sold value.

        Returns updated attribute.

        """

        logger.debug("Setting price_sold from {} to {}".format(self._price_sold, value))
        self._price_sold = value
        return self._price_sold

    @property
    def discount(self):
        """
        This function returns the attribute info of discount.

        """

        # logger.debug("Getting discount")
        return self._discount

    @discount.setter
    def discount(self, perc_int):
        """
        This function will update the value of self.discount to value input.

        Returns updated attribute.

        """

        logger.debug("Setting discount {} to {}".format(self._discount, perc_int))
        self._discount = perc_int
        return self._discount

    @property
    def notes(self):
        """
        This function returns the attribute info of notes.

        """

        # logger.debug("Getting notes")
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        This function will update the value of self.notes to value input.

        Returns the updated attribute.

        """

        # logger.debug("Setting notes")
        self._notes = notes
        return self._notes

    @property
    def custom_bool(self):
        """
        This function returns the attribute info of custom_bool.

        """

        # logger.debug("Getting custom_bool")
        return self._custom_bool

    @custom_bool.setter
    def custom_bool(self, new_bool):
        """
        Function will update the value of self.custom_bool to value new_bool.

        Returns value in attribute

        """

        logger.debug("Setting custom_bool")
        if self._custom_bool != new_bool:
            self._custom_bool = new_bool
        else:
            logger.error('Requested custom_bool in cooper_item to be same')

        return self._custom_bool

    @property
    def completion_date(self):
        """
        This function returns the attribute info of notes.

        """

        # logger.debug("Getting completion_date")
        return self._completion_date

    @completion_date.setter
    def completion_date(self, completion_date):
        """
        This function will update the value of self.notes to value input.

        Returns updated attribute

        """

        # logger.debug("Setting completion_date")
        self._completion_date = completion_date
        return self._completion_date

    @property
    def date_added(self):
        """
        This function returns the date this object was added.

        """

        # logger.debug("Getting date_added")
        return self._date_added

    @property
    def itemNum(self):
        """
        This function returns the attribute info of notes.

        """

        # logger.debug("Getting itemNum")
        return self._itemNum

    @itemNum.setter
    def itemNum(self, sum_num:int):
        """
        This function takes in some number (to be provided by counting items for
        the year within a DB eventually) then adds the last 2 digits of
        current year to it. This is to be used as the completed piece number
        field. NOT to be used as main key within a SQL DB, as it only is
        created when piece is completed.

        Returns the new completed item number.

        """

        logger.warning('Need to test sum_num is number? Coming from DB though.')
        self._itemNum = str(sum_num) + str(self._date_added.year)[2:]
        return self._itemNum

    @property
    def markup(self):
        """
        This function returns attribute:    _markup

        """

        return self._markup

    @markup.setter
    def markup(self, add_markup):
        """
        This function adds to markup and returns updated attribute

        """

        logger.warning('Need to check if add_markup is INT')
        self._markup += add_markup
        return self._markup

    @property
    def owner(self):
        """
        This function returns the information of the owner of the item.

        """

        return self._owner

    @owner.setter
    def owner(self, owner_dict:dict):
        """
        This function updates the owner information and returns attribute

        """

        logger.warning('Need to check that input is proper dict or class item')
        self._owner = owner_dict
        return self._owner

    @property
    def vip_bool(self):
        """
        This function returns current value for attribute _vip_bool

        """

        return self._vip_bool

    @vip_bool.setter
    def vip_bool(self, bool_update):
        """
        This function sets _vip_bool if different valueself.
        Returns current value.

        """

        logger.warning('Need to test if bool_update is a bool')

        if self._vip_bool != bool_update:
            self._vip_bool = bool_update
        return self._vip_bool

    @property
    def woodType(self):
        """
        This function returns the wood information

        """

        logger.warning('Needs to pull from DB')
        return self._woodType

    def get_dict(self):
        # I think there is a magic method for this? If not, make one
        """
        This function returns the dict view of the item instance.

        """

        def chk_date(completion_date):
            """
            This function checks if None, returns "Not yet completed"
            Otherwise returns datetime object.

            """

            def create_DateStr(dt_obj):
                """
                This function takes in a DateTime object and returns the date
                in a string format.

                """

                return "{}-{}-{}".format(dt_obj.year, dt_obj.month, dt_obj.day)

            if completion_date is None:
                return "Not yet completed"

            return create_DateStr(completion_date)

        return {'itemNum': self.itemNum,
                'at_cost': self.at_cost,              # from Wood inheritance
                'date_added': chk_date(self.date_added),
                'completion_date': chk_date(self.completion_date),
                'custom_bool': self.custom_bool,
                'discount': self.discount,
                'hard_vs_soft': self._woodType.hard_vs_soft,    # from Wood inheritance
                'markup': self.markup,                # from Wood inheritance
                'notes': self.notes,
                'price_sold': self.price_sold,
                'vip_bool': self.vip_bool,            # from Wood inheritance
                'wood_type': self._woodType.wood_name           # from Wood inheritance
                }
