import sys
import os
from pathlib import Path
file = Path(__file__). resolve()
package_root_directory = file.parents [1]
sys.path.append(str(package_root_directory))

pipPath = f'{os.path.dirname(sys.executable)}\\Scripts'
os.system(f'setx PATH "%PATH%;{pipPath}"')
import pygame
import copy
import tkinter as tk
from game_background.grid_threes import get_value_new_tile
from game_background.mettre_en_orchestre_le_jeu_pt2_3 import move_grid, grid_add_new_tile, move_possible, get_score, init_game, is_int, is_record, Sounds
from game_background.buttons_functions import erases_game, game_saved, mute_unmute_volume, open_save_game, save_game
from tkinter import *
from playsound import playsound as pl
#from carbonai import PowerMeter



#power_meter = PowerMeter(project_name="Threes", program_name="Tkinter", is_online=False, location="FR")

pygame.mixer.init()
pygame.init()


root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
threes_icon = os.path.join(root_dir, "icons", "threes_icon.ico")

dict_colors={"background": "#87CEEB", 0: "#8FBC8F", 1: "#FF6347", 2: "#FFFAF0", 3: "#FFFAF0", 
            6: "#FFFAF0", 12: "#FFFAF0", 24: "#FFFAF0", 48: "#FFFAF0", 96: "#FFFAF0", 192: "#FFFAF0",
            384: "#FFFAF0", 768: "#FFFAF0", 1536: "#FFFAF0", 3072: "#FFFAF0", 6144: "#FFFAF0",}

dict_colors_num={0: "#8FBC8F", 1: "#FFF8DC", 2: "#FFF8DC", 3: "#B9CC3D", 6: "#B22222", 12: "#B22222", 
            24: "#B22222", 48: "#B22222", 96: "#B22222", 192: "#B22222", 384: "#B22222", 768: "#B22222",
            1536: "#B22222", 3072: "#B22222", 6144: "#B22222",}
letter="Comic Sans MS"
size=0
fixed_size = 0
center = None
grid = []
root_welcome = None
the_name_of_the_player = []
var1 = None
unlock = 0
next_tile= 0
mute_status = "unmute"
display_next_tile = None
my_score = 0
display_score = None
label_text = []
old_grid = []

##############################################################################################################################
################################################# GRAPHICAL USER INTERFACE ###################################################
##############################################################################################################################


def reload_saved_game():
    """Open window to ask if player wants to reload last saved game

    Parameters
    ----------
    global grid : list
        A list of lists containing the current game grid

    global center : frame
        A frame used to display the grid

    global size : str
        A string that informs the size of the matrix grid 

    global var1 :
        Parameter of the button, when setted to (1) the button will stop waiting and continue from button_no.wait_variable(var1)
 
    global unlock : int
        Logic used to chose if the button pressed in the reload_saved_game screen was YES or NO 

    global my_score : int
        An integer that stores the current score

    
    Actions
    -------
        Open window and asks if player wants to reload last saved game
    """
    global grid
    global center
    global size
    global var1
    global unlock
    global my_score
    unlock = 0
    

    root_reload = tk.Tk()
    root_reload.title('THREES!')
    root_reload.iconbitmap(threes_icon)
    root_reload.lift()
    root_reload.attributes("-topmost", True)
    root_reload.configure(background=dict_colors["background"])

    var1 = tk.IntVar()

    root_reload.geometry('280'+'x'+'180')
    root_reload.minsize('280','180')
    root_reload.maxsize('280','180')

    infos = tk.Frame(root_reload, bg = dict_colors["background"], bd=2)
    infos.pack(expand=YES)

    hello_message = tk.Label(infos, bg = dict_colors["background"], bd=2, font=(letter, 10), text="WELCOME TO THREES!")   
    hello_message.pack(anchor=CENTER, expand=YES)

    name_message = tk.Label(infos, bg = dict_colors["background"], bd=2, font=(letter, 10), text="There is a saved game available.\nDo you want to continue to play it?")   
    name_message.pack()

    button_yes= tk.Button(infos, text="YES", font=(letter, 10), fg='purple', command=lambda: unlock_button_YES(1))
    button_yes.pack(side=center, padx=5)
    
    button_no= tk.Button(infos, text="NO", font=(letter, 10), fg='purple', command=lambda: unlock_button_NO(2))
    button_no.pack(side=center, padx=5)

    
    button_no.wait_variable(var1)

    if unlock == 1:
        root_reload.destroy()
        grid=open_save_game()
        my_score = get_score(grid)
        root,center=begin_game()

    else:
        root_reload.destroy()
        welcome_screen()
        grid = init_game(int(size))
        root,center=begin_game()

    return root,center


