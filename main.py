"""
The main file combining all sub packages and letting the AI play snake

creator: Mark Jacobsen
"""
from Game import game
from DataCollector import datacollector


if __name__ == "__main__":
    # Prepare collection of data
    collector = datacollector.DataCollector()

    # run the snake game
    main_game = game.Game(1000, 800)
    main_game.add_external_function(collector.get_screen_data, main_game.screen)
    main_game.run()
