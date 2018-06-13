# from resources.wood import Wood
import logging                  # https://docs.python.org/3/library/logging.html

# class Sign(Wood):
class Sign:
    """
    This class is to create an Sign object.

    """

    def __init__(self, size_w = 0.00, size_l = 0.00, mww_notes = ""):
        """
        This is the __init__ method which allows someone to create an instance of the Sign class.

        This function determines what attributes each instance of the class will have.

        """

        self._size_l = size_l
        self._size_w = size_w
        self._mww_notes = mww_notes

    @property
    def size_l(self):
        """
        This function returns the length of the sign.

        """

        return self._size_l

    @size_l.setter
    def size_l(self, length):
        """
        This function sets the length of the sign.

        """

        logger.warning('Need to check if length of sign is integer or float.')
        self._size_l = length

    @property
    def size_w(self):
        """
        This function returns the width of the sign.

        """

        return self._size_w

    @size_w.setter
    def size_w(self, width):
        """
        This function sets the width of the sign.

        """

        logger.warning('Need to check if width of sign is integer or float.')
        self._size_w = width

    @property
    def mww_notes(self):
        """
        This function returns the information about the notes for the sign.

        """

        logger.debug('Returning notes...')
        return self._mww_notes

    @size_w.setter
    def mww_notes(self, notes):
        """
        This function sets the notes with the updated data.

        """

        self._mww_notes = notes
        logger.info('Notes for sign updated.')
