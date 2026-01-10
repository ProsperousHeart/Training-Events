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
#   NOTES:
#       - some of the logging is not consistent throughout ... this is
#           intentional so you can see other ways of leaving breadcrumbs
#           for your future self
#       - as mentioned before, there is no one right way to code, so several
#           different styles have been shared here
# =============================================================================
import logging
logging.basicConfig(
    filename='CiscoLive2018-SEMIBASIC-FINAL.log',       # consider using formatting instead
    filemode='w',                       # overwrites the file every time
    level=logging.DEBUG,                # lowest logging level
    format="%(asctime)s|%(levelname)s: %(name)s @ %(lineno)d|%(message)s"
    )
# setup logging buffer for console
console = logging.StreamHandler()
console.setLevel(logging.WARNING) # all WARNING or higher will show on console

# set format easy for console to use
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
console.setFormatter(formatter)
logging.getLogger(__name__).addHandler(console)
logger = logging.getLogger(__name__)

# ===========================================================
# random is a module we will use to generate a random number
# ===========================================================
import random

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
            if input_str is None:
                logger.warning('This should never happen! Input was empty.')
                return (True, None)
            try:
                val = int(input_str)
            except ValueError as err:
                logger.warning('Integer not provided')
                return (True, None)
            if val not in choices.keys():
                logger.warning('Valid integer not provided')
                return (True, None)
            return (False, val)

        logger.debug('Requesting input...')
        choice_str = '1 - rock, 2 - paper, 3 - scissors'
        test_bool = True
        while(test_bool):
            in_put = input('Please provide your choice ({}):  '.format(choice_str))
            logger.debug('Attempting to check input ...')
            test_bool_tup = check_input(in_put)
            test_bool = test_bool_tup[0]
        logger.debug('Input received. Returning response:  {}'.format(test_bool_tup[1]))
        return test_bool_tup[1]


def get_user_input():
    """
    This function has no input required, since it will be generating a response
    from the user. This function will only allow a number between 1 and the
    max number of possible options (base is 3), where each number represents
    the choices available and minimizes user error.

    Returns the integer requested.

    """

    logger.debug('Starting get_user_input()...')
    user_obj = Choice()
    user_obj.choice = user_obj.input()
    logger.debug('Ending get_user_input() & returning:  {}'.format(user_obj.choice))

    return user_obj.choice


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
    random_int = random.randint(1, len(choices.keys()))
    logger.debug('Ending get_comp_choice() & returning:  {}'.format(random_int))
    # pass

    return random_int


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

    def compare(user:int, comp:int):
        """
        Compares values and returns a string of who won.

        From our STEP1-BU-Requirements.md file:

                           1         2          3
                       | ROCK  |   PAPER  | SCISSORS
            1 ROCK     |  tie  |   paper  | rock
            2 PAPER    | paper |    tie   | scissors
            3 SCISSORS |  rock | scissors | tie

        """

        # ============================================================
        # this particular function does not currently check inputs...
        # why or why would you not do this?
        # ============================================================

        logger.debug('Ending calc_winner()...')
        if user == comp:
            return 'Game ended in a tie!'
        elif (user == 1 and comp == 2) or (user == 2 and comp == 3) or (user == 3 and comp == 1):
            return 'Computer Wins!'
        elif (user == 1 and comp == 3) or (user == 2 and comp == 1) or (user == 3 and comp == 2):
            return 'User Wins!'

    logger.debug('Starting calc_winner()...')
    dict2rtn = dict()
    dict2rtn['user'] = user
    dict2rtn['comp'] = comp
    logger.debug('Attempting to call compare()...')
    dict2rtn['winner'] = compare(user, comp)
    logger.debug('Ending calc_winner()...')

    return dict2rtn


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

    # ======================================================================
    # If the incoming dictionary had been a class object, you could minimize
    # code by using the object's internal function ... But then no one could
    # reuse that code unless they imported the class!
    # ======================================================================

    logger.debug('Starting print_winner()...')
    print('User chose:  {}'.format(data_dict['user']))
    print('Comp chose:  {}'.format(data_dict['comp']))
    print(data_dict['winner'])
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
    #   - ability to play more than once (even if not storing data)
    # ================================================

    logger.debug('Ending {}()...'.format(__name__))
