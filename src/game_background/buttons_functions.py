""" Performed Operations of the Buttons.

This file contains all buttons functions used in the GUI
and the operations they have to perform.

    Functions here defined are used in the graphical interface

PYLINT score = 9.44/10
"""
import shelve
from tkinter.constants import FALSE, TRUE
import pygame
import os
from pygame import mixer

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
path_save = os.path.join(root_dir, "data/save_game", "save_game.txt")

def save_game(game_grid):
    """
    Creates/opens a save_game.txt and saves the current grid

    Inputs
    ----------
    game_grid : list
        A list of lists containing the current/given game grid.

    Outputs/Returns
    -------
        The output is a Boolean value. (True or False)

    """
    recorded_game = shelve.open(path_save)
    recorded_game['last_game'] = game_grid
    recorded_game.close()



def game_saved():
    """
    Checks if there is a saved game

    Inputs
    ----------
        This function has no input.

    Outputs/Returns
    -------
        The output is a Boolean value. (True or False)
    """
    recorded_game = shelve.open(path_save)
    try:
        last_game = recorded_game['last_game']
        if last_game == []:
            return FALSE
        else:
            return TRUE
    except:
        recorded_game['last_game'] = []
        return FALSE



def erases_game():
    """
    Erases a saved game

    Inputs
    ------
        This function has no input.

    Outputs/Returns
    ---------------
        This function has no output.
    """

    recorded_game = shelve.open(path_save)
    recorded_game['last_game'] = []
    recorded_game.close()



def open_save_game():
    """
    Opens the last saved game

    Outputs
    -------
    game_grid : list
        A list of lists containing the saved game grid.
    """
    recorded_game = shelve.open(path_save)
    game_grid = recorded_game['last_game']
    recorded_game.close()
    print("Jogo carregado com sucesso!")
    print(game_grid)
    return game_grid


def mute_unmute_volume(command):
    """
    Mutes and unmutes the music and sounds.

    Input
    ----------
    command : str
        It specifies if the desired action is muting or unmuting.

    Outputs
    -------
        This function has no output.
    """

    if command == "mute":
        pygame.mixer.music.set_volume(0)
    elif command == "unmute":
        pygame.mixer.music.set_volume(1)