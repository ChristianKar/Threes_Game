import sys  
from pathlib import Path 
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory))

from game_background.grid_threes import init_game, grid_add_new_tile, get_all_tiles, get_value_new_tile
from game_background.affiche_grille import THEMES, grid_to_string_with_size_and_theme
from game_background.gestion_des_deplacements import move_grid
from game_background.tester_la_fin_du_jeu import get_grid_tile_max, is_game_over, move_possible
from game_background.buttons_functions import mute_unmute_volume
from playsound import playsound as pl
from numpy import UFUNC_PYVALS_NAME, void 
from pygame import mixer
import pygame
import os
import shelve

pygame.mixer.init()
pygame.init()
root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
Sounds = {"sound_1": os.path.join(root_dir, "sounds", "sound_5.wav"), "sound_2": os.path.join(root_dir, "sounds", "sound_6.wav"),
         "back_sound": os.path.join(root_dir, "sounds", "musica_naruto.wav")}


def is_int(s):
    # this function checks if the input is an integer
    # input: the variable to check
    # output: Boolean
    try:
        s = int(s)
        return True
    except ValueError:
        return False


def ask_and_read_grid_size():
    # This function gets the desired size to the grid from a user input.
    # It also ensures that the size is an integer 
    # input: none
    # output: the chosen size for the grid   
    while True:
        size = input("Insert the size of your grid (choose between 3 and 8):\n ")
        
        if is_int(size) and 3<=int(size)<=8: # The user can choose a grid size between 3 and 8 as size to the grid
            print("You chose the size:", size)
            break
        else:
            print("The inserted value is not an integer between 3 and 8 \n")
    return size


def ask_and_read_grid_theme():
    # This function will get, as input from the user, the desired theme. User choose between 3 possible themes
    # input: none
    # output: the chosen theme
    values = ["0", "1", "2"]
    while True:
        theme = input("\n\n Choose your theme: \n 0- Number(classical) \n 1- Chemistry \n 2- Alphabet \n")
        if isinstance(theme, str) and theme in values:
            print("You chose the theme:", theme)
            break
        else:
            print("The inserted value is not 0, 1 or 2")
    return theme

def get_score(game_grid):
    tiles = get_all_tiles(game_grid)
    score = 0
    for i in tiles:
        if i != 0:
            if i not in [1, 2]:
                k = 0
                while True:
                    if i%2 == 0:
                        i = i/2
                        k += 1
                    else:
                        break
                score = score + 3**(k)
    return score


def is_record(game_grid, name):
    score = get_score(game_grid)
    while True:
        d = shelve.open('src\data\high_score\score_threes_1.txt')
        try:
            list_score = d['score']
            list_name = d['name']
        except:
            list_score = [score,0,0]
            list_name = [name, '', '']
            d['score'] = list_score
            d['name'] = list_name
            d.close()
            print("\nCongratulations, new highest score achieved!!\n\n ", score, "points")
            break
        for i in range(3):
            if int(score) > int(list_score[i]):
                list_name.insert(i, name)
                list_score.insert(i, score)
                list_score.pop()
                list_name.pop(0)
                d['score'] = list_score
                d['name'] = list_name
                positions = ['', ' second ', ' third ']
                print("\nCongratulations, new", positions[i], "highest score achieved!!\n\n ", score, "points")
                d.close()
                break
        break
    print("\n***HIGHEST SCORES***\n1- ",list_name[0], " : ", list_score[0],
        "\n2- ", list_name[1], " : ", list_score[1], "\n3- ", 
        list_name[2], " : ", list_score[2])


def play():
    # This function starts the game, asking the user for the desired size and theme
    # input: none
    # output: Winning or losing message
    # size = ask_and_read_grid_size()
    # theme = ask_and_read_grid_theme()
    size = int(5)
    theme = "0" 
    initial_grid = init_game(int(size))
    pygame.mixer.music.load(Sounds["back_sound"])
    pygame.mixer.music.play(-1)
    print(grid_to_string_with_size_and_theme(
        initial_grid, THEMES[str(theme)], int(size))) # Display the created grid, according to size and theme parameters
    end_game = False
    directions = ["left", "right", "up", "down"]
    dir_dic = {"left": 0, "right": 1, "up": 2, "down": 3}
    grid_updated = initial_grid
    x = 0
    while end_game == False: # Until the game is not ended, this loop will continue to get user's moves
        direction = input('Choose your move:')
        if direction not in directions: # test if the input command is valid
            print(grid_to_string_with_size_and_theme(
                    grid_updated, THEMES[str(theme)], int(size)))
            print("Invalid command: Choose left, right, up or down")
            continue
        possible_moves = move_possible(initial_grid)
        while not possible_moves[dir_dic[direction]]: # If the input move is not possible makes a loop until a valid move is input
            print("Invalid Move")
            direction = input('Choose your move:')
            if direction not in directions:
                print(grid_to_string_with_size_and_theme(
                    grid_updated, THEMES[str(theme)], int(size)))
                print("Invalid command: Choose left, right, up or down")
                continue
            
        grid_moved = move_grid(initial_grid, direction) # moves the grid with the input move        
        pl(Sounds["sound_2"])
        if x == 0:
            mute_unmute_volume("mute")
            x = 1
        elif x == 1:
            mute_unmute_volume("unmute")
            x = 0 
        tile_value = get_value_new_tile()
        grid_updated = grid_add_new_tile(grid_moved, direction, tile_value)
        print(grid_to_string_with_size_and_theme(grid_updated, THEMES[str(theme)], int(size))) 
        # printing the new grid
    
        initial_grid = grid_updated
    
    is_record(initial_grid) 

if __name__ == "__main__":
    play()
