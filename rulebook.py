import curses

# We don't really need the whole rulebook in the code, but if we have the time we can add it here

def rulebook(parameter):
    Explore_the_lost_cities = """
    Explore_the_lost_cities
        Place your cards to form expedition routes that lead
        you to remote and mysterious corners of the world:
        the Himalayan mountains, the Central American
        rainforest, the Egyptian desert, a mysterious volcano,
        and the bottom of the sea. Particularly daring
        players can also make a bet on the success of their
        expeditions. If after three games you have the highest
        overall score, you win.
        Note: The game rules are very simple. But don't get
        the wrong impression — there is much more to Lost
        Cities than it might seem at first glance!
        """

    Game_Components = """
    Game Components:
        • 1 Game board
        • 60 Playing cards:

        • 45 Expedition cards
            (values indicated on the 
            cards: 2-10; in five colors)

        • 15 Wager cards (three of each color)  
        """

    Object_of_the_Game = """
    Object of the Game:
    Both players' goal is to form expedition routes that —
    after subtracting the expedition costs — earn them as
    many discovery points as possible. You set up the
    expeditions by forming a separate column of cards for
    each color. The numeric values within a column of
    cards must increase from card to card. You can place
    wager cards at the beginning of each column to
    multiply a column's value. At the end of the game, the
    cards in each player's columns are scored.
    """



    parameter.addstr(1, 1, Explore_the_lost_cities)
    parameter.addstr(13, 1, Game_Components)
    parameter.addstr(22, 1, Object_of_the_Game)
