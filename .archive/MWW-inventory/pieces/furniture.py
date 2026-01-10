# from resources.wood import Wood
import logging                  # https://docs.python.org/3/library/logging.html

# class Furniture(Wood):
class Furniture():
    """
    This class is to create an Furniture object.

    """

    type = ['chair', 'bench', 'table']

    def __init__(self, type = "", cloth = None, folding = False, mww_notes = ""):
        """
        This is the __init__ method which allows someone to create an instance of the Furniture class.

        This function determines what attributes each instance of the class will have.

        """

        logger.debug('Initialiazing new instance of Furniture()')

        self._type = type
        self._cloth = cloth
        self._folding = folding
        self._mww_notes = mww_notes

    @property
    def cloth(self):
        """
        This function returns the data in attribute _cloth

        """

        return self._cloth

    @cloth.setter
    def cloth(self, data:dict):
        """
        This function sets the attribute _cloth with data (dict).

        Returns updated value.

        """

        logger.warning('Need to confirm if cloth data input is dict and proper values')
        self._cloth = data
        return self._cloth

    @property
    def folding(self):
        """
        This function returns the data in attribute _folding

        """

        return self._folding

    @folding.setter
    def folding(self, folding_bool):
        """
        This function updates the folding boolean.

        Returns updated value.

        """

        logger.warning('Need to test if bool is a bool.')
        self._folding = folding_bool
        return self._folding

    @property
    def mww_notes(self):
        """
        This function returns the data in attribute _mww_notes

        """

        return self._mww_notes

    @mww_notes.setter
    def mww_notes(self, notes:str):
        """
        This function updates notes about the furniture and then returns the data.

        """

        logger.warning('Need to test if notes is a note - otherwise update to STR.')
        self._mww_notes = notes
        return self._mww_notes

    @property
    def type(self):
        """
        This function returns the data in attribute _type

        """

        return self._type

    @type.setter
    def type(self, type_update:str):
        """
        This function sets the attribute _type then returns new value.

        """

        logger.warning('Need to test if type_update is a STR.')
        self._type = type_update
        return self._type
