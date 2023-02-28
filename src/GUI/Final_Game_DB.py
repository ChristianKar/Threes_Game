import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory))

from game_background.tester_la_fin_du_jeu import is_game_over, get_grid_tile_max  
from playsound import playsound as pl
from GUI.constants import back_color_pallet, number_color_pallet, usual_fonts
from game_background.mettre_en_orchestre_le_jeu import Sounds, is_record, save_record, get_score
from pygame.locals import *
from game_background.grid_threes import *
from game_background.gestion_des_deplacements import move_grid
from game_background.tester_la_fin_du_jeu import move_possible
from game_background.buttons_functions import *
import MySQLdb
import os


root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
record_path = os.path.join(root_dir, "data/high_score", "score_threes_1.txt")
image_path_1 = os.path.join(root_dir, "icons", "icon_download.png")
image_path_2 = os.path.join(root_dir, "icons", "icon_exit.png")
image_path_3 = os.path.join(root_dir, "icons", "icon_mute.png")
image_path_4 = os.path.join(root_dir, "icons", "icon_play.png")
image_path_5 = os.path.join(root_dir, "icons", "icon_restart.png")
image_path_6 = os.path.join(root_dir, "icons", "icon_menu.png")
image_path_7 = os.path.join(root_dir, "icons", "threes_icon.ico")
image_path_8 = os.path.join(root_dir, "icons", "icon_save.png")
record_path = os.path.join(root_dir, "data/high_score", "score_threes_1.txt")

global running_game
global running_record
running_game = False
running_record = False

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)

def wait_for_key():
    for event in pygame.event.get():
        if event.type == QUIT:
            return 'q'
        if event.type == KEYDOWN:
            if event.key == K_UP:
                return 'u'
            elif event.key == K_DOWN:
                return 'd'
            elif event.key == K_RIGHT:
                return 'r'
            elif event.key == K_LEFT:
                return 'l'
            elif event.key == K_q or event.key == K_ESCAPE:
                return 'q'
            elif event.key == K_BACKSPACE:
                return 'bck'

def up(screen, grid, tile, score,build_game,size):
    global running_game
    global running_record
    if move_possible(grid)[2] == False:
        #pl(Sounds['sound_3'])
        return grid, tile
    else:
        pl(Sounds["sound_2"])
        grid = move_grid(grid,"up")
        grid = grid_add_new_tile(grid, "up", tile)
        next_tile = get_value_new_tile()
        score = get_score(grid)
        save_game(grid)
        build_game.draw_game(screen, grid, next_tile, score,size)
        pygame.display.flip()
        if is_game_over(grid) == 'You lose':
            running_game = False
            running_record = True
            erases_game()
            return grid, next_tile

        return grid, next_tile

def down(screen, grid, tile, score, build_game,size):
    global running_game
    global running_record
    if move_possible(grid)[3] == False:
        #pl(Sounds['sound_3'])
        return grid, tile
    else:
        pl(Sounds["sound_2"])
        grid = move_grid(grid,"down")
        grid = grid_add_new_tile(grid, "down", tile)
        next_tile = get_value_new_tile()
        score = get_score(grid)
        save_game(grid)
        build_game.draw_game(screen, grid, next_tile, score,size)
        pygame.display.flip()
        if is_game_over(grid) == 'You lose':
            running_game = False
            running_record = True
            erases_game()
            return grid, next_tile
        return grid, next_tile

def left(screen, grid, tile, score, build_game,size):
    global running_game
    global running_record
    if move_possible(grid)[0] == False:
        #pl(Sounds['sound_3'])
        return grid, tile
    else:
        pl(Sounds["sound_2"])
        grid = move_grid(grid,"left")
        grid = grid_add_new_tile(grid, "left", tile)
        next_tile = get_value_new_tile()
        score = get_score(grid)
        save_game(grid)
        build_game.draw_game(screen, grid, next_tile, score,size)
        pygame.display.flip()
        if is_game_over(grid) == 'You lose':
            running_game = False
            running_record = True
            erases_game()
        return grid, next_tile


