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

        self.size_w = size_w
        self.size_l = size_l
        self.mww_notes = mww_notes