def welcome_screen():
    """Open window to ask the player his username and the desired matrix size

    Parameters
    ----------
    global grid : list
        A list of lists containing the current game grid

    global center : frame
        A frame used to display the grid

    global size : str
        A string that informs the size of the matrix grid 

    global var1 :
        Parameter of the button, when setted to (1) the button will stop waiting and continue from button_no.wait_variable(var1)
 
    global unlock : int
        Logic used to chose if the button pressed in the reload_saved_game screen was YES or NO 

    global root_welcome : Tk root
        The root of the welcome window on which all informations are displayed

    
    Actions
    -------
        Open window and asks the player his username and matrix size
    """

    global grid
    global center 
    global size
    global var1
    global unlock
    global root_welcome
    global the_name_of_the_player

    root_welcome = tk.Tk()
    root_welcome.title('THREES!')
    root_welcome.iconbitmap(threes_icon)
    root_welcome.lift()
    root_welcome.attributes("-topmost", True)
    root_welcome.configure(background=dict_colors["background"])

    var1 = tk.IntVar()

    root_welcome.geometry('280'+'x'+'180')
    root_welcome.minsize('280','180')
    root_welcome.maxsize('280','180')

    infos = tk.Frame(root_welcome, bg = dict_colors["background"], bd=2)
    infos.pack(expand=YES)

    hello_message = tk.Label(infos, bg = dict_colors["background"], bd=2, font=(letter, 10), text="WELCOME TO THREES!")   
    hello_message.pack(anchor=CENTER, expand=YES)

    name_message = tk.Label(infos, bg = dict_colors["background"], bd=2, font=(letter, 10), text="Enter your user name to save your scores")   
    name_message.pack()

    user_name = Entry(infos, width=20, borderwidth=10)
    user_name.pack()

    grid_message = tk.Label(infos, bg = dict_colors["background"], bd=2, font=(letter, 10), text="Enter the matrix size from 3 to 8 (default 4)")   
    grid_message.pack()

    matrix_size = Entry(infos, width=20, borderwidth=10)
    matrix_size.pack()

    button_begin= tk.Button(infos, text="START", font=(letter, 10), fg='purple',command=lambda: check_user_inputs(user_name, matrix_size))
    button_begin.pack(side=center, padx=5)

    button_begin.wait_variable(var1)


def check_user_inputs(user_name, matrix_size):
    """Check if the user inputs are valid

    Parameters
    ----------

    user_name : str
        A string that informs the the username

    global var1 :
        Parameter of the button, when setted to (1) the button will stop waiting and continue from button_no.wait_variable(var1)
 
    global unlock : int
        Logic used to chose if the button pressed in the reload_saved_game screen was YES or NO 

    global root_welcome : Tk root
        The root of the welcome window on which all informations are displayed

    
    Actions
    -------
        Open window and asks the player his username and matrix size
    """
    global the_name_of_the_player
    global var1
    global size
    global fixed_size

    the_name_of_the_player = user_name.get()
    size = matrix_size.get()
    if is_int(size) and len(the_name_of_the_player)!=0:
        if int(size) in [3,4,5,6,7,8]:
            fixed_size = size
            var1.set(1)


def begin_game():
    global size
    global grid
    global center
    global root_welcome
    global next_tile
    global display_next_tile
    global fixed_size
    global my_score
    global display_score

    try:
        root_welcome.destroy()
    except:
        pass
    root = tk.Tk()
    root.title('THREES!')
    root.iconbitmap(threes_icon)
    root.lift()
    root.attributes("-topmost", True)
    root.configure(background=dict_colors["background"])

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    h_dimen = int(screen_height/2)
    w_dimen = int(screen_width/3)

    root.geometry(str(h_dimen)+'x'+str(w_dimen))
    root.minsize('500','300')

    lab_up = tk.Frame(root, bg = dict_colors["background"], bd=2, pady=4)   
    lab_up.grid(columnspan=int(len(grid)))

    fixed_size = int(len(grid))
    size = int(len(grid)/10)

    button_restart = Button(lab_up, text="Restart", font=(letter, 10), fg='purple', command=restart_game)
    button_restart.pack(side=LEFT, padx=5)

    button_mute = Button(lab_up, text="Mute", font=(letter, 10), fg='purple', command=call_mute)
    button_mute.pack(side=LEFT, padx=5)
    
    button_quit = Button(lab_up, text="Quit", font=(letter, 10), fg='purple', command= root.destroy)
    button_quit.pack(side=LEFT, padx=5)

    display_score = Label(lab_up, text=str(my_score), font=(letter, 10), fg='black',background= dict_colors["background"])
    display_score.pack(side=LEFT, padx=20)

    display_next_tile = Label(lab_up, text=str(next_tile), font=(letter, 10), fg='black',background= dict_colors["background"])
    display_next_tile.pack(side=LEFT, padx=20)
    
    center = tk.Frame(root, bg = dict_colors["background"], bd=10, padx=2)

    root.columnconfigure(1, weight=5)
    root.rowconfigure(1, weight=5)
    
    return root, center