def right(screen, grid, tile, score, build_game,size):
    global running_game
    global running_record
    if move_possible(grid)[1] == False:
        #pl(Sounds['sound_3'])
        return grid, tile
    else:
        pl(Sounds["sound_2"])
        grid = move_grid(grid,"right")
        grid = grid_add_new_tile(grid, "right", tile)
        next_tile = get_value_new_tile()
        score = get_score(grid)
        save_game(grid)
        build_game.draw_game(screen, grid, next_tile, score,size)
        if is_game_over(grid) == 'You lose':
            running_game = False
            running_record = True
            erases_game()  
        pygame.display.flip()
        return grid, next_tile


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        COLOR_INACTIVE = pygame.Color('lightskyblue3')
        COLOR_ACTIVE = pygame.Color('dodgerblue2')
        FONT = pygame.font.Font(None, 32)
        
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                    self.txt_surface = FONT.render(self.text, True, self.color)
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                    self.txt_surface = FONT.render(self.text, True, self.color)
                else:
                    self.text += event.unicode
                    self.txt_surface = FONT.render(self.text, True, self.color)
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)
                

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


class Button:    
    def __init__(self,text,width,height,pos,elevation, gui_font, top_color, bot_color, cover_color, image = None):
        #Core attributes 
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]
        self.width=width
        self.height=height
        self.pos=pos
        self.cover_color = cover_color
        # top rectangle 
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = top_color
        self.top_color_original = top_color

        # bottom rectangle 
        self.bottom_rect = pygame.Rect(pos,(width,height))
        self.bottom_color = bot_color
        #text
        self.default_font = gui_font
        self.text = text
        self.text_surf = gui_font.render(text,True,'#FFFFFF') 
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
        self.button_icon = image

    def change_text(self, newtext):
        self.text_surf = self.default_font.render(newtext, True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center) 
    def draw(self, screen):
        # elevation logic 
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center    
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation 
        pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 7)
        pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 7)
        if self.button_icon != None:
            self.image_rect = self.button_icon.get_rect(center = self.top_rect.center)
            screen.blit(self.text_surf, self.text_rect)
            screen.blit(self.button_icon,self.image_rect)
        else:
            screen.blit(self.text_surf, self.text_rect)
        if self.check_click()==True: return True    
    def check_click(self):    
        mouse_pos = pygame.mouse.get_pos()  
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = self.cover_color
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
                self.change_text(f"{self.text}")
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    #print('click')
                    self.pressed = False
                    self.change_text(self.text)
                    return True
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = self.top_color_original


class Initial_Screen:
    def __init__(self, screen, title_font, medium_font):

        # Filling the windown with blank
        screen.fill(back_color_pallet['screen_back'])

        # Creating initial title
        title_surface_1 = title_font.render('    rees', False, number_color_pallet['title_1'])
        title_surface_2 = title_font.render('T', False, number_color_pallet['title_2'])
        title_surface_3 = title_font.render('  h', False, number_color_pallet['title_3'])
        title_rect_1 = title_surface_1.get_rect(center= (screen.get_width()/2,screen.get_height()/2 - 100))
        title_rect_2 = title_surface_1.get_rect(center= (screen.get_width()/2+15,screen.get_height()/2 - 100))
        title_rect_3 = title_surface_1.get_rect(center= (screen.get_width()/2+6,screen.get_height()/2 - 100))

        # Creating buttons subtitles
        start_text_surface = medium_font.render('New game', False, number_color_pallet['text_1'])
        start_text_rect = start_text_surface.get_rect(center = (screen.get_width()/2 + 95,screen.get_height()/2))
        exit_text_surface = medium_font.render('Exit game', False, number_color_pallet['text_1'])
        exit_text_rect = exit_text_surface.get_rect(center = (screen.get_width()/2 + 95,screen.get_height()/2 + 120))
        load_text_surface = medium_font.render('Load game', False, number_color_pallet['text_1'])
        load_text_rect = load_text_surface.get_rect(center= (screen.get_width()/2 + 95,screen.get_height()/2 +60))

        # Creating size buttons explanation text

        text_size_surface = medium_font.render('Choose grid size: ', False, number_color_pallet['text_1'])
        text_size_rect = text_size_surface.get_rect(center = (105,(screen.get_height()-40)/2 + 30))

        # Blit the title in the screen
        screen.blit(title_surface_1,title_rect_1)
        screen.blit(title_surface_2,title_rect_2)
        screen.blit(title_surface_3,title_rect_3)

        # Blit the support text for size in the screen
        screen.blit(text_size_surface,text_size_rect)

        # Blit the subtitles of the buttons in the screen
        screen.blit(start_text_surface,start_text_rect)
        screen.blit(exit_text_surface,exit_text_rect)
        screen.blit(load_text_surface,load_text_rect)


