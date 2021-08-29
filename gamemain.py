import pygame
import random
import sys
import os
from constants import *
from letters import *
from question import *
from pickups import *



def gameloop(settings, question):
	# Game loop
	while question.WIN==False and settings.LIVES >0:
		# keep loop running at the right speed
		settings.clock.tick(settings.FPS)
		# Process input (events)
		for event in pygame.event.get():
			# check for closing window
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				# get a list of all sprites that are under the mouse cursor
				clicked_sprites = [s for s in settings.all_sprites if s.rect.collidepoint(pos)]
				# do something with the clicked sprites..
				if len(clicked_sprites)>0:
					question.clicked(clicked_sprites)
		settings.draw()
		# *after* drawing everything, flip the display
		pygame.display.flip()
	if question.WIN:
		settings.winscreen()
	else:
		settings.losescreen()
	exitloop(settings, question)

def exitloop(settings, question):
	flag = True
	while flag:
		settings.clock.tick(settings.FPS)
		for event in pygame.event.get():
			# check for closing window
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONUP:
				flag = False
				question.killall()
				
		
	


if __name__ == "__main__":
	pygame.init()
	pygame.mixer.init()
	settings = Settings()

	while True:
		question = Question(settings)
		# coin1 = Coin1(settings)
		# coin2 = Coin2(settings)
		# coin3 = Coin3(settings)
		# heart1 = Heart(settings)
		settings.all_sprites.add(coin1)
		settings.all_sprites.add(coin2)
		settings.all_sprites.add(coin3)
		settings.all_sprites.add(heart1)


		gameloop(settings, question)