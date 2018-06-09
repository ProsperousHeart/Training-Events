class Artwork:
    """
    This class is to create an Artwork object.

    """

    def __init__(self, img_link = None, at_cost = 0.00, num_hours = 0, jil_notes = ""):
        """
        This is the __init__ method which allows someone to create an instance of the Artwork class.

        This function determines what attributes each instance of the class will have.

        """

        self.img_link = img_link
        self.at_cost = at_cost
        self.num_hours = num_hours
        self.jil_notes = jil_notes
