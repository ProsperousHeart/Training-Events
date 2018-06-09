import datetime
import resources.artwork as art
import resources.wood as wood
import pieces.furniture as furniture
import pieces.sign as sign
import pieces.wood_cup as cup

class CooperageItem:
    """
    This class is the item that will be used to put into the database.

    """

    def __init__(self, at_cost = 0.00, price_sold = 0.00, discount = 0, notes = "",  custom_bool = False):
        """
        This will instantiate a CooperageItem instance.

        """

        self.at_cost = at_cost
        self.price_sold = price_sold
        self.discount = discount
        self.notes = notes
        self.custom_bool = custom_bool
        self.completion_date = None
        self.date_added = self.get_today()

    def get_dict(self):
        # I think there is a magic method for this? If not, make one
        """
        This function returns the dict view of the item instance.

        """

        def chk_date(self):
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

            if self.completion_date is None:
                return "Not yet completed"

            return create_DateStr(self.completion_date)

        return {'at_cost': self.at_cost,
                'price_sold': self.price_sold,
                'discount': self.discount,
                'notes': self.notes,
                'custom_bool': self.custom_bool,
                'completion_date': chk_date(self.completion_date),
                }

    def get_today(self):
        """
        This function returns today's date as a datetime object.

        https://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/


        """

        return datetime.datetime.now()
