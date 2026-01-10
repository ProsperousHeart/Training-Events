# from resources.wood import Wood

# class Wood_Cup(Wood):
class Wood_Cup():
    """
    This class is to create a Wood_Cup object.

    """

    staves_options = [8, 10]
    handle_options = ['L', 'R']

    # def __init__(self, wood_type_obj = None, size = None, art_class_obj = None, handle_loc = "R", staves = 0):
    def __init__(self, size = None, handle_loc = "R", staves = 0):
        """
        This is the __init__ method which allows someone to create an instance of the Wood_Cup class.

        This function determines what attributes each instance of the class will have.

        """

        logger.debug('Initialiazing new instance of Wood_Cup()')

        self._handle_loc = handle_loc
        # self.wood_type = wood_type_obj
        # self.art_class_obj = art_class_obj
        self._staves = staves
        self._size = size

    @property
    def handle_loc(self):
        """
        This function returns the current information about the cup's handle location.

        """

        return self._handle_loc

    @handle_loc.setter
    def handle_loc(self, loc):
        """
        This function will update the handle location to be either L for left
        or R for right.

        """

        # need to check and ensure a string and L or R
        if loc.upper() in handle_options:

            self._handle_loc = loc

        else:
            logger.warning('Handle location request does not exist')

            # also need to return some kind of error to user???

    @property
    def size(self):
        """
        This function returns the size of the cup. This is determined by the cooper?

        """

        return self._size

    @size.setter
    def size(self, size):
        """
        This function will update the size ... Most likely some mathematical equation
        but will assume it is a string for now.

        Returns new self._size data

        """

        self._size = size
        return self._size

    @property
    def staves(self):
        """
        This function returns the current number of staves.

        """

        return self._staves

    @staves.setter
    def staves(self, num_staves):
        """
        This function sets the number of staves on this item.

        """

        # need to check and ensure the number is accurate (8? 10?) before setting
        # provide error if wrong? Or just always provide a particular number of staves

        if num_staves not in staves:

            logger.warning('Requested number of staves does not exist.')

            # need to return some kind of error message as well - be more exact

        else:
            self._staves = num_staves
