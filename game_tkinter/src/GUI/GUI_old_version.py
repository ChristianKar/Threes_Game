import sys  
from pathlib import Path 
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory))

import tkinter as tk
from tkinter import *
from game_background.mettre_en_orchestre_le_jeu_pt2_3 import move_grid, ask_and_read_grid_size, ask_and_read_grid_theme 
from game_background.grid_threes import init_game, grid_add_new_tile
from game_background.tester_la_fin_du_jeu import move_possible
#dic={0: "#8FBC8F", 1: "#FFF8DC", 2: "#FF6347", 3:"#FF6347", 4: "#FFFAF0", 8: "#FFFAF0", 16: "#42ed71", 32: "#17e650", 64: "#17c246", 128: "#149938", 256: "#107d2e", 512: "#0e6325", 1024: "#0b4a1c", 2048: "#031f0a", 4096: "#000000", 8192: "#000000",} 
dict_colors={"background": "#87CEEB", 0: "#8FBC8F", 1: "#FF6347", 2: "#FFFAF0", 3: "#FFFAF0", 6: "#FFFAF0", 12: "#FFFAF0", 24: "#FFFAF0", 48: "#FFFAF0", 96: "#FFFAF0", 192: "#FFFAF0", 384: "#FFFAF0", 768: "#FFFAF0", 1536: "#FFFAF0", 3072: "#FFFAF0", 6144: "#FFFAF0",} 
dict_colors_num={0: "#8FBC8F", 1: "#FFF8DC", 2: "#FFF8DC", 3: "#000000", 6: "#B22222", 12: "#B22222", 24: "#B22222", 48: "#B22222", 96: "#B22222", 192: "#B22222", 384: "#B22222", 768: "#B22222", 1536: "#B22222", 3072: "#B22222", 6144: "#B22222",}

size=0
center = None
grid = []
display_info = None

def graphical_grid_init():
    global size
    global grid
    global center
    global display_info

    root = tk.Tk()
    root.title('THREES!')
    root.iconbitmap('src/GUI/uthrees_icon.ico')  

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    h_dimen = int(screen_height/2)
    w_dimen = int(screen_width/3)

    root.geometry(str(h_dimen)+'x'+str(w_dimen))
    root.minsize('600','300')
    
    lab_up = tk.Frame(root, bg = dict_colors["background"], bd=2)   
    lab_up.grid(sticky=N, columnspan=int(len(grid)))
    
    e = Entry(lab_up, width=20, borderwidth=10)
    e.pack(anchor=W, side=LEFT, fill=BOTH)
    button_save = Button(lab_up, text="Save", font=("Comic Sans MS", int(size)), fg='purple')
    button_save.pack(side=LEFT, padx=5)
    button_restart = Button(lab_up, text="Restart", font=("Comic Sans MS", int(size)), fg='purple')
    button_restart.pack(side=LEFT, padx=5)
    button_help = Button(lab_up, text="Help", font=("Comic Sans MS", int(size)), fg='purple', command=call_help)
    button_help.pack(side=LEFT, padx=5)
    button_mute = Button(lab_up, text="Mute", font=("Comic Sans MS", int(size)), fg='purple')
    button_mute.pack(side=LEFT, padx=5)
    button_quit = Button(lab_up, text="Quit", font=("Comic Sans MS", int(size)), fg='purple')
    button_quit.pack(side=LEFT, padx=5)

    display_info = tk.Label(lab_up, text="Enjoy the game", font=("Comic Sans MS", int(size)), fg='purple', bg=dict_colors["background"], bd=2, padx=2)
    display_info.pack(side=LEFT, padx=5, expand=YES)
    

    center = tk.Frame(root, bg = dict_colors["background"], bd=10, padx=2)

    root.columnconfigure(1, weight=5)
    root.rowconfigure(1, weight=5)
    size = int(len(grid)/10)

    return root, center

def call_help():
    global display_info
    help_text = "Change"
    display_info.set(help_text)
    #display_info.pack(side=LEFT, padx=5, expand=YES)

def graphical_grid_refresh():
    global size
    global center
    global grid
    for i in range(len(grid)):
        for j in range(len(grid)):
            
                  
            center.grid(row=1, column=1, sticky=NSEW)
            center.columnconfigure(i, weight=5, minsize=len(grid))
            center.rowconfigure (j, weight=5, minsize=len(grid))

            text_grid = str(grid[i][j])
            frame = tk.Frame(center, bg=dict_colors["background"], highlightbackground=dict_colors["background"], highlightthickness=1,  padx=3,  pady=3)
            frame.grid(row=i, column=j, sticky=NSEW)
            frame.columnconfigure(i,weight=1)
            frame.rowconfigure(j,weight=1)

            label = tk.Label(frame, text=text_grid, anchor=CENTER, bg=dict_colors_num[grid[i][j]], fg='black', font=("Comic Sans MS", int(size)), relief=RAISED, padx=5, pady=5)
            label.config(anchor=CENTER, justify=CENTER)        
            label.pack(expand=YES, fill=BOTH)


def resize(e):
    global size
    size = (e.width+e.height)/40
    graphical_grid_refresh()

def update_grid(direction):
    global grid
    grid_moved = move_grid(grid, direction) # moves the grid with the input move
    grid_updated = grid_add_new_tile(grid_moved, direction)
    grid = grid_updated

def is_move_possible(direction):
    dir_dic = {"left": 0, "right": 1, "up": 2, "down": 3}    
    possible_moves = move_possible(grid)
    if not possible_moves[dir_dic[direction]]: # If the input move is not possible makes a loop until a valid move is input
        print("Invalid Move")
        return 0

def is_game_over():
    if is_move_possible("left")==0 and is_move_possible("right")==0 and is_move_possible("up")==0 and is_move_possible("down")==0:
        print("game over")
        if get_grid_tile_max(grid) >= 2048:
            print('Congrats! You achieved 2048 :)') # test if the game is over
            end_game = True
        else:
            print('You lose')
            end_game = True


def left(self):
    print("left")
    if is_move_possible("left")==0:
        return
    update_grid("left")
    graphical_grid_refresh()
    is_game_over() 

def right(self):
    print("right")
    if is_move_possible("right")==0:
        return
    update_grid("right")
    graphical_grid_refresh()
    is_game_over()

def up(self):
    print("up")
    if is_move_possible("up")==0:
        return
    update_grid("up")
    graphical_grid_refresh()
    is_game_over()

def down(self):
    print("down")
    if is_move_possible("down")==0:
        return
    update_grid("down")
    graphical_grid_refresh()
    is_game_over()



def play():
    # This function starts the game, asking the user for the desired size and theme
    # input: none
    # output: Winning or losing message
    global grid
    global center
    grid_size = ask_and_read_grid_size()
    grid = init_game(int(grid_size))

    root,center=graphical_grid_init()
    center.bind('<Configure>', resize)

    #end_game = False

    #grid_updated = grid
    graphical_grid_refresh()

    root.bind("<Left>", left)
    root.bind("<Right>", right)
    root.bind("<Up>", up)
    root.bind("<Down>", down)
    root.bind("")
        
    root.mainloop()

if __name__ == '__main__':
    play()
    exit(1)