def end_game(root):
    """Displays the end game screen

    Parameters
    ----------
    global center : frame
        A frame used to display the grid

    
    Actions
    -------
        Display indicated values in a frame over the older screen
    
    """
    global center
    global the_name_of_the_player
    global my_score

    root_endgame = tk.Tk()
    root_endgame.title('THREES!')
    root_endgame.iconbitmap(threes_icon)
    root_endgame.lift()
    root_endgame.attributes("-topmost", True)
    root_endgame.configure(background=dict_colors["background"])

    root_endgame.geometry('280'+'x'+'480')
    root_endgame.minsize('280','480')
    root_endgame.maxsize('280','480')

    infos = tk.Frame(root_endgame, bg = dict_colors["background"], bd=2)
    infos.pack(expand=YES)

    gameover_message = tk.Label(infos, bg = dict_colors["background"], bd=2, font=(letter, 10), text="GAME OVER!")   
    gameover_message.pack(anchor=CENTER, expand=YES)

    finalscore_message = tk.Label(infos, bg = dict_colors["background"], bd=2, font=(letter, 10), text=("Score of " + str(the_name_of_the_player) + " is : "+ str(my_score)))   
    finalscore_message.pack()


##############################################################################################################################
########################################### VERIFICATIONS AND GRID MANIPULATION ##############################################
##############################################################################################################################

def is_move_possible(direction):
    """Checks if the game is over

    Parameters
    ----------
        direction : string
            A string that informs to what direction the function needs to check movement
        
        global grid : list
            A list of lists containing the current game grid

    Returns
    -------
        int 0
            If the movement is invalid returns 0
    
    """
    global grid

    dir_dic = {"left": 0, "right": 1, "up": 2, "down": 3}    
    possible_moves = move_possible(grid)
    if not possible_moves[dir_dic[direction]]: # If the input move is not possible makes a loop until a valid move is input
        return 0


def update_grid(direction):
    """Updates the current grid to a new grid after a valid movement

    Parameters
    ----------
        direction : string
            A string that informs to what direction the function needs to check movement
        
        global grid : list
            A list of lists containing the current game grid

    Actions
    -------
        If the movement is invalid returns 0
    
    """
    global grid

    grid_moved = move_grid(grid, direction) # moves the grid with the input move
    grid_updated = grid_add_new_tile(grid_moved, direction, next_tile)
    grid = grid_updated


def graphical_grid_refresh_general():
    global size
    global center
    global grid
    global label_text
    global old_grid

    for i in range(len(grid)):
        for j in range(len(grid)):
            if old_grid[i][j] != grid[i][j]:

                text_grid = str(grid[i][j])
                frame = tk.Frame(center, bg=dict_colors["background"], highlightbackground=dict_colors["background"], highlightthickness=1,  padx=3,  pady=3)
                frame.grid(row=i, column=j, sticky=NSEW)
                frame.columnconfigure(i,weight=1)
                frame.rowconfigure(j,weight=1)

                label_text = tk.Label(frame, text=text_grid, anchor=CENTER, bg=dict_colors_num[grid[i][j]], fg='black', font=("Comic Sans MS", int(size)), relief=RAISED, padx=5, pady=5)
                label_text.config(anchor=CENTER, justify=CENTER)        
                label_text.pack(expand=YES, fill=BOTH)
                old_grid[i][j]=grid[i][j]

    pl(Sounds["sound_2"])


def graphical_grid_refresh():
    global size
    global center
    global grid
    global label_text
    global old_grid

    for i in range(len(grid)):
        old_grid = [copy.deepcopy(grid) for i in range(len(grid))]
        for j in range(len(grid)):
            
            old_grid[i].append(grid[i][j])

            center.grid(row=1, column=1, sticky=NSEW)
            center.columnconfigure(i, weight=5, minsize=len(grid))
            center.rowconfigure (j, weight=5, minsize=len(grid))

            text_grid = str(grid[i][j])
            frame = tk.Frame(center, bg=dict_colors["background"], highlightbackground=dict_colors["background"], highlightthickness=1,  padx=3,  pady=3)
            frame.grid(row=i, column=j, sticky=NSEW)
            frame.columnconfigure(i,weight=1)
            frame.rowconfigure(j,weight=1)

            label_text = tk.Label(frame, text=text_grid, anchor=CENTER, bg=dict_colors_num[grid[i][j]], fg='black', font=("Comic Sans MS", int(size)), relief=RAISED, padx=5, pady=5)
            label_text.config(anchor=CENTER, justify=CENTER)        
            label_text.pack(expand=YES, fill=BOTH)

    pl(Sounds["sound_2"])


