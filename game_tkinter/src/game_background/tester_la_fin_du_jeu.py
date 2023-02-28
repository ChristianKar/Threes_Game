import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory))

import copy
from game_background.gestion_des_deplacements import move_grid

def is_grid_full(grid_game):

    is_full = True
    for line in grid_game:
        for element in line:
            if element == 0 or element == ' ':
                is_full = False
                break
    return is_full

def move_possible(grid):    # This function aplies the move grid and compares to the original grid. If they are equal, the result is False, that means that there is no possible left 
    grid_ori = [copy.deepcopy(grid) for i in range(5)]
    grid_left = move_grid(grid_ori[1], 'left')
    grid_right = move_grid(grid_ori[2], 'right')
    grid_up = move_grid(grid_ori[3], 'up')
    grid_down = move_grid(grid_ori[4], 'down')
    movements = []
    direction = [grid_left, grid_right,grid_up, grid_down]
    for i in range(len(direction)):
        if direction[i] == grid_ori[0]:
            movements.append(False)
        else:
            movements.append(True)
    return movements

def is_game_over(grid):
    movements = move_possible(grid)
    message = ' '
    if True not in movements:
        return 'You lose'
    else:
        return 'Keep Playing'

def get_grid_tile_max(game_grid):
    tiles = []
    for i in game_grid:
        i = [0 if x == ' ' else x for x in i]
        tiles.extend(i)
    return max(tiles)