class Build_Game:
    def __init__(self, num_font_1, num_font_2, num_font_3):
        self.num_font_1 = num_font_1 
        self.num_font_2 = num_font_2 
        self.num_font_3 = num_font_3

    def draw_game(self, screen, grid, next_tile, score, size):
        # Creating list of tiles
        tiles_dic = {}
        # Filling the windown with blank
        # screen.fill(back_color_pallet['screen_back'])

        # Constants of sizes we need
        W = 300
        H = 400
        N = size
        SPACING = 10 #default

        #Adapting spacing with the grid size
        if N >= 6:
            SPACING = 5

        # Drawing new tile space
        pygame.draw.rect(screen, back_color_pallet['back'], pygame.Rect(screen.get_width()-115,35, 40, 45), border_radius= 5)
        pygame.draw.rect(screen, back_color_pallet[str(next_tile)+'_back'], pygame.Rect(screen.get_width()-105,45,20,28), border_radius= 6)
        pygame.draw.rect(screen, back_color_pallet[next_tile], pygame.Rect(screen.get_width()-105,43,20,28), border_radius= 6)

        # Drawing score
        text_score_surface = self.num_font_2.render('Score: ' + str(score), False, number_color_pallet['text_2'])
        pygame.draw.rect(screen, back_color_pallet['screen_back'], pygame.Rect(screen.get_width()/2-120,100, 150, 40), border_radius= 5)

        # Creating surface that it's going to receive the drawing of the grid and filling with blank
        grid_back = pygame.Surface((W,H))
        grid_back.fill(back_color_pallet['screen_back'])

        # Drawing the grid background
        pygame.draw.rect(grid_back, back_color_pallet['back'], pygame.Rect(0,0,W,H), border_radius= 10)

        # Draw the tiles spaces in the surface grid_back with an loop
        for i in range(N):
            for j in range(N):

                # This is the string of the number we want to add the tile
                number = grid[i][j]

                # Verifying the lenght of the number so we can adapt the text
                if len(str(number)) <= 2:
                    num_font = self.num_font_1
                elif len(str(number)) == 3:
                    num_font = self.num_font_2
                else:
                    num_font = self.num_font_3
                
                # Determinating the dimentions of the tiles (rect_w and rect_h) and the placing (rect_x and rect_y)
                rect_x = j * W // N + SPACING
                rect_y = i * H // N + SPACING
                rect_w = W // N - 2 * SPACING
                rect_h = H // N - 2 * SPACING

                # Drawing each rectangle that are the spaces for the tiles
                pygame.draw.rect(grid_back, back_color_pallet['back_tile'], pygame.Rect(rect_x,rect_y,rect_w,rect_h), border_radius= 5)

                # Drawing each rectangle tiles with the text
                if number == 0: # Don't need a tile
                    pass
                elif number == get_grid_tile_max(grid) and number != 3:
                    tile_back = pygame.draw.rect(grid_back, back_color_pallet[str(number)+'_back'], pygame.Rect(rect_x,rect_y,rect_w,rect_h), border_radius= 5)
                    tile = pygame.draw.rect(grid_back, back_color_pallet[number], pygame.Rect(rect_x,rect_y-rect_h*0.06,rect_w,rect_h), border_radius= 5)
                    number_surface = num_font.render(str(number), False, number_color_pallet['max_number'])
                    number_text_rect = number_surface.get_rect(center= (rect_x + rect_w/2,rect_y + rect_h/2))
                    
                    tiles_dic[i] = (tile, tile_back)

                    # Blit the number in the surface grid
                    grid_back.blit(number_surface,number_text_rect)

                else:
                    tile_back = pygame.draw.rect(grid_back, back_color_pallet[str(number)+'_back'], pygame.Rect(rect_x,rect_y,rect_w,rect_h), border_radius= 5)
                    tile = pygame.draw.rect(grid_back, back_color_pallet[number], pygame.Rect(rect_x,rect_y-rect_h*0.06,rect_w,rect_h), border_radius= 5)
                    number_surface = num_font.render(str(number), False, number_color_pallet[number])
                    number_text_rect = number_surface.get_rect(center= (rect_x + rect_w/2,rect_y + rect_h/2))
                    
                    tiles_dic[i] = (tile, tile_back)

                    # Blit the number in the surface grid
                    grid_back.blit(number_surface,number_text_rect)


        # Blit the surface grid in the screen
        screen.blit(grid_back, ((screen.get_width()-W)/2,(screen.get_height()-H)/2+30))

        # Blit the text of score in the screen
        screen.blit(text_score_surface, (screen.get_width()/2-120,100))



