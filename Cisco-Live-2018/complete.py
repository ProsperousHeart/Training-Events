# This is step 3 of the "Bare Bones" Process - Creating The Empty Functions
# Here is the process I follow for this phase ...
#
#   1 - write out the comments of expected functions
#   2 - create those functions with proper docstrings, logging, and pass ONLY
#       NOTE:  pass is a null operation (nothing happens) and is therefore
#              only used as a placeholder when no code needs to be executed
#              such as when a function doesn't do anything yet or have logging
#   3 - tie the functions together in your __main__
#   4 - test the logic with print or logging statements

import io
# =============================================================================
# More information on logging can be found here:
#   www.blog.pythonlibrary.org/2012/08/02/python-101-an-intro-to-logging
#   www.digitalocean.com/community/tutorials/how-to-use-logging-in-python3
#   www.loggly.com/ultimate-guide/python-logging-basics
# =============================================================================
import logging
logging.basicConfig(
    filename='CiscoLive2018.log',       # consider using formatting instead
    filemode='w',                       # overwrites the file every time
    level=logging.DEBUG,                # lowest logging level
    format="%(asctime)s:%(levelname)s:%(message)s"
    )
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
loggingBuffer = io.StringIO()
logger.addHandler(logging.StreamHandler(loggingBuffer))

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

        logger.debug('Creating new Choice class object...')
        self.choice = 0     # could set to None, but we expect this to be INT
        logger.debug('Completed creation of new Choice class object...')

        @property
        def choice(self):
            """
            This function returns the attribute:    choice

            """

            logger.debug('Returning choice attribute data...')
            return self.__choice

        @choice.setter
        def choice(self, data):
            """
            This function sets the attribute:   choice

            """

            logger.debug('Setting Choice class attribute for choice...')
            self.__choice = data
            logger.debug('Completed setting Choice class attribute for choice')

    def input(self):
        """
        This function allows user to provide input.
        Assigns response to the choice attribute.

        """

        def check_input(input_str:str):
            """
            This function checks if the input was one of the possible numbers.

            """

            if input_str is not None and type(input_str)

        logger.debug('Requesting input...')
        choice_str = '1 - rock, 2 - paper, 3 - scissors'
        test_bool = True
        while(test_bool):
            input = raw_input('Please provide your choice:  {}'.format(choice_str))
            test_bool = check_input()
        logger.debug('Returning response...')
        # pass


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

    logger.debug('Starting get_user_input()...')
    logger.debug('Ending get_user_input()...')
    # pass

    return None


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

    logger.debug('Starting get_comp_choice()...')
    logger.debug('Ending get_comp_choice()...')
    # pass

    return None


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

    logger.debug('Starting calc_winner()...')
    logger.debug('Ending calc_winner()...')
    # pass

    return None


def print_winner(data_dict:dict):
    """
    This function takes in a dictionary and prints to screen/CLI:
        - who chose what
        - who was the winner

    Returns nothing ... unless you add the data to a file.
    Then you could return the filename to allow them to access it's location.

    """

    logger.debug('Starting print_winner()...')
    logger.debug('Ending print_winner()...')
    # pass
