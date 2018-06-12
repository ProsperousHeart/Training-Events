import logging                  # https://docs.python.org/3/library/logging.html
from money import Money

logger = logging.getLogger(__name__)

class Wood:
    """
    This class is to create an Wood object.

    """

    def __init__(self, vip_bool = False, wood_name = "", hard_vs_soft = False,
                at_cost = 0.00):
        """
        This is the __init__ method which allows someone to create an instance of the Wood class.

        This function determines what attributes each instance of the class will have.

        """
        logger.debug('Creating initial wood data...')

        self._at_cost = Money(amount=at_cost, currency='USA')    # at cost
        self.hard_vs_soft = hard_vs_soft    # True if hardwood
        self.markup = Money(amount=0.00, currency='USA') # markup 4 labor, etc
        self.vip_bool = vip_bool            # True if speciality, else standard
        self.wood_name = wood_name          # cedar, poplar, etc

        logger.debug('Completed setup...')

    def chg_atCost(self, float_in):
        """
        This function completely replaces the at cost portion. Since the cost
        for wood can change at any time, this needs to be easily updated.
        A float up to 2 decimal places is provided as input, no data returned.

        """

        logger.debug('Updated at_cost from {} to {}'.format(self.at_cost,
                    float_in))
        # self.at_cost = Money(amount=round(float_in, 2), currency='USA')
        self.at_cost = Money(amount=format(float_in, '.2f'), currency='USA')


    def get_Hardness(self):
    # @classmethod
    # def get_Hardness(cls):
        """
        Function that returned the hardness of the wood.

        """

        # logger.debug('Returning if hard vs soft wood...')
        return self.hard_vs_soft
        # return cls.hard_vs_soft

    def get_WoodType(self):
    # @classmethod
    # def get_WoodType(cls):
        """
        Function that returns the type of wood used in this piece.

        """

        # if self.wood_name ==

        # logger.debug('Returning type of wood:  {}'.format(self.wood_name))
        return self.wood_name
        # return cls.wood_name

    # def get_WoodInfo(self):
    @classmethod
    def get_WoodInfo(cls):
        """
        This function returns the hardness and type of wood in a single dict.

        """

        logger.debug('Returning hardness & wood type...')
        # return {'hardness': self.hard_vs_soft, 'type': self.wood_name}
        return {'hardness': cls.hard_vs_soft, 'name': cls.wood_name}

    # def get_dict(self):
    @classmethod
    def get_WoodInfo(cls):
        """
        This function returns the dict view of the item instance.

        """

        logger.debug('Returning dictionary of attributes for Wood...')
        # return {
        #     'at_cost': self.at_cost,
        #     'hard_vs_soft': self.hard_vs_soft,
        #     'markup': self.markup,
        #     'wood_name': self.wood_name,
        #     'vip_bool': self.vip_bool
        # }
        return {
            'at_cost': cls.at_cost,
            'hard_vs_soft': cls.hard_vs_soft,
            'markup': cls.markup,
            'wood_name': cls.wood_name,
            'vip_bool': cls.vip_bool
        }
