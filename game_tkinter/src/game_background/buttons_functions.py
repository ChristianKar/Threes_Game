import shelve
from tkinter.constants import FALSE, TRUE
import pygame
from pygame import mixer


def save_game(game_grid):
    """Creates/opens a save_game.txt and saves the current grid

    Parameters
    ----------
    game_grid : list
        A list of lists containing the current game grid
    
    Returns
    -------
        True or False
    
    """
    d = shelve.open('src\data\save_game\save_game.txt')
    d['last_game'] = game_grid
    d.close()


def game_saved():
    """Checks if there is a saved game

    Returns
        True or False
    """
    d = shelve.open('src\data\save_game\save_game.txt')
    try:
        last_game = d['last_game']
        if last_game == []:
            return FALSE
        else:
            return TRUE
    except:
        d['last_game'] = []
        return FALSE


def erases_game():
    """Erases a saved game"""

    d = shelve.open('src\data\save_game\save_game.txt')
    d['last_game'] = []
    d.close()


def open_save_game():
    """Opens the last saved game
    
    Returns
    -------
    game_grid : list
        A list of lists containing the saved game grid
    """
    d = shelve.open('src\data\save_game\save_game.txt')
    game_grid = d['last_game']
    d.close()
    print("Jogo carregado com sucesso!")
    print(game_grid)
    return game_grid


def mute_unmute_volume(command):
    """Mutes and unmutes the music and sounds
    
    Parameters
    ----------
    command : str
        specify if the desired action is muting or unmuting
    """

    if command == "mute":
        pygame.mixer.music.set_volume(0)
    elif command == "unmute":
        pygame.mixer.music.set_volume(1)

def nova_funcao():
    print("teste")