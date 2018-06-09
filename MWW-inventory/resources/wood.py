class Wood:
    """
    This class is to create an Wood object.

    """

    def __init__(self, vip_bool = False, wood_type = "", hard_vs_soft = False, at_cost = 0.00):
        """
        This is the __init__ method which allows someone to create an instance of the Wood class.

        This function determines what attributes each instance of the class will have.

        """

        self.vip_bool = vip_bool            # True if speciality, else standard
        self.wood_type = wood_type          # cedar, poplar, etc
        self.hard_vs_soft = hard_vs_soft    # True if hardwood
        self.at_cost = at_cost              # at cost to purchase
        self.markup = 0.00                  # markup for the labor, etc
