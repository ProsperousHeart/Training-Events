from resources.wood import Wood

class Wood_Cup(Wood):
    """
    This class is to create a Wood_Cup object.

    """

    def __init__(self, wood_type_obj = None, size = None, art_class_obj = None, handle_loc = "R", staves = 0):
        """
        This is the __init__ method which allows someone to create an instance of the Wood_Cup class.

        This function determines what attributes each instance of the class will have.

        """

        self.staves = staves
        self.wood_type = wood_type_obj
        self.art_class_obj = art_class_obj
        self.staves = staves
        self.size = size
