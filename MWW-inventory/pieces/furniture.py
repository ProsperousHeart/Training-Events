# from resources.wood import Wood
import logging                  # https://docs.python.org/3/library/logging.html

# class Furniture(Wood):
class Furniture():
    """
    This class is to create an Furniture object.

    """

    def __init__(self, type = "", cloth = None, folding = False, mww_notes = ""):
        """
        This is the __init__ method which allows someone to create an instance of the Furniture class.

        This function determines what attributes each instance of the class will have.

        """

        self.type = type
        self.cloth = cloth
        self.folding = folding
        self.mww_notes = mww_notes
