import logging                  # https://docs.python.org/3/library/logging.html
from money import Money

class Artwork:
    """
    This class is to create an Artwork object. Each object instance has the
    following attributes:

        _img_link   a string representation of an HTML link to see image
        _at_cost    Money object (USA currency)
        _markup     INT to show how much markup to sell for
        _num_hours  number of hours worked on piece
        _jil_notes  notes about artwork for JIL to remember

    """

    def __init__(self, img_link = None, at_cost = 0.00, num_hours = 0, jil_notes = ""):
        """
        This is the __init__ method which allows someone to create an instance of the Artwork class.

        This function determines what attributes each instance of the class will have.

        """

        self._img_link = img_link
        self._at_cost = Money(amount=at_cost, currency='USA')
        self._markup = 0
        self._num_hours = num_hours
        self._jil_notes = jil_notes

    @property
    def img_link(self):
        """
        This function returns the attribute:    _img_link

        """

        return self._img_link

    @img_link.setter
    def img_link(self, html:str):
        """
        This function updates the attribute:    img_link
        Returns updated attribute

        """

        logger.warning('Need to test if html is a correct HTML string - possibly even pulled form Google?')
        self._img_link = html
        return self._img_link

    @property
    def at_cost(self):
        """
        This function returns the attribute:    _at_cost

        """

        return self._at_cost

    @at_cost.setter
    def at_cost(self, new_atCost):
        """
        This function uses new_atCost to update attribute:    _at_cost
        Returns updated attribute

        """

        logger.warning('Need to check and ensure new_atCost is a possible FLOAT')
        self._at_cost = new_atCost
        return self._at_cost

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
    def num_hours(self):
        """
        This function returns the attribute:    num_hours

        """

        return self._num_hours

    @num_hours.setter
    def num_hours(self, inc_hours:int):
        """
        This function will increment some number of hoursself.
        Returns updated attribute.

        """

        logger.warning('Need to test that inc_hours is INT')
        self._num_hours += inc_hours
        return self._num_hours

    @property
    def jil_notes(self):
        """
        This function returns the attribute:    jil_notes

        """

        return self._jil_notes

    @jil_notes.setter
    def jil_notes(self, notes):
        """
        This function uses notes to update attribute:   _jil_notes
        Returns updated attribute

        """

        logger.warning('Need to check for string??? Chagne to sTR? Worth it?')
        self._jil_notes = notes
        return self._jil_notes
