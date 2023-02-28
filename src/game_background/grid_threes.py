""" Grid Initialization and Tile Creation and Insertion.

This file contains all the necessary functions for initializing/creating
the grid. Also, it contains the functions for selecting and inserting 9 random
tiles on the initial grid and a random tile as next instertion.

This file can also be imported as a module and contains the following
functions:
    create_grid
    get_value_new_tile
    get_all_tiles
    get_empty_tiles_positions
    grid_add_new_tile
    init_game

PYLINT score = 9.63/10

"""

import sys
from pathlib import Path
import random
file = Path(__file__). resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))



def create_grid(size):
    """
    Creates a squared grid (list of lists) based on the size chosen by the user.

    Parameters
    -------
    size : int
        The size of the grid in which the player wants to play

    Returns
    -------
    game_grid : list
        List of lists containing the created game grid
    """

    game_grid = []
    for _ in range(0, size):
        game_grid.append(size * [0])
    return game_grid


def get_value_new_tile():
    """
    Randomly chooses a value between 1, 2 and 3.
    xl% probability of picking 1, y% of pikcing 2 and z% of picking 3.

    Returns
    -------
    new_value : int
        The randomly picked value.
    """
    list = [1, 2, 3]
    new_value = random.choices(list, weights=(28, 28, 44))[0]
    #[0] is used because choices returns a list
    return new_value



def get_all_tiles(game_grid):
    """
    Get all tiles an put them into a single list.

    Parameters
    -------
    game_grid : list
        A list of lists containing the current game grid.

    Returns
    -------
    tiles : list
        A list containing all the tiles.
    """
    tiles = []
    for i in game_grid:
        i = [0 if x == ' ' else x for x in i]
        tiles.extend(i)
    return tiles


def get_empty_tiles_positions(game_grid, move):
    """
    Gets the position of all empty tiles (value 0)

    Parameters
    ----------
    game_grid : list
        The current game_grid
    move : str
        The desired move from the user.

    Returns
    -------
    empty_tiles : list
        A list with the coordinates (x, y) of all the empty tiles.
    """
    row = -1
    column = -1
    empty_tiles = []
    if move == "up":
        row = len(game_grid)-1
        for j in game_grid[row]:
            column += 1
            if j == 0:
                empty_tiles.append((row, column))
        column = -1
    elif move == "down":
        row = 0
        for j in game_grid[row]:
            column += 1
            if j == 0:
                empty_tiles.append((row, column))
        column = -1
    elif move == "left":
        for i in game_grid:
            row += 1
            if i[len(game_grid)-1] == 0:
                empty_tiles.append((row, len(game_grid)-1))
        column = -1
    elif move == "right":
        for i in game_grid:
            row += 1
            if i[0] == 0:
                empty_tiles.append((row, 0))
    elif move == "random":
        for i in game_grid:
            row += 1
            for j in i:
                column += 1
                if j in (0, ' '): #if j == 0 or j == ' ':
                    empty_tiles.append((row, column))
            column = -1
    return empty_tiles


def get_new_position(game_grid, move):
    """Randomly chooses a position among the list of empty positions.
    All positions have the same probability of being picked (constant distribution)

    Parameters
    ----------
    game_grid : list
        List of lists containing the current game grid
    move : str
        The desired move from the user.


    Returns
    -------
    x_pos : int
        The index of the game_grid element where the position needs to be picked
    y_pos : int
        The index of the game_grid[x] element where the position needs to be picked
    """
    available_places = get_empty_tiles_positions(game_grid, move)
    random_place = random.choices(available_places)
    x_pos = random_place[0][0]
    y_pos = random_place[0][1]
    return x_pos, y_pos



def grid_get_value(game_grid, x_pos, y_pos):
    """
    Gets the value of a tile at a certain given position.

    Parameters
    ----------
    game_grid : list
        List of lists containing the current game grid
    x_pos : int
        The index of the game_grid element where the value will be picked.
    y_pos : int
        The index of the game_grid[x] element where the value will be picked

    Returns
    -------
    value : int
        The value of the specified tile
    """
    value = game_grid[x_pos][y_pos]
    return value



def grid_add_new_tile(game_grid, move, tile_value):
    """
    Ads a new randomly valued (1, 2 or 3) tile to an randomly picked
    available position in game grid.

    Parameters
    ----------
    game_grid : list
        List of lists containing the current game grid
    move : str
        The desired move from the user.
    tile_value : int
        The value of the tile that is going to be added.

    Returns
    -------
    game_grid : list
        List of lists containing the new game grid
    """
    while True:
        x_pos, y_pos = get_new_position(game_grid, move)
        if grid_get_value(game_grid, x_pos, y_pos) == 0: # testing the place is indeed available
            game_grid[x_pos][y_pos] = tile_value
            break
        else:
            continue # It Needs to be DELETED --> Unnecessary "else" after "break"
    return game_grid


def init_game(size):
    """
    Creates a new game grid and adds 9 randomly valued (1, 2 or 3) tiles to
    9 randomly chosen positions to start the game.

    Parameters
    ----------
    size : int
        The size of the lines and columns of the game grid.

    Returns
    -------
    new_grid : list
        List of lists containing the initial game grid.
    """
    new_grid = create_grid(size)
    for _ in range(9):
        new_grid = grid_add_new_tile(new_grid, "random", get_value_new_tile())
    return new_grid


    