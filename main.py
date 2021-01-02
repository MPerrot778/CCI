from src.displayer import Displayer
from src.decode_map import DecodeMap
from src.drone import Drone
from src.bot import Bot
import argparse

if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser(description="Welcome to the drone bot!")
    argument_parser.add_argument("--map", type=str, help="The file path of the game map",
                                 default="levels/easy.txt")
    arguments = argument_parser.parse_args()

    map_decoder = DecodeMap(arguments.map)

    # The Drone has access to the current game map but can see only the top layer
    drone = Drone(map_decoder.scrambled)

    # The bot (AI) knows the end game map (unscrambled) and can interact with the drone
    bot = Bot(map_decoder.unscrambled, drone)

    # TODO: bot playing loop

    # Example usage of Displayer
    displayer = Displayer()
    displayer.display_game_map(map_decoder.scrambled)
    displayer.display_game_map(map_decoder.unscrambled)
    displayer.stop()
