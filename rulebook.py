import curses
from player import screen_cols
# We don't really need the whole rulebook in the code, but if we have the time we can add it here

def rulebook(parameter):
    parameter.clear()

    rulebook_1 = """
================================================================
                LOST CITIES - PYTHON EDITION
================================================================

OBJECTIVE:
Mount profitable expeditions to the five Lost Cities (Himalayas, 
Rainforest, Desert, Volcano, and Neptune). 

To succeed, you must play cards in ascending order for each color. 
However, starting an expedition costs points, so ensure you make 
enough progress to turn a profit!

----------------------------------------------------------------
                        HOW TO PLAY
----------------------------------------------------------------
The game consists of cards numbered 2-10 in 5 colors, plus 3
Wager cards per color.

1. STARTING AN EXPEDITION:
- You build expeditions by playing cards of the matching color.
- Cards must be played in ASCENDING numeric order (e.g., you 
    cannot play a 4 after a 7).
- Wager cards represent investments. They multiply your 
    score but must be played BEFORE any number cards of that
    color.

2. TURN SEQUENCE:
A turn consists of two phases: 
(A) Play or Discard a card.
(B) Draw a new card.
        """

    rulebook_2 = """
----------------------------------------------------------------
                        CONTROLS
----------------------------------------------------------------
PHASE 1: ACTION (Play or Discard)
[LEFT] / [RIGHT] : Highlight a card in your hand.
[DOWN] ARROW     : PLAY the selected card to its expedition.
[UP] ARROW       : DISCARD the selected card to the central pile.

PHASE 2: DRAW
[LEFT] / [RIGHT] : Select a pile to draw from (Main Deck or 
                    any of the 5 Color Discard Piles).
                    *Note: You cannot draw a card you just discarded.
[DOWN] ARROW     : CONFIRM DRAW to end your turn.

----------------------------------------------------------------
                        SCORING
----------------------------------------------------------------
At the end of the game, each color/expedition is scored separately:

1. SUM: Add up the values of all number cards in the expedition.
2. COST: Subtract 20 points (the cost of starting an expedition).
* If you played NO cards for a color, the score is 0.
3. MULTIPLIER: 
- 1 Wager card  = Score x 2
- 2 Wager cards = Score x 3
- 3 Wager cards = Score x 4
4. BONUS: If an expedition has 8 or more cards, add +20 points 
(after the multiplier calculation).

SCORING EXAMPLES:
- Cards: [Wager, 2, 5, 10]
Su
- Cards: [4, 6, 7, 8]
Sum: 25. Cost: -20. Net: 5. No Multiplier. Final = 5.

=====m: 17. Cost: -20. Net: -3. Multiplier (x2): Final = -6.
===========================================================
"""
    count = 1
    for line in rulebook_1.splitlines():
            parameter.addstr(count, 1, line)
            count += 1

    count = 1
    for line in rulebook_2.splitlines():
            parameter.addstr(count, (screen_cols // 2) + 1, line)
            count += 1

    parameter.refresh()
    parameter.getch()