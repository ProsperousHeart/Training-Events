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
# =============================================================================
# More information on logging can be found here:
#   www.blog.pythonlibrary.org/2012/08/02/python-101-an-intro-to-logging
#   www.digitalocean.com/community/tutorials/how-to-use-logging-in-python3
#   www.loggly.com/ultimate-guide/python-logging-basics
# =============================================================================
import logging
logging.basicConfig(
    filename='CiscoLive2018-Step4.log',       # consider using formatting instead
    filemode='w',                       # overwrites the file every time
    level=logging.DEBUG,                # lowest logging level
    format="%(asctime)s|%(levelname)s: %(name)s @ %(lineno)d|%(message)s"
    )
# setup logging buffer for console
console = logging.StreamHandler()
console.setLevel(logging.DEBUG) # all DEBUG or higher will show on console

# set format easy for console to use
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
console.setFormatter(formatter)
logging.getLogger(__name__).addHandler(console)
logger = logging.getLogger(__name__)

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

    Input dictionary example:

        {
            'winner': 'user' or 'comp',
            'user': {some integer}
            'comp': {some integer}
        }

    Returns nothing ... unless you add the data to a file.
    Then you could return the filename to allow them to access it's location.

    """

    logger.debug('Starting print_winner()...')
    logger.debug('Ending print_winner()...')
    # pass


if __name__ == "__main__":
    """
    This function is only executed if run as a script.
    This particular bare bones STEP3 will only utilize base requirements.
    """

    logger.debug('Starting {}()...'.format(__name__))

    # ==========================================================
    # The functions needed are as follows:
    #   - get user input
    #   - generate choice for computer
    #   - calculate winner
    #   - print winner
    #
    #   NOTE:  Be sure that you ALWAYS check the data returned
    #          This ensures you are getting the excct type of
    #          data expected as well as avoid future bugs.
    #          See "complete.py" for everything.
    # ==========================================================
    user = get_user_input()
    comp = get_comp_choice()
    data_dict = calc_winner(user, comp)
    print_winner(data_dict)

    # ================================================
    # Nice to have needs:
    #   - way to store info (database)
    #   - way to retrieve info (to show scoreboard)
    #   - way to email
    #   - expanded logic for additional options
    #   - possibly Jinja2 for a nice HTML look
    # ================================================

    logger.debug('Ending {}()...'.format(__name__))
