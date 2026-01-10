# Main Requirements

Your business unit has requested that you make a rock, paper, scissors
game that employees' kids can play when they visit their parents.

And they want it done in a month.

That's all they want, have at it.

Well ... great. So let's talk about what's possible.

## Base Needs

Start from ground floor. What are the base requirements of a simple
rock, paper, scissors game?

1 - there are 2 players<br>
2 - there are some number of combinations to create a tie / winner<br>
3 - there are at minimum 3 options<br>
4 - need some way to view the winner

## Nice To Have (More Complexity)

What are some things that would make this a better user experience?
- more options (Lizard or Spock, anyone?)
- ability to have best X out of Y games
- scoreboard
- ability to email or print result
- visualize the number of games and compare results and losses
- allow user to play multiple times without having to run script each time
    (no database required for this one since you're not storing anything)

# Resources Needed

Python is a given.

Will you need another module to be able to complete something? Like pyxlsx
to create an Excel file, or sqlite3 / mongoDB to create a database?

Gather these requirements beforehand, including any documentation
you feel you may need when you're ready to work on those pieces.

## Logic

You will also need to do a logical mapping of winning combinations:

         | ROCK  |   PAPER  | SCISSORS
ROCK     |  tie  |   paper  | rock
PAPER    | paper |    tie   | scissors
SCISSORS |  rock | scissors | tie

If you decide to expand on your options, be sure to redo your logic.

Or leverage your time by using someone else's work like [this fine specimen](https://www.liquidfractal.org/gallery/image/196-rock-paper-scissors-lizard-spock-spider-man-batman-wizard-glock)!

# Timelines

This is really based on how often the BU wants an update (it is suggested
at least once a week to provide major accomplishments & and anything
that may be holding you back).

You should also consider having a daily scrum update. Takes about 15 minutes
where you and your team meet up to share:
- accomplishments
- what you're working on that day
- any road blocks you may have

This not only keeps your team accountable, but you will have a better grasp
on the situation if you're not meeting deadlines.
