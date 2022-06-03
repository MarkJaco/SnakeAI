"""
The main file combining all sub packages and letting the AI play snake

creator: Mark Jacobsen
"""
from Game import game
from Conversion import convert


def get_screen_data(screen):
    """
    get the screen data to recognize objects
    """
    li = convert.pygame_to_list(screen)

if __name__ == "__main__":
    # run the snake game
    main_game = game.Game(1000, 800)
    main_game.add_external_function(get_screen_data, main_game.screen)
    main_game.run()
