""" Movement Management Functions.

This files contains all the functions responsible for moving
the current grid to a desired direction given by the user.

This file can also be imported as a module and contains the following
functions:
    move_row_left
    move_row_right
    move_grid

PYLINT score = 9.50/10
"""

import sys
from pathlib import Path
import numpy as np

file = Path(__file__). resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))


def move_row_left(grid):
    """
    This function moves the grid to the left.

    Inputs
    -------
    grid : list
        A list of lists containing the current game grid.

    Outputs
    -------
        grid : list
        A list of lists containing the modified game grid after the execution of the movement.
    """
    count_var = 0

    for j in range(len(grid)-1):
        sum = grid[j] + grid[j+1]
        first_test_condition = (grid[j] != 0 and (grid[j] == grid[j+1] or sum == 3))
        second_test_condition = (j == 0 or 0 not in grid[0:j])
        if first_test_condition and second_test_condition and sum not in [2, 4]:
            grid[j] = grid[j] + grid[j+1]
            grid[j+1] = 0
            count_var = j+2
            break

    for j in range(count_var, len(grid)):
        if (j != 0 and grid[j] != 0 and grid[j-1] == 0):
            grid[j-1] = grid[j]
            grid[j] = 0

    return grid

def move_row_right(grid):
    """
    This function moves the grid to the right.

    Inputs
    -------
    grid : list
        A list of lists containing the current game grid.

    Outputs
    -------
        grid : list
        A list of lists containing the modified game grid after the execution of the movement.
    """
    size = len(grid)
    for j in reversed(range(1, len(grid))):     #Now we merge tailes that have the same value
        sum = grid[j] + grid[j-1]
        first_test_condition = (grid[j] != 0 and (grid[j] == grid[j-1]) or sum == 3)
        second_test_condition = (j == len(grid) or 0 not in grid[j:len(grid)])
        if  first_test_condition and sum not in [2, 4] and second_test_condition:
            grid[j] = grid[j] + grid[j-1]
            grid[j-1] = 0
            size = j-1
            break

    for j in reversed(range(0, size)):     #First we move all the tailes to the right, when possible
        if (j != (len(grid)-1) and j>=0 and grid[j] != 0 and grid[j+1] == 0):
            grid[j+1] = grid[j]
            grid[j] = 0

    return grid

def move_grid(game_grid, direction):
    """
    This function is the complete movement function that is responsible for
    performing the complete movement of the grid.

    Inputs
    -------
    grid : list
        A list of lists containing the current game grid.

    direction : str
        A string that contains the direction to which the game grid must be moved.

    Outputs
    -------
        game_grid : list
        A list of lists containing the modified game grid after the execution of the movement.
    """
    if direction == "left":
        for grid in game_grid:
            move_row_left(grid)

    elif direction == 'right':
        for grid in game_grid:
            move_row_right(grid)

    elif direction == "up":    # Just need to transpose the matrix of the grid
        game_grid_a = np.array(game_grid)
        game_grid_transp = game_grid_a.transpose()
        for grid in game_grid_transp:
            move_row_left(grid)
        game_grid = game_grid_transp.transpose()
        game_grid = game_grid.tolist()

    elif direction == "down":
        game_grid_a = np.array(game_grid)
        game_grid_transp = game_grid_a.transpose()
        for grid in game_grid_transp:
            move_row_right(grid)
        game_grid = game_grid_transp.transpose()
        game_grid = game_grid.tolist()

    return game_grid
