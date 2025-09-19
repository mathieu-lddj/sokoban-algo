

from config import get_map, moves_input, type_dico, find_tiles

class Game:
    def __init__(self):
        self.__actual_level = 1
        self.__map = get_map(f"../maps/map {self.__actual_level}.txt") # Matrice
        self.__player_loc = None
        self.__objects_placed = False
        self.__under_player_type = "0" # Type of the tile under the player
        self.__goals_located = False # To only find them once
        self.__goals_locations = []
        self.__exit_spawned = False
        self.__never_located = True # To know where to spawn the exit
        self.__exit_spawn_loc = None
        self.__game_won = False


    def print_map(self):
        for line in self.__map:
            row_str = ''
            for tile in line:
                row_str += type_dico.get(tile, '?')
            print(row_str)


    def in_bounds(self, y, x):
        return 0 <= y < len(self.__map) and 0 <= x < len(self.__map[y])


    def reset_game(self):
        self.__map=get_map(f"../maps/map 1.txt")
        self.__actual_level = 1
        self.__player_loc = None
        self.__objects_placed = False
        self.__under_player_type = "0"
        self.__goals_located = False
        self.__goals_locations = []
        self.__exit_spawned = False
        self.__never_located = True
        self.__exit_spawn_loc = None
        self.level_won = False
        self.__game_won = False





    def move(self):

        if self.__game_won:
            direction = input(f"Partie terminée. Appuyez sur {moves_input[4]} pour reset : ")
            while direction != moves_input[4]:
                print("Partie terminée. Seul RESET est autorisé.")
                direction = input(f"Appuyez sur {moves_input[4]} pour reset : ")
            self.reset_game()
            return







        direction = input(f"Vous pouvez RESET avec {moves_input[4]}.\n"
                              f"Choisissez votre direction ({moves_input[0]}, {moves_input[1]}, {moves_input[2]}, {moves_input[3]}) : ")
        while direction not in moves_input:
            print("Input non valide")
            direction = input(f"Vous pouvez RESET avec {moves_input[4]}.\n"
                              f"Choisissez votre direction ({moves_input[0]}, {moves_input[1]}, {moves_input[2]}, {moves_input[3]}) : ")

        # Player location
        y, x = find_tiles(self.__map, "2")[0]

        # To know where to spawn the exit
        if self.__never_located:
            self.__exit_spawn_loc = (y, x)
            self.__never_located = False

        if direction == moves_input[4]:
            self.reset_game()
            return


        # Vectors
        elif direction == moves_input[0]:
            vec = (-1, 0)
        elif direction == moves_input[1]:
            vec = (0, -1)
        elif direction == moves_input[2]:
            vec = (1, 0)
        else:
            vec = (0, 1)

        dy, dx = y + vec[0], x + vec[1]

        # Stop from moving if no tile after
        if not self.in_bounds(dy, dx):
            return

        VOID, WALL, PLAYER, OBJECT, GOAL, EXIT = "0", "1", "2", "3", "4", "5"
        ACTUAL_POS = self.__map[y][x]
        IN_FRONT = self.__map[dy][dx]

        if IN_FRONT == VOID:
            self.__map[y][x] = self.__under_player_type
            self.__under_player_type = self.__map[dy][dx]
            self.__map[dy][dx] = PLAYER

        elif IN_FRONT == WALL:
            return

        elif IN_FRONT == OBJECT:
            dy2, dx2 = y + 2*vec[0], x + 2*vec[1]
            # Stop from pushing if no tile after
            if not self.in_bounds(dy2, dx2):
                return
            TWO_AHEAD = self.__map[dy2][dx2]
            if TWO_AHEAD in (OBJECT, WALL):
                return
            elif TWO_AHEAD == GOAL:
                self.__map[dy2][dx2] = OBJECT
                self.__map[dy][dx] = PLAYER
                self.__map[y][x] = self.__under_player_type
                self.__under_player_type = VOID
            else:
                self.__map[y][x] = self.__under_player_type
                self.__map[dy][dx] = PLAYER
                self.__map[dy2][dx2] = OBJECT
                self.__under_player_type = VOID

        elif IN_FRONT == GOAL:
            self.__map[y][x] = self.__under_player_type
            self.__under_player_type = self.__map[dy][dx]
            self.__map[dy][dx] = PLAYER





        elif IN_FRONT == EXIT:
            self.__map[y][x] = self.__under_player_type
            self.__map[dy][dx] = PLAYER

            if self.__actual_level < 5:
                self.__actual_level += 1
                self.__map = get_map(f"../maps/map {self.__actual_level}.txt")
                self.level_won = True
                # reset flags
                self.__exit_spawned = False
                self.__goals_located = False
                self.__goals_locations = []
                self.__objects_placed = False
                self.__never_located = True
            else:
                self.call_win()
                return  # important: on fige l'état de fin



    def spawn_exit(self):
        if not self.__exit_spawned:
            y,x = self.__exit_spawn_loc
            self.__map[y][x] = "5"
            self.__exit_spawned = True
            self.level_won = False # Reset for the next level

    def check_objects_placed(self):
        # Find the goals locations if never did
        if not self.__goals_located:
            self.__goals_locations = find_tiles(self.__map, "4")
            self.__goals_located = True

        # Check if all goals became objects
        objects_locations = find_tiles(self.__map, "3")
        if set(self.__goals_locations) == set(objects_locations):
            self.__objects_placed = True
            self.spawn_exit()

        # With that the goal is still there if we remove the object from it
        for loc in self.__goals_locations:
            if self.__map[loc[0]][loc[1]] == "0":
                self.__map[loc[0]][loc[1]] = "4"

    # Win event
    def call_win(self):
        self.__game_won = True
        print("\n🎉 Niveau 5 terminé ! Fin du jeu.\nAppuyez sur 'r' pour recommencer.")
        return True
























        