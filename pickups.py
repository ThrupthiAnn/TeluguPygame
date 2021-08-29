import pygame
from constants import *
import random
import sys
import os

class Pickup(pygame.sprite.Sprite):
	def __init__(self, settings, img):
		pygame.sprite.Sprite.__init__(self)
		self.image = img
		self.settings = settings
		self.rect = self.image.get_rect()
		self.rect.center = (settings.WIDTH / 2 + random.randint(-50,50), settings.HEIGHT / 2 + random.randint(-50,50))
		self.topspeed = 3
		self.time = 0
		self.xspeed = random.randint(-self.topspeed, self.topspeed)
		self.yspeed =  random.randint(-self.topspeed, self.topspeed)
		self.bounds = settings.movescreen

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

class Coin1(Pickup):
	def __init__(self, settings):
		img = pygame.image.load('Asset/coin1.png').convert()
		img = pygame.transform.scale(img, (30,30))
		img.set_colorkey(BLACK)
		super().__init__(settings, img)

class Coin2(Pickup):
	def __init__(self, settings):
		img = pygame.image.load('Asset/coin2.png').convert()
		img = pygame.transform.scale(img, (35,35))
		img.set_colorkey(BLACK)
		super().__init__(settings, img)

class Coin3(Pickup):
	def __init__(self, settings):
		img = pygame.image.load('Asset/coin3.png').convert()
		img = pygame.transform.scale(img, (40,40))
		img.set_colorkey(BLACK)
		super().__init__(settings, img)

class Heart(Pickup):
	def __init__(self, settings):
		img = pygame.image.load('Asset/heart.gif').convert()
		img = pygame.transform.scale(img, (50,50))
		img.set_colorkey(BLACK)
		super().__init__(settings, img)

