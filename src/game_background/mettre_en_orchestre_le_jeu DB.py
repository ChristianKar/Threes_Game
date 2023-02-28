""" Whole Game Controller

This file contains functions that ask the user for his/her desired
size and theme. It also gets the score of the player in actual time
and check if it is a new record or not.

This file can also be imported as a module and contains the following
functions:
    is_int
    ask_and_read_grid_size
    ask_and_read_grid_theme
    get_score
    is_record

PYLINT score = 7.31/10
"""
import mysql.connector
import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

import shelve
import os
import pygame
from game_background.grid_threes import get_all_tiles
import MySQLdb
pygame.mixer.init()
pygame.init()
root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
Sounds = {"sound_1": os.path.join(root_dir, "sounds", "sound_5.wav"),
          "sound_2": os.path.join(root_dir, "sounds", "sound_6.wav"),
          "sound_3": os.path.join(root_dir, "sounds", "sound_7.wav"),
          "back_sound": os.path.join(root_dir, "sounds", "musica_naruto.wav")}
record_path = os.path.join(root_dir, "data/high_score", "score_threes_1.txt")


def is_int(sow):
    '''
    This function checks if the input is an integer.

    Parameters
    --------
    sow : int or str or float
        The variable to check.This input can be everything that's why
        we perform this check.
        
    Returns
    --------
    The return is a Boolean variable (True or False)

    '''

    try:
        sow = int(sow)
        return True
    except ValueError:
        return False


def get_score(game_grid):
    '''
    This fuction counts the score of the current game grid.

    Parameters
    --------
    game_grid : list
        The current or updated game grid. It is a list of lists.
        
    Returns
    --------
    score : int
        The current score.

    '''

    tiles = get_all_tiles(game_grid)
    score = 0
    for i in tiles:
        if i not in [0, 1, 2]:
            k = 0
            while True:
                if i%2 == 0:
                    i = i/2
                    k += 1
                else:
                    break
            score = score + 3**(k)
    return score


def is_record(game_grid):
    """Check if the final score is a record.
    
    Parameters
    ----------
    game_grid : list
        list of lists containing the currently game grid.
    
    Returns
    -------
    record : Boolean
        if player got or not a record
    score : int
        player's final score
    pos : int
        player position in the ranking
    """
    record = False
    score = get_score(game_grid)
    while True:
        d = shelve.open(record_path)
        try:
            list_score = d['score']
        except:
            list_score = [0,0,0]
            list_name = ["", "", ""]
            d['score'] = list_score
            d['name'] = list_name
            record =  True
            pos = 0
            break
        for i in range(3):
            pos = i
            if int(score) > int(list_score[i]):
                record = True
                break
            i = 0
        break

    return record, score, int(pos)

def save_record(name, score, pos):
    """
    Saves in a txt file the name, score and position of the player who did the record
    
    Parameters
    ----------
    name : str
        name of the record player
    score : int
        record score
    pos : int
        the position of the record player in the ranking

    Returns
    -------
    None
    """

    d = shelve.open(record_path)
    list_score = d['score']
    list_name = d['name']
    list_name.insert(pos, name)
    list_score.insert(pos, score)
    list_score.pop()
    list_name.pop()
    d['name'] = list_name
    d['score'] = list_score
    d.close()


