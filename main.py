"""
The main file combining all sub packages and letting the AI play snake

creator: Mark Jacobsen
"""
from Game import game
from Conversion import convert

if __name__ == "__main__":
    # run the snake game
    main_game = game.Game(1000, 800)
    # main_game.run()

    screen = main_game.screen
    li = convert.pygame_to_list(screen)
    print(li)