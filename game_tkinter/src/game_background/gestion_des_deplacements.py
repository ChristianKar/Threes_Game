import sys  
from pathlib import Path
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory))

from game_background.grid_threes import grid_add_new_tile 
import numpy as np
import copy

# This function moves to the right
global grid

def move_row_left(grid):   # Now we need to the same thing for the left
    a = 0
    
    for j in range(len(grid)-1):            
        sum = grid[j] + grid[j+1]
        if (grid[j] != 0 and (grid[j] == grid[j+1] or sum == 3)) and (j == 0 or 0 not in grid[0:j]) and sum not in [2,4]:
            grid[j] = grid[j] + grid[j+1]
            grid[j+1] = 0
            a = j+2
            break

    for j in range(a, len(grid)):             
        if (j != 0 and grid[j] != 0 and grid[j-1] == 0):
            grid[j-1] = grid[j]
            grid[j] = 0      

    return grid 

def move_row_right(grid):
    a = len(grid)
    for j in reversed(range(1, len(grid))):        # Now we merge tailes that have the same value      
        sum = grid[j] + grid[j-1]
        if (grid[j] != 0 and (grid[j] == grid[j-1]) or sum == 3) and sum not in [2, 4] and (j == len(grid) or 0 not in grid[j:len(grid)]):
            grid[j] = grid[j] + grid[j-1]
            grid[j-1] = 0
            a = j-1
            break

    for j in reversed(range(0, a)):    # First we move all the tailes to the right, when possible         
        if (j != (len(grid)-1) and j>=0 and grid[j] != 0 and grid[j+1] == 0):
            grid[j+1] = grid[j]
            grid[j] = 0   

    return grid

def move_grid(game_grid, move):

    if move == "left":        
        for grid in game_grid:
            move_row_left(grid)
 
    elif(move == 'right'):
        for grid in game_grid:
            move_row_right(grid)

    elif (move == "up"):    # For up and down, we just need to transfor the Grid into a matrix and transpose it
        game_grid_a = np.array(game_grid)
        game_grid_transp = game_grid_a.transpose()
        for grid in game_grid_transp:
            move_row_left(grid)
        game_grid = game_grid_transp.transpose()            
        game_grid = game_grid.tolist()
    
    elif (move == "down"):
        game_grid_a = np.array(game_grid)
        game_grid_transp = game_grid_a.transpose()
        for grid in game_grid_transp:
            move_row_right(grid)
        game_grid = game_grid_transp.transpose()            
        game_grid = game_grid.tolist()
    
    return game_grid
