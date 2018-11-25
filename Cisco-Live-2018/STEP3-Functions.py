# This is step 3 of the "Bare Bones" Process - Creating The Empty Functions
# Here is the process I follow for this phase ...
#
#   1 - write out the comments of expected functions
#   2 - create those functions with proper docstrings, logging, and pass ONLY
#   3 - tie the functions together in your __main__
#   4 - test the logic with print or logging statements

# ======================================================================
# create global for choice options ... bad practice, so would be better
# to utilize a DB (currently a nice to have)
# can be updated later to include additional options
# ======================================================================
choices = {
    1:  'rock',
    2:  'paper',
    3:  'scissors'
}

# ======================================================================
# create a class to be used for a user (or computer) making a "choice"
# Inspired by:  https://stackoverflow.com/a/3694822
#
# This also allows you to grow your options, such as providing a username!
# How would you integrate allowing them to provide their name?
# ======================================================================
class Choice(object):
    """
    This class uses object orientation to wrap "data" in a proper class/obj.

    """

    def __init__(self):
        """
        This is the constructor function - also known
        as what happens when this class is created.

        """

        pass

    def input(self):
        """
        This function allows user to provide input.
        Assigns response to the choice attribute.

        """

        pass

    def get_choice(self):
        """
        Returns object's choice attribute data.

        """

        pass


if __name__ == "main":
    """
    This function is only executed if run as a script.
    This particular bare bones STEP3 will only utilize base requirements.
    """

    # ================================================
    # The functions needed are as follows:
    #   - get user input
    #   - generate choice for computer
    #   - calculate winner
    #   - print winner
    # ================================================

    # ================================================
    # Nice to have needs:
    #   - way to store info (database)
    #   - way to retrieve info (to show scoreboard)
    #   - way to email
    #   - expanded logic for additional options
    #   - possibly Jinja2 for a nice HTML look
    # ================================================

    pass

def get_user_input():
    """
    This function has no input required, since it will be generating a response
    from the user. This function will only allow a number between 1 and the
    max number of possible options (base is 3), where each number represents
    the choices available and minimizes user error.

    Returns the integer requested.

    """

    pass


def get_comp_choice():
    """
    This function randomly generates a number between 1 up to and including
    the max number of options. If base, it should be 3. If expanded, it
    will depend on the number of options and logic you have created.

    Returns the integer "chosen" by the computer/randomizer.

    """

    # =====================================================================
    # FOOD FOR THOUGHT:  If we used a class variable for the user's input ...
    # couldn't you create a function in that class to automatically
    # generate the computer response? :-O
    #   - why or why would this NOT be a good idea?
    # =====================================================================

    pass


def calc_winner(user:int, comp:int):
    """
    This function takes 2 integer inputs user and comp. Utilizing the logic
    of your particular RPS game, it will then choose a winner.

    Returns a dictionary like this:

        {
            'winner': 'user' or 'comp',
            'user': {some integer}
            'comp': {some integer}
        }

    To get fancy, you could create a class to have variables - but no need
    other than for practice.

    """

    pass


def print_winner(data_dict:dict):
    """
    This function takes in a dictionary and prints to screen/CLI:
        - who chose what
        - who was the winner

    Returns nothing ... unless you add the data to a file.
    Then you could return the filename to allow them to access it's location.

    """

    pass
