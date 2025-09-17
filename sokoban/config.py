def get_map(map_file):
    with open(map_file) as map:
        lines = [list(line.strip()) for line in map]
    return lines

# Return a list of all tiles of a certain type
def find_tiles(matrice, type):
    tiles_locations = []
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j]==type:
                tiles_locations.append((i,j))
    return tiles_locations



# Up, Left, Down, Right, Reset
moves_input = ("z","q","s","d","r")

# Void, Wall, Player, Object, Goal, Endgame
type_dico = {"0": "🔲", "1": "🧱", "2": "🤠", "3": "🧊", "4": "✨", "5": "🚩"}