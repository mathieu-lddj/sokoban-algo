import os 

map = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 2, 1, 0, 1],
    [1, 0, 0, 3, 0, 1],
    [1, 0, 0, 0, 4, 1],
    [1, 1, 1, 1, 1, 1]
]

render_dict = {0: '⬛', 1: '🧱', 2: '🎯', 3: '📦', 4: '🙂', 5: '🎁'}

def rendering(map):
    for line in map:
        row_str = ''
        for tile in line:
            row_str += render_dict.get(tile, '?')  
        print(row_str)
os.system('cls')
rendering(map)
