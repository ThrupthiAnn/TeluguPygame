import pygame
import random
import sys
import os
from constants import *

def getLetter(index):
	assert index>=0 and index<=51, 'Letter index out of range. '
	img = pygame.image.load(os.path.join('Asset/letters', 'letters_' + str(index) + '.png')).convert()
	img.set_colorkey(WHITE)
	return img

class Fixed(pygame.sprite.Sprite):
	def __init__(self, index, pos):
		pygame.sprite.Sprite.__init__(self)
		self.img = getLetter(index)
		self.image = self.img
		self.rect = self.img.get_rect()
		self.rect.center = pos
		self.state = 0
		self.index = index

	def update(self):
		if self.state==1:
			self.image = pygame.Surface((self.rect.width, self.rect.height))
			self.image.fill(BLUE)
		elif self.state==2:
			self.image = pygame.Surface((self.rect.width, self.rect.height))
			self.image.fill(DARKGREY)
		else:
			self.image = self.img
		
	def clicked(self):
		pass

class Mover(pygame.sprite.Sprite):
	def __init__(self, index, settings):
		pygame.sprite.Sprite.__init__(self)
		self.image = getLetter(index)
		self.settings = settings
		self.rect = self.image.get_rect()
		self.rect.center = (settings.WIDTH / 2 + random.randint(-50,50), settings.HEIGHT / 2 + random.randint(-50,50))
		self.topspeed = 3
		self.time = 0
		self.xspeed = random.randint(-self.topspeed, self.topspeed)
		self.yspeed =  random.randint(-self.topspeed, self.topspeed)
		self.bounds = settings.movescreen
		self.index = index
		self.ANSWER = 1

	def collision(self):
		if self.rect.left<=self.bounds.left  or self.rect.right >=self.bounds.right:
			self.xspeed *=-1 
		if self.rect.top<=self.bounds.top or self.rect.bottom>=self.bounds.bottom:
			self.yspeed *=-1 

	def update(self):
		self.time +=1
		if self.time%500 == 0:
			if self.xspeed >=0: self.xspeed += 1
			else: self.xspeed -=1
			if self.yspeed >=0: self.yspeed += 1
			else: self.yspeed -= 1
			self.time = 0
		self.collision()
		self.rect.x +=int(self.xspeed)
		self.rect.y +=self.yspeed
		if self.rect.right > self.settings.WIDTH:
			self.rect.left = 0

