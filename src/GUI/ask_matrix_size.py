import pygame, sys
from constants import back_color_pallet

class Button:    
    def __init__(self,text,width,height,pos,elevation, top_color, bot_color, cover_color):
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

        # bottom rectangle 
        self.bottom_rect = pygame.Rect(pos,(width,height))
        self.bottom_color = bot_color
        #text
        self.text = text
        self.text_surf = gui_font.render(text,True,'#FFFFFF') 
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def change_text(self, newtext):
        self.text_surf = gui_font.render(newtext, True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center) 
    def draw(self, gui_font, screen):
        # elevation logic 
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center    
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation 
        pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
        pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
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
        	self.top_color = back_color_pallet[2]
 
# initiate pygame
pygame.init()
matrix_size = 0
gui_font = pygame.font.Font(None,30)
 
# define the RGB value for white
white = (255, 255, 255)
 
# assigning values to X and Y variable
X = 400
Y = 600
 
# create the display surface object
display_surface = pygame.display.set_mode((X, Y))
 
# set the pygame window name
pygame.display.set_caption('Game Over')
 
# create a font object.
GO_font=pygame.font.Font(None,60)
ranking_font=pygame.font.Font(None,40)
font=pygame.font.Font(None,30)
 
# create a text surface object
text = GO_font.render('Game Over', True, white, back_color_pallet[1])
text_ranking = ranking_font.render('Ranking: ', True, back_color_pallet[2], back_color_pallet[1])
 
# create a rectangular object for the text surface object
textRect = text.get_rect()
textRect2 = text_ranking.get_rect()
 
# set the position of the rectangle objects
textRect.center = (X//2, Y//2-200)
textRect2.center = (X//2, Y//2-150)

# creates buttons  self,text,width,height,pos,elevation, top_color, bot_color, cover_color
start_new_game_button=Button("Start game",200,40,(X//2-100, Y//2+50),5, back_color_pallet[2],back_color_pallet[1] ,(255, 190, 11))
exit_button=Button('Exit Game',200,40,(X//2-100, Y//2+200),5, back_color_pallet[2],back_color_pallet[1] ,(255, 190, 11))
size_button_4=Button("4",40,40,(X//2-150, Y//2+10),5, back_color_pallet[2],back_color_pallet[1] ,(255, 190, 11))
size_button_5=Button("5",40,40,(X//2-150, Y//2+60),5, back_color_pallet[2],back_color_pallet[1] ,(255, 190, 11))
size_button_6=Button("6",40,40,(X//2-150, Y//2+110),5, back_color_pallet[2],back_color_pallet[1] ,(255, 190, 11))
size_button_7=Button("7",40,40,(X//2-150, Y//2+160),5, back_color_pallet[2],back_color_pallet[1] ,(255, 190, 11))


display_surface.fill(back_color_pallet[1])
# infinite loop
running=True
while running:
    if start_new_game_button.draw(font,display_surface):
        if matrix_size != 0:
            print("Start game " + str(matrix_size))

    if exit_button.draw(font,display_surface):
        print("Exit Game")
        running=not running

    if size_button_4.draw(font,display_surface):
        matrix_size = 4
        print(matrix_size)

    if size_button_5.draw(font,display_surface):
        matrix_size = 5
        print(matrix_size)
    
    if size_button_6.draw(font,display_surface):
        matrix_size = 6
        print(matrix_size)

    if size_button_7.draw(font,display_surface):
        matrix_size = 7
        print(matrix_size)

    pygame.display.update()
 
    # completely fill the surface object

    # attaching the text to the surface object
    display_surface.blit(text, textRect)
    display_surface.blit(text_ranking, textRect2)
 
    # iterate over the list of Event objects
    for event in pygame.event.get():
 
        # if event object type is QUIT then quitting the game
        if event.type == pygame.QUIT:
 
            # deactivates the pygame library
            pygame.quit()
            # quit the program.
            quit()
 
        # Draws the surface object to the screen.
        pygame.display.update()
