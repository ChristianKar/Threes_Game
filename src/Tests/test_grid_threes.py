import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

# from game2048.grid_2048 import create_grid
from game_background.grid_threes import create_grid, get_value_new_tile, get_all_tiles, get_empty_tiles_positions, get_new_position, grid_get_value, grid_add_new_tile, init_game
from pytest import *

# A test to try if create_grid function works!


def test_create_grid():
    assert create_grid(4) == [[0, 0, 0, 0], [0, 0, 0, 0], [
        0, 0, 0, 0], [0, 0, 0, 0]]
# test_create_grid() <-- test

'''
# Iteration 1 --> A test to try if a value tile 2 is placed at a given position!
# We changed the create grid to use 0 to be more compatible with the moving tiles functions
def test_grid_add_new_tile_at_position():
    game_grid = create_grid(4)
    game_grid = grid_add_new_tile_at_position(game_grid, 1, 1)
    assert game_grid == [[0, 0, 0, 0], [0, 2, 0, 0], [
        0, 0, 0, 0], [0, 0, 0, 0]]
# test_grid_add_new_tile_at_position() <-- test


# Iteration 2.1 - A test to try if the value of a new tile is 2 or 4.
def test_grid_add_new_tile_at_position():
    game_grid = create_grid(4)
    game_grid = grid_add_new_tile_at_position(game_grid, 1, 1)
    tiles = get_all_tiles(game_grid)
    assert 2 in tiles or 1 in tiles
# test_grid_add_new_tile_at_position() <-- test


# Iteration 2.2 - A test to figure out if we took all tiles in a list!
def test_get_value_new_tile():
    assert get_value_new_tile() in {2, 1, 3}
# test_get_value_new_tile()
'''

# Iteration 2.3 - A test to figure out if we took all tiles in a list!
def test_get_all_tiles():
    assert get_all_tiles([[0, 1, 6, 2], [0, 0, 0, 0], [0, 384, 24, 48], [
                         1536, 3072, 384, 0]]) == [0, 1, 6, 2, 0, 0, 0, 0, 0, 384, 24, 48, 1536, 3072, 384, 0]
    assert get_all_tiles([[12, 1, 6, 2], [2, 1, 2, 96], [1, 384, 24, 48], [1536, 3072, 384, 2]]) == [12, 1, 6, 2, 2, 1, 2, 96, 1, 384, 24, 48, 1536, 3072, 384, 2]
    assert get_all_tiles(create_grid(3)) == [0 for i in range(9)]
#test_get_all_tiles() <-- test


# Iteration 3.1 - A test to try figure out where are the empty grid places.
def test_get_empty_tiles_positions():
    assert get_empty_tiles_positions([[0, 12, 24, 0], [48, 0, 24, 2], [2, 2, 6, 1], [
                                     384, 6, 12, 0]], 'random') == [(0, 0), (0, 3), (1, 1), (3, 3)]
    assert get_empty_tiles_positions(create_grid(2), 'random') == [
        (0, 0), (0, 1), (1, 0), (1, 1)]
    assert get_empty_tiles_positions(
        [[12, 1, 6, 2], [2, 1, 2, 96], [1, 384, 24, 48], [1536, 3072, 384, 2]], 'random') == []
#test_get_empty_tiles_positions() <-- test


# Iteration 3.2 - A test if a new tile is placed randomly in an available square of the game grid.
def test_get_new_position():
    grid = [[0, 12, 24, 0], [48, 0, 24, 2], [2, 2, 6, 1], [384, 6, 12, 0]]
    x, y = get_new_position(grid, 'random')
    assert(grid_get_value(grid, x, y)) == 0
    grid = [[0, 1, 6, 2], [0, 0, 0, 0], [
        0, 384, 24, 48], [1536, 3072, 384, 0]]
    x, y = get_new_position(grid, 'random')
    assert(grid_get_value(grid, x, y)) == 0
# test_get_new_position() <-- test


# Iteration 3.3 - A test to check if my fuction placed in an empty place the 2 or 4.
def test_grid_add_new_tile():
    game_grid = create_grid(4)
    game_grid = grid_add_new_tile(game_grid, 'random',2)
    tiles = get_all_tiles(game_grid)
    assert 2 in tiles or 1 in tiles

# test_grid_add_new_tile()


# Iteration 4 - Test: Add 2 tiles in the playing area!
def test_init_game():
    grid = init_game(4)
    tiles = get_all_tiles(grid)
    assert 2 in tiles or 1 in tiles
    assert len(get_empty_tiles_positions(grid, 'random')) == 7


# test_init_game()