class Game_Over_Screen:
    def __init__(self, screen, tela):
        self.screen = screen
        self.GO_font= usual_fonts['title_game_over']
        ranking_font= usual_fonts['title_ranking']
        gui_font = usual_fonts['text_game_over_screen']
 
        # completely fill the surface object
        screen.fill(back_color_pallet['screen_back'])

        # define the RGB value for white
        white = (255, 255, 255)

        # Loading icons
        icon_menu = pygame.image.load(image_path_6)
        icon_menu = pygame.transform.scale(icon_menu, (21, 21))

        icon_exit = pygame.image.load(image_path_2)
        icon_exit = pygame.transform.scale(icon_exit, (21, 21))

        icon_save = pygame.image.load(image_path_8)
        icon_save = pygame.transform.scale(icon_save, (21, 21))


        # Creating buttons subtitles
        self.menu_text_surface = gui_font.render('Menu', False, number_color_pallet['text_1'])
        self.menu_text_rect = self.menu_text_surface.get_rect(center = (screen.get_width()/2 -50,screen.get_height()/2+155))
        self.exit_text_surface = gui_font.render('Exit game', False, number_color_pallet['text_1'])
        self.exit_text_rect = self.exit_text_surface.get_rect(center = (screen.get_width()/2 + 80,screen.get_height()/2+155))
        self.save_text_surface = gui_font.render('Save record', False, number_color_pallet['text_1'])
        self.save_text_rect = self.save_text_surface.get_rect(center= (screen.get_width()/2 + 20,screen.get_height()/2+155))
 
        # assigning values to X and Y variable
        X = 400
        Y = 600
        self.font=pygame.font.Font(None,30)
        self.gui_font = pygame.font.Font(None,25)
        # create a text surface object
        self.text = self.GO_font.render('Game Over', True, number_color_pallet['title_1'])
        self.text_ranking = ranking_font.render('Ranking: ', True, back_color_pallet[2])
        
        # create a rectangular object for the text surface object
        self.textRect = self.text.get_rect()
        self.textRect2 = self.text_ranking.get_rect()
        
        # set the position of the rectangle objects
        self.textRect.center = (X//2, Y//2-200)
        self.textRect2.center = (X//2, Y//2-60)

        #button_start = Button('', 35, 35, (210,(screen.get_height()-35)/2), 5, gui_font, back_color_pallet[2], back_color_pallet['2_back'], back_color_pallet['2_back'], icon_play)
        name = ''
        # infinite loop
        running=True
        if tela == "record":
            # creates buttons
            self.save_name_button=Button('', 35, 35, (135,(screen.get_height()-35)/2 + 160),5,  gui_font, back_color_pallet[2], back_color_pallet['2_back'], back_color_pallet['2_back'], icon_save)
            self.input_box1 = InputBox(screen.get_width()/2 -100, screen.get_height()/2 +70, 140, 32)
            
        elif tela == "game_over":
            self.start_new_game_button=Button('', 35, 35, (85,(screen.get_height()-35)/2 + 160),5,  gui_font, back_color_pallet[2], back_color_pallet['2_back'], back_color_pallet['2_back'], icon_menu)
            self.exit_button=Button('', 35, 35, (205,(screen.get_height()-35)/2 + 160),5,  gui_font, back_color_pallet[2], back_color_pallet['2_back'], back_color_pallet['2_back'], icon_exit)  
            # create a rectangular object for the text surface object
            self.textRect = self.text.get_rect()
            self.textRect2 = self.text_ranking.get_rect()
        
            # set the position of the rectangle objects
            self.textRect.center = (X//2, Y//2-200)
            self.textRect2.center = (X//2, Y//2-120)
        
    def display_rec_message(self, pos, score):
        X = 400
        Y = 600
        position = [" ", " second ", " third "]
        record_message_2 = "New"+position[pos]+"highest score!"
        record_message_3 = score+" points"
        record_message_4 = "Please, insert your name to save score"

        self.rec_message_text_2 = self.gui_font.render(record_message_2, True, number_color_pallet['title_1'])
        self.rec_messageRect_2 = self.rec_message_text_2.get_rect()
        self.rec_messageRect_2.center = (X//2-5, Y//2-40)
        self.rec_message_text_3 = self.gui_font.render(record_message_3, True, number_color_pallet['title_2'])
        self.rec_messageRect_3 = self.rec_message_text_3.get_rect()
        self.rec_messageRect_3.center = (X//2, Y//2-20)
        self.rec_message_text_4 = self.gui_font.render(record_message_4, True, number_color_pallet['title_1'])
        self.rec_messageRect_4 = self.rec_message_text_4.get_rect()
        self.rec_messageRect_4.center = (X//2, Y//2)
    
    
    def display_ranking(self):
        X = 400
        Y = 600
        d = shelve.open(record_path)
        name_list = d['name']
        score_list = d['score']
        ranking = "1º "+name_list[0]+"  "+str(score_list[0])+" Points"
        ranking_2 = "2º "+name_list[1]+"  "+str(score_list[1])+" Points"
        ranking_3 = "3º "+name_list[2]+"  "+str(score_list[2])+" Points"
        self.ranking_text = self.gui_font.render(ranking, True, number_color_pallet['title_1'])
        self.ranking_messageRect = self.ranking_text.get_rect()
        self.ranking_messageRect.center = (X//2, Y//2-20)
        self.ranking_text_2 = self.gui_font.render(ranking_2, True, number_color_pallet['title_1'])
        self.ranking_messageRect_2 = self.ranking_text.get_rect()
        self.ranking_messageRect_2.center = (X//2, Y//2)
        self.ranking_text_3 = self.gui_font.render(ranking_3, True, number_color_pallet['title_1'])
        self.ranking_messageRect_3 = self.ranking_text.get_rect()
        self.ranking_messageRect_3.center = (X//2, Y//2+20)
        

def main():

    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    # Screen dimentions
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 600

    # Fonts used
    medium_text_font = pygame.font.Font(None,20) #for initial screen
    number_font_1 = pygame.font.Font(None,30) #for small numbers
    number_font_2 = pygame.font.Font(None,25) #for medium numbers
    number_font_3 = pygame.font.Font(None,20) #for big numbers
    gui_font = pygame.font.Font(None,30)
    gui_font_mini = pygame.font.Font(None,20)

    # Set up the drawing window
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    # Set up the name of the window
    pygame.display.set_caption('Threes')

    #Set up the icon of the application
    screen_icon = pygame.image.load(image_path_7)
    pygame.display.set_icon(screen_icon)

    #Initial size grid
    size = 0

    # Showing initial screen of the game
    Initial_Screen(screen, usual_fonts['title_game'], usual_fonts['text_init_screen'])

    #Set up the images of the buttons of the initial screen
    icon_download = pygame.image.load(image_path_1)
    icon_download = pygame.transform.scale(icon_download,(24,24))
    icon_play = pygame.image.load(image_path_4)
    icon_play = pygame.transform.scale(icon_play,(22,22))
    icon_exit = pygame.image.load(image_path_2)
    icon_exit = pygame.transform.scale(icon_exit,(25,25))


    # Set up sounds
    pygame.mixer.music.load(Sounds["back_sound"])
    pygame.mixer.music.play(-1)

    #Creating the buttons objects
    button_start = Button('', 35, 35, (210,(screen.get_height()-35)/2), 5, gui_font, back_color_pallet[2], back_color_pallet['2_back'], back_color_pallet['2_back'], icon_play)
    button_end = Button('', 35, 35, (210,(screen.get_height()-35)/2 + 120), 5, gui_font, back_color_pallet[2], back_color_pallet['2_back'], back_color_pallet['2_back'], icon_exit)
    if game_saved() == True :
        button_load = Button('',35, 35, (210,(screen.get_height()-35)/2 +60), 5, gui_font, back_color_pallet[2], back_color_pallet['2_back'], back_color_pallet['2_back'], icon_download)
    elif game_saved() == False:
        button_load = Button('',35, 35, (210,(screen.get_height()-35)/2 +60), 5, gui_font, "#90A5A1","#90A5A1", "#90A5A1", icon_download)
    
    button_4 = Button('4', 25, 25, (70,(screen.get_height()-40)/2 + 60), 5, gui_font, back_color_pallet[2], back_color_pallet['2_back'], back_color_pallet['2_back'])
    button_5 = Button('5', 25, 25, (105,(screen.get_height()-40)/2 + 60), 5, gui_font, back_color_pallet[2], back_color_pallet['2_back'], back_color_pallet['2_back'])
    button_6 = Button('6', 25, 25, (70,(screen.get_height()-40)/2+ 100), 5, gui_font, back_color_pallet[2], back_color_pallet['2_back'], back_color_pallet['2_back'] )
    button_7 = Button('7', 25, 25, (105,(screen.get_height()-40)/2 + 100), 5, gui_font, back_color_pallet[2], back_color_pallet['2_back'], back_color_pallet['2_back'])

    pygame.display.flip()
    global running_game
    running_initial = True
    running_game = False
    end_game = False
    while running_initial:
        
        # Seeing the input box
        '''
        text, active, color= wait_for_type(screen, input_box, color_active, color_inactive, color, text, active, font_input)
        '''

        # Waiting for the player to click 4
        if button_4.draw(screen) == True:
            size = 4

        # Waiting for the player to click 5
        if button_5.draw(screen) == True:
            size = 5

        # Waiting for the player to click 6
        if button_6.draw(screen) == True:
            size = 6
        
        # Waiting for the player to click 6
        if button_7.draw(screen) == True:
            size = 7

        # Waiting for the player to click start
        if size not in [4,5,6,7]:
            button_start.top_color = "#90A5A1"
            button_start.bottom_color = "#90A5A1"
            button_start.cover_color = "#90A5A1"
            button_start.draw(screen)
        else:
            button_start.top_color = back_color_pallet[2]
            button_start.bottom_color = back_color_pallet['2_back']
            button_start.cover_color = back_color_pallet['2_back']
            if button_start.draw(screen) == True:
                running_game = True
                reload = False
        
        if game_saved() == True :
            if button_load.draw(screen) == True:
                running_game = True 
                reload = True
        if game_saved() == False :
            if button_load.draw(screen) == True:
                pass
        
        # Waiting for the player to click exit
        if button_end.draw(screen) == True:
            running_initial = False 


        # Did the user click the window close button?
        if wait_for_key() == 'q':
            running_initial = False

        elif running_game == True:
            # Showing the initial games
            screen.fill(back_color_pallet['screen_back'])
            mute = False
            if reload:
                grid = open_save_game()
                size = len(grid)
            else:
                grid = init_game(size)
            next_tile = get_value_new_tile()
            score = get_score(grid)
            
            #Set up the images of the buttons of the initial screen
            icon_mute = pygame.image.load(image_path_3)
            icon_restart = pygame.image.load(image_path_5)
            icon_restart = pygame.transform.scale(icon_restart, (21, 21))
            icon_exit = pygame.image.load(image_path_2)
            icon_exit = pygame.transform.scale(icon_exit, (21, 21))

            button_mute = Button('', 30, 30, (screen.get_width()/2 - 120, 40), 3, gui_font_mini, back_color_pallet['button_top'], back_color_pallet['button_bottom'], back_color_pallet['button_bottom'],icon_mute)
            button_restart = Button('', 30, 30, (screen.get_width()/2 - 60, 40), 3, gui_font_mini, back_color_pallet['button_top'], back_color_pallet['button_bottom'], back_color_pallet['button_bottom'], icon_restart)
            button_quit = Button('', 30, 30, (screen.get_width()/2, 40), 3, gui_font_mini, back_color_pallet['button_top'], back_color_pallet['button_bottom'], back_color_pallet['button_bottom'],icon_exit)
            build_game = Build_Game(number_font_1, number_font_2, number_font_3)
            build_game.draw_game(screen, grid, next_tile, score, size)
            pygame.display.flip()
            save_game(grid)
            while running_game:

                # Waiting for the player to do a move or quit
                key = wait_for_key()

                # Veryfing mute condition
                if button_mute.draw(screen) == True:
                    if mute == False:
                        mute = True
                        mute_unmute_volume("mute")
                    else:
                        mute = False
                        mute_unmute_volume("unmute")

                # Veryfing restart condition
                if button_restart.draw(screen) == True:
                    grid = init_game(size)
                    next_tile = get_value_new_tile()
                    build_game.draw_game(screen, grid, next_tile, score, size)
                    pygame.display.flip()

                # Veryfing quit condition
                if button_quit.draw(screen) == True:
                    sys.exit()
                    

                # Did the user click arrow up
                if key == 'u':
                    grid, next_tile = up(screen, grid, next_tile, score, build_game,size)
                if key == 'd':
                    grid, next_tile = down(screen, grid, next_tile, score, build_game,size)
                if key == 'l':
                    grid, next_tile = left(screen, grid, next_tile, score, build_game,size)
                if key == 'r':
                    grid, next_tile = right(screen, grid,next_tile, score, build_game,size)
                
                # Did the user click the window close button?
                if key == 'q':
                    sys.exit()
                
                pygame.display.update()
            
            record, score, pos = is_record(grid)
            if record == True:
                record_screen = Game_Over_Screen(screen, "record")
                record_screen.display_rec_message(pos, str(score))
                running_record = True
                # attaching the text to the surface object
                record_screen.screen.blit(record_screen.text, record_screen.textRect)
                record_screen.screen.blit(record_screen.save_text_surface, record_screen.save_text_rect)
                record_screen.screen.blit(record_screen.rec_message_text_2, record_screen.rec_messageRect_2)
                record_screen.screen.blit(record_screen.rec_message_text_3, record_screen.rec_messageRect_3)
                record_screen.screen.blit(record_screen.rec_message_text_4, record_screen.rec_messageRect_4)
            
                
                while running_record:
                    pygame.display.update()
                    record_screen.input_box1.update()
                    record_screen.input_box1.draw(record_screen.screen)
                    if record_screen.save_name_button.draw( record_screen.screen):
                        save_record(record_screen.input_box1.text, score, pos)
                        d = shelve.open(record_path)
                        list_name = d['name']
                        running_record = False
                        print(list_name)
                        
                    # iterate over the list of Event objects            
                        # if event object type is QUIT then quitting the game
                    for event in pygame.event.get():
                
                        # if event object type is QUIT then quitting the game
                        record_screen.input_box1.handle_event(event)
                        if event.type == pygame.QUIT:
                
                            # deactivates the pygame library
                            pygame.quit()
                            # quit the program.
                            quit()
            
            game_over_running = True
            game_over_screen = Game_Over_Screen(screen, "game_over")
            game_over_screen.display_ranking()
            # attaching the text to the surface object
            game_over_screen.screen.blit(game_over_screen.ranking_text, game_over_screen.ranking_messageRect)
            game_over_screen.screen.blit(game_over_screen.ranking_text_2, game_over_screen.ranking_messageRect_2)
            game_over_screen.screen.blit(game_over_screen.ranking_text_3, game_over_screen.ranking_messageRect_3)
            game_over_screen.screen.blit(game_over_screen.menu_text_surface, game_over_screen.menu_text_rect)
            game_over_screen.screen.blit(game_over_screen.exit_text_surface, game_over_screen.exit_text_rect)
            game_over_screen.screen.blit(game_over_screen.text, game_over_screen.textRect)
            game_over_screen.screen.blit(game_over_screen.text_ranking, game_over_screen.textRect2)
            while game_over_running:
                pygame.display.update()
                if game_over_screen.start_new_game_button.draw(game_over_screen.screen):
                    Initial_Screen(screen, usual_fonts['title_game'], usual_fonts['text_init_screen'])
                    break
                if game_over_screen.exit_button.draw(game_over_screen.screen):
                    sys.exit()
                
                # iterate over the list of Event objects
                for event in pygame.event.get():
            
                    # if event object type is QUIT then quitting the game
                    if event.type == pygame.QUIT:
            
                        # deactivates the pygame library
                        sys.exit()
                        # quit the program.
                        
        
        pygame.display.update()

    # Done! Time to quit.
    pygame.quit()


main()