def is_game_over(root):
    """Checks if the game is over

    Parameters
    ----------
        None

    Actions
    -------
        Executes functions
    
    """
    global grid
    global the_name_of_the_player

    if is_move_possible("left")==0 and is_move_possible("right")==0 and is_move_possible("up")==0 and is_move_possible("down")==0:
        is_record(grid, str(the_name_of_the_player))
        end_game(root)
        erases_game()



##############################################################################################################################
################################################### BUTTONS AND COMMANDS VARIABLES ###################################################
##############################################################################################################################

def restart_game():
    """Order of functions to be executed in order to restart the game if restart button is pressed

    Parameters
    ----------
    global grid : list
        A list of lists containing the current game grid

    global fixed_size : int
        The original matrix size

    global my_score : int
        An integer that stores the current score

    global display_score : label
        A label that display the value of my_score
    
    Actions
    -------
        Executes functions in order to restart the grid to play again
    
    """
    global grid
    global fixed_size
    global my_score
    global display_score

    my_score = 0
    erases_game()
    grid = init_game(int(fixed_size))
    graphical_grid_refresh()
    display_score["text"] = str(my_score)


def call_mute():
    """Activates and deactivates the mute option

    Parameters
    ----------
    global mute_status : str
        A string that informs the current mute status
    
    Actions
    -------
        Changes mute_status and mute or unmute music based on it
    
    """
    global mute_status

    if mute_status == "unmute":
        mute_status = "mute"
        mute_unmute_volume(mute_status)
    elif mute_status == "mute":
        mute_status = "unmute"
        mute_unmute_volume(mute_status)


def unlock_button_YES(x):
    """In function reload_saved_game it's necessary to wait until one of the buttons is pressed, this function together
        with unlock_button_NO do this action to allow reload_saved_game to finish and choose the right action. The three
        functions work together.

    Parameters
    ----------
        global unlock : int
            Logic used to chose if the button pressed in the reload_saved_game screen was YES or NO

    Actions
    -------
        Unlock reload_saved_game screen after a choice was made
    
    """
    global unlock

    unlock = x
    unlock_button_NO(x)


def unlock_button_NO(x):
    """In function reload_saved_game it's necessary to wait until one of the buttons is pressed, this function together
        with unlock_button_YES do this action to allow reload_saved_game to finish and choose the right action. The three
        functions work together.

    Parameters
    ----------
        global var1 
            Parameter of the button, when setted to (1) the button will stop waiting and continue from button_no.wait_variable(var1)
        
        global unlock : int
            Logic used to chose if the button pressed in the reload_saved_game screen was YES or NO

    Actions
    -------
        Unlock reload_saved_game screen after a choice was made
    
    """
    global var1
    global unlock

    unlock = x
    var1.set(1)


def resize(e):
    """Set a new value to size if the game window has been manually resized

    Parameters
    ----------
        global size : str
            A string that informs the size of the matrix grid, now modified to carry the information of the numbers
            displayed on the grid size
        
        e :
            Inner parameter of bind(<"Configure">)

    Actions
    -------
        Call the refresh function given a new size to the text in the 
    
    """
    global size

    size = (e.width+e.height)/40
    graphical_grid_refresh()


def left(root):
    """Order of functions to be executed if laft arrow is pressed

    Parameters
    ----------
    global grid : list
        A list of lists containing the current game grid

    global next_tile : int
        An int generated randomly that indicates which will be next tile appear on the grid

    global display_next_tile : label
        A label that display the value of next_tile

    global my_score : int
        An integer that stores the current score

    global display_score : label
        A label that display the value of my_score
    
    Actions
    -------
        Executes functions and display indicated values
    
    """
    global grid
    global next_tile
    global display_next_tile
    global my_score
    global display_score
    
    if is_move_possible("left")==0:
        return
    update_grid("left")
    graphical_grid_refresh_general()
    save_game(grid)
    my_score = get_score(grid)
    is_game_over(root)
    next_tile = get_value_new_tile()
    display_next_tile["text"]= str(next_tile)
    display_next_tile["background"] = dict_colors_num[next_tile]
    display_score["text"] = str(my_score)
   

