from os import kill
from constants import *
from letters import *

def getQuestion(letters, unknowns):
	starting = random.randint(0, 51-letters)
	questions = list(range(letters))
	random.shuffle(questions)
	questions = questions[:unknowns]
	questions.sort()
	indices = list(range(starting, starting+letters))
	return indices, questions

class Question:
	def __init__( self, settings):
		self.indices, self.questions = getQuestion(settings.letters, settings.unknowns)
			# get a new question
		self.fixedletters = []
		self.settings = settings
		self.WIN = False

		# create fixed letter sprites and arrange them
		xpos = 50
		for ii in range(len(self.indices)):
			self.fixedletters.append(Fixed(self.indices[ii], (xpos, 50)))
			xpos = xpos + self.fixedletters[ii].rect.width + 20
			settings.all_sprites.add(self.fixedletters[ii])
		for ii in self.questions:
			self.fixedletters[ii].state=2
		self.fixedletters[self.questions[0]].state = 1
		self.nextanswer = 0

		# determine the moving letters
		self.movers = []
		avail = list(set(range(52)) - set(self.indices))
		random.shuffle(avail)
		for ii in range(settings.extras):
			self.movers.append(avail[ii])
		for ii in self.questions:
			self.movers.append(self.indices[ii])

		# create sprites for moving letters
		self.movingletters = []
		for ii in range(len(self.movers)):
			self.movingletters.append(Mover(self.movers[ii], settings))
			settings.all_sprites.add(self.movingletters[ii])

	def killall(self):
		for ii in self.movingletters:
			ii.kill()
		for ii in self.fixedletters:
			ii.kill()

	def success(self):
		self.settings.SCORE += 1
		self.settings.correctsound.play()
		self.fixedletters[self.questions[self.nextanswer]].state = 3
		self.fixedletters[self.questions[self.nextanswer]].update()
		if self.nextanswer + 1 >= len(self.questions):
			self.win()
		else:
			self.nextanswer = self.nextanswer + 1
			self.fixedletters[self.questions[self.nextanswer]].state = 1
			self.fixedletters[self.questions[self.nextanswer]].update()


	def isanswer(self, index):
		for ii in self.questions:
			if index == self.fixedletters[ii].index:
				return True
		return False

	def win(self):
		self.settings.SCORE += 100
		self.WIN = True
		pygame.display.set_caption('WIN!!')

	def failure(self):
		self.settings.wrongsound.play()
		self.settings.LIVES -= 1

	def clicked(self, clickedlist):
		killlist = []
		for ii in clickedlist:
			if(type(ii)) == Mover:
				if ii.index == self.indices[self.questions[self.nextanswer]]:
					self.success()
					ii.kill()
				else:
					self.failure()
					if not self.isanswer(ii.index):
						ii.kill()
