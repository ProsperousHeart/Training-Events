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

class CooperageItem(Wood):
    """
    This class is the item that will be used to put into the database.

    """

    def __init__(self, sum_num = 1, price_sold = 0.00, discount = 0,
                    notes = "",  custom_bool = False, vip_bool = False,
                    wood_type = "", hard_vs_soft = False, at_cost = 0.00):
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

        # Wood.__init__(self, vip_bool = False, wood_type = "",
        super().__init__(vip_bool, wood_type, hard_vs_soft, at_cost)
        self._price_sold = Money(amount=price_sold, currency='USA')
        self._discount = discount
        self._notes = notes
        self._custom_bool = custom_bool
        self._completion_date = None
        self._date_added = get_today()
        self._itemNum = str(sum_num) + str(self._date_added.year)[2:]

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

        """

        logger.debug("Adding {} to {} for at_cost".format(self._at_cost, value))
        self._at_cost += value

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
        This function will add value to the self.price_sold value.

        """

        logger.debug("Setting price_sold from {} to {}".format(self._price_sold, value))
        self._price_sold = value

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

        """

        logger.debug("Setting discount {} to {}".format(self._discount, perc_int))
        self._discount = perc_int

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

        """

        # logger.debug("Setting notes")
        self._notes = notes

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

        """

        logger.debug("Setting custom_bool")
        if self._custom_bool != new_bool:
            self._custom_bool = new_bool
        else:
            logger.error('Requested custom_bool in cooper_item to be same')

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

        """

        # logger.debug("Setting completion_date")
        self._completion_date = completion_date

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
                'hard_vs_soft': self.hard_vs_soft,    # from Wood inheritance
                'markup': self.markup,                # from Wood inheritance
                'notes': self.notes,
                'price_sold': self.price_sold,
                'vip_bool': self.vip_bool,            # from Wood inheritance
                'wood_type': self.wood_name           # from Wood inheritance
                }