def right(root):
    """Order of functions to be executed if right arrow is pressed

    Parameters
    ----------
    global grid : list
        A list of lists containing the current game grid

    global next_tile : int
        An int generated randomly that indicates which will be next tile appear on the grid

    global display_next_tile : label
        A label that display the value of next_tile

    global my_score : int
        An integer that stores the current score

    global display_score : label
        A label that display the value of my_score
    
    Actions
    -------
        Executes functions and display indicated values
    
    """
    global grid
    global next_tile
    global display_next_tile
    global my_score
    global display_score

    if is_move_possible("right")==0:
        return
    update_grid("right")
    graphical_grid_refresh_general()
    save_game(grid)  
    my_score = get_score(grid)
    is_game_over(root)
    next_tile = get_value_new_tile()
    display_next_tile["text"]= str(next_tile)
    display_next_tile["background"] = dict_colors_num[next_tile]
    display_score["text"] = str(my_score)


def up(root):
    """Order of functions to be executed if up arrow is pressed

    Parameters
    ----------
    global grid : list
        A list of lists containing the current game grid

    global next_tile : int
        An int generated randomly that indicates which will be next tile appear on the grid

    global display_next_tile : label
        A label that display the value of next_tile

    global my_score : int
        An integer that stores the current score

    global display_score : label
        A label that display the value of my_score
    
    Actions
    -------
        Executes functions and display indicated values
    
    """
    global grid
    global next_tile
    global display_next_tile
    global my_score
    global display_score

    if is_move_possible("up")==0:
        return
    update_grid("up")
    graphical_grid_refresh_general()
    save_game(grid)
    my_score = get_score(grid)
    is_game_over(root)
    next_tile = get_value_new_tile()
    display_next_tile["text"]= str(next_tile)
    display_next_tile["background"] = dict_colors_num[next_tile]
    display_score["text"] = str(my_score)


def down(root):
    """Order of functions to be executed if down arrow is pressed

    Parameters
    ----------
    global grid : list
        A list of lists containing the current game grid

    global next_tile : int
        An int generated randomly that indicates which will be next tile appear on the grid

    global display_next_tile : label
        A label that display the value of next_tile

    global my_score : int
        An integer that stores the current score

    global display_score : label
        A label that display the value of my_score
    
    Actions
    -------
        Executes functions and display indicated values
    
    """
    global grid
    global next_tile
    global display_next_tile
    global my_score
    global display_score
    
    if is_move_possible("down")==0:
        return
    update_grid("down")
    graphical_grid_refresh_general()
    save_game(grid)
    my_score = get_score(grid)
    is_game_over(root)
    next_tile = get_value_new_tile()
    display_next_tile["text"]= str(next_tile)
    display_next_tile["background"] = dict_colors_num[next_tile]
    display_score["text"] = str(my_score)



##############################################################################################################################
########################################################### GAME PLAY ########################################################
##############################################################################################################################

'''
@power_meter.measure_power(
  package="sklearn",
  algorithm="x",
  data_type="tabular",
  data_shape="x",
  algorithm_params="n_estimators=300, max_depth=15",
  comments="Classifier trained on the MNIST dataset, 3rd test"
'''
def play():
        """Calls, in order, all function necessary to run the game

        Parameters
        ----------
        global grid : list
            A list of lists containing the current game grid

        global center : frame
            A frame used to display the grid

        global size : str
            A string that informs the size of the matrix grid

        global next_tile : int
            An int generated randomly that indicates which will be next tile appear on the grid

        global display_next_tile : label
            A label that display the value of next_tile
        
        Actions
        -------
            Executes functions and display indicated values
            Keeps an open channel to recieve user commands
        
        """
        global grid
        global center
        global size
        global next_tile
        global display_next_tile

        has_game = game_saved()
        if has_game == TRUE:
            pygame.mixer.music.load(Sounds["back_sound"])
            pygame.mixer.music.play(-1)
            root,center = reload_saved_game()
        else:
            pygame.mixer.music.load(Sounds["back_sound"])
            pygame.mixer.music.play(-1)     
            welcome_screen()
            grid = init_game(int(size))
            root,center=begin_game()

        center.bind('<Configure>', resize)
        graphical_grid_refresh()

        next_tile = get_value_new_tile()

        display_next_tile["text"]= str(next_tile)
        display_next_tile["background"] = dict_colors_num[next_tile]
        root.bind("<Left>", lambda root: left(root))
        root.bind("<Right>", lambda root: right(root))
        root.bind("<Up>", lambda root: up(root))
        root.bind("<Down>", lambda root: down(root))
        root.bind("")
                
        root.mainloop()
