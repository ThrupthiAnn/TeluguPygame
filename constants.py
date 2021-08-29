import pygame
import os

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHTGREY = (200,200,200)
DARKGREY = (100,100,100)
BLUEGREY = (230, 230, 255)

class Life(pygame.sprite.Sprite):

	def __init__(self, settings):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join('Asset', 'heart.gif')).convert()
		self.image = pygame.transform.scale(self.image, (50,50))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.settings = settings

	def update(self):
		pass

class Settings:

	def __init__(self):
		self.WIDTH = 500
		self.HEIGHT = 500
		self.FPS = 30
		self.SCORE = 0
		self.LIVES = 3
		self.LEVEL = 0
		self.levelincrease = 2

		self.background = WHITE
		self.fixedbackground = WHITE
		self.movebackground = LIGHTGREY
		self.scorebackground = BLUEGREY

		self.correctsound = pygame.mixer.Sound('Asset/Pickup_Coin2.wav')
		self.wrongsound = pygame.mixer.Sound('Asset/Hit_Hurt3.wav')
		self.losesound = pygame.mixer.Sound('Asset/GameOver.wav')
		self.winsound = pygame.mixer.Sound('Asset/winfretless.ogg')
		self.music = pygame.mixer.music.load('Asset/FeverDrMario.mp3')
		pygame.mixer.music.set_volume(0.4)

		fixedheight = 70
		scoreheight = 100
		moveheight = self.HEIGHT - fixedheight - scoreheight - 40

		self.fixedscreen = pygame.Rect(10,10,self.WIDTH-20, fixedheight)
		self.movescreen = pygame.Rect(10, self.fixedscreen.bottom + 10, self.WIDTH-20, moveheight)
		self.scorescreen = pygame.Rect(10, self.movescreen.bottom + 10, self.WIDTH - 20, scoreheight )

		self.letters = 5 # number of letters in the question
		self.unknowns = 1 
		self.extras = 3




		self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		pygame.display.set_caption(str(self.SCORE))
		self.clock = pygame.time.Clock()
		self.all_sprites = pygame.sprite.Group()

		# create hearts

		self.lives = []
		right = self.scorescreen.right
		for ii in range(self.LIVES):
			self.lives.append(Life(self))
			self.lives[ii].rect.center = self.scorescreen.center
			self.lives[ii].rect.right = right 
			right = self.lives[ii].rect.left - 10
			# self.all_sprites.add(self.lives[ii])
		self.drawhearts()
		pygame.mixer.music.play(loops=-1)

	def drawhearts(self):
		for ii in range(self.LIVES):
			self.screen.blit(self.lives[ii].image, self.lives[ii].rect.topleft)

	def restart(self):
		self.SCORE = 0
		self.LIVES = 3
		self.letters = 5
		self.unknowns = 1
		self.extras = 3
		self.LEVEL=0
		

	def draw_text(self, text, size, x, y, color):
		font_name = pygame.font.match_font('arial')
		font = pygame.font.Font(font_name, size)
		text_surface = font.render(text, True, color)
		text_rect = text_surface.get_rect()
		text_rect.center = (x, y)
		self.screen.blit(text_surface, text_rect)

	def winscreen(self):
		self.LEVEL +=1
		self.unknowns = min(int(self.LEVEL/self.levelincrease) + 1, 5)
		pygame.display.set_caption('You won!!')
		self.screen.fill(WHITE)
		self.draw_text('You won!!', 70,self.screen.get_rect().centerx, self.screen.get_rect().centery, GREEN)
		self.draw_text('Score = ' + str(self.SCORE), 30, self.screen.get_rect().centerx, self.screen.get_rect().centery+100, BLACK)
		self.winsound.play()
		pygame.display.flip()

	def losescreen(self):
		pygame.display.set_caption('You lost!!')
		self.screen.fill(WHITE)
		self.draw_text('You lost!!', 70,self.screen.get_rect().centerx, self.screen.get_rect().centery, RED)
		self.draw_text('Final score = ' + str(self.SCORE), 30, self.screen.get_rect().centerx, self.screen.get_rect().centery+100, BLACK)
		self.losesound.play()

		pygame.display.flip()
		self.restart()

	def draw(self):
		# Draw / render
		pygame.display.set_caption('Score = ' + str(self.SCORE) + ',Lives = ' + str(self.LIVES))
		self.screen.fill(self.background)
		pygame.draw.rect(self.screen, self.fixedbackground, self.fixedscreen)
		pygame.draw.rect(self.screen, self.movebackground, self.movescreen)
		pygame.draw.rect(self.screen, self.scorebackground, self.scorescreen)
		self.all_sprites.draw(self.screen)
		# Update
		self.all_sprites.update()
		self.drawhearts()





