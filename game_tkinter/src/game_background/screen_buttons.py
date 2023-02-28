import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory))


import pygame
import button_class as button

def screen_buttons():
    
	""" Input: This input has no input.
		Output: This function has as an output the selected button. Be aware the output is a string!"""
    	
	#create display window
	SCREEN_HEIGHT = 500
	SCREEN_WIDTH = 1200

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Button Demo')

	#load button images
	start_img = pygame.image.load('threes\src\icons\start_btn.png').convert_alpha()
	exit_img = pygame.image.load('threes\src\icons\exit_btn.png').convert_alpha()
	help_button = pygame.image.load('threes\src\icons\help_btn.png').convert_alpha()
	restart_button = pygame.image.load('threes\src\icons\Restart_btn.png').convert_alpha()

	#create button instances
	start_button = button.Button(100, 200, start_img, 0.8)
	exit_button = button.Button(350, 200, exit_img, 0.8)
	help_button = button.Button(570, 200, help_button, 1.5)
	restart_button = button.Button(900, 200, restart_button, 1.2)

	#Game loop
	run = True
	output = None

	while run:

		screen.fill((202, 228, 241)) # <-- Background color

		# Verify please. Maybe I don't need to have 4 if statements but just one and use elif. #todo
		if start_button.draw(screen):
			output = 'START'
			# print('START')
			run = False
		
		if exit_button.draw(screen):
			output = 'EXIT'
			# print('EXIT')
			run = False
		elif help_button.draw(screen):
			output = 'HELP'
			#print('HELP')
			run = False
		
		elif restart_button.draw(screen):
    		 print('Hello')
			# For some reason I can not implement the following two comments...
			# output = 'RESTART'
			#run = False

		# The above if statements are responsible for giving us an output. When the user clicks on a button the output
		# takes as a value the string of the button and the run variable becomes False in order to be able to finish the while loop.
		# BUT for some reason in the restart button I can neither set an output nor a run variable!

		#Event handler is looking for event
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				run = False

		pygame.display.update()
	
	pygame.quit()
	
	return output

# print(screen_buttons())
