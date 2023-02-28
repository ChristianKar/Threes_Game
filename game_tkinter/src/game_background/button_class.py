import pygame

#We're creating a button class!
class Button():
    
	# Definition of the init method!
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position --> I need this to show where is the mouse of my computer!
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions --> Is the mouse over the button? That's what this function is doing!
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True # Here I can only do one click! (That's why later, I set a new if statement!)
				action = True
			#print("I'm over the button")

		if pygame.mouse.get_pressed()[0] == 0: # this is an additional statement in order to be able to click the same button many times.
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action