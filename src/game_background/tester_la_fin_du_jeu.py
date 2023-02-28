""" Game Ender Tester

This file contains functions that first checks if the grid is full.
It also checks if there is a possible move and returns all the
possible movements. At the same time, it contains a function that
checks if the game is over.

This file can also be imported as a module and contains the following
functions:
    is_grid_full
    move_possible
    is_game_over
    get_grid_tile_max

PYLINT score = 9.23/10
"""

import sys
from pathlib import Path
import copy
file = Path(__file__). resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

from game_background.gestion_des_deplacements import move_grid

def is_grid_full(grid_game):
    '''
    This function checks if the grid is full.

    Parameters
    --------
    game_grid : list
        The current or updated game grid. It is a list of lists.

    Returns
    --------
    The return is a Boolean variable (True or False)

    '''

    is_full = True
    for line in grid_game:
        for element in line:
            if element in (0, ' '):
                is_full = False
                break
    return is_full

def move_possible(grid):
    '''
    This function aplies the move grid and compares to the original grid. If they
    are equal, the result is False, that means that there is no possible move.


    Parameters
    --------
    grid : list
        The current or updated game grid. It is a list of lists.

    Returns
    --------
    movements : list
        The return is a list of Boolean variables.

    '''
    grid_ori = [copy.deepcopy(grid) for i in range(5)]
    grid_left = move_grid(grid_ori[1], 'left')
    grid_right = move_grid(grid_ori[2], 'right')
    grid_up = move_grid(grid_ori[3], 'up')
    grid_down = move_grid(grid_ori[4], 'down')
    movements = []
    direction = [grid_left, grid_right, grid_up, grid_down]
    for i in range(len(direction)):
        if direction[i] == grid_ori[0]:
            movements.append(False)
        else:
            movements.append(True)
    return movements

def is_game_over(grid):
    '''
    This function checks if the game is over and returns a message
    as response. The message is either "Keep playing" or "You lose"
    depending
    on the case.

    Parameters
    --------
    grid : list
        The current or updated game grid. It is a list of lists.

    Returns
    --------
    It return a message. The message is either "Keep playing"
    or "You lose".

    '''
    movements = move_possible(grid)
    # message = ' '
    if True not in movements:
        return 'You lose'
    else:
        return 'Keep Playing'

def get_grid_tile_max(game_grid):
    '''
    This function gets the greatest tile of the game grid.

    Parameters
    --------
    game_grid : list
        The current or updated game grid. It is a list of lists.

    Returns
    --------
    max(tiles) : int
        It is the maximum/greatest tile of the game grid.

    '''
    tiles = []
    for i in game_grid:
        i = [0 if x == ' ' else x for x in i]
        tiles.extend(i)
    return max(tiles)
