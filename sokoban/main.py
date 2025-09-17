from classes import Game
import os

game = Game()

while True:
    game.check_objects_placed()
    game.print_map()
    game.move()
    os.system("clear")
