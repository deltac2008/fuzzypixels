#!/usr/bin/env python

# PiPong - A remake of the classic Pong game using PyGame.
# code take from that written by Liam Fraser - 28/07/2012 for the Linux User & Developer magazine.

import pygame   #provides what we need to make a game
import sys      # gives us the sys.exit to close program
import random   # can generate random positions for the ball

from pygame.locals import *
from pygame import *

# our main game class
class PiPong:
	def __init__(self):

		# make the display size a member of the class
		self.displaySize = (640,480)
        
        # initialise pygame
		pygame.init()
        
		# create a clock to control game speed etc.
		self.clock = pygame.time.Clock()
        
		# set window title display window etc
		display.set_caption("PiPong")
		self.display = display.set_mode(self.displaySize)
		self.background = Background(self.displaySize)
        
		# create two bats, ball then add to sprite group
		self.player1Bat = Bat(self.displaySize, "player1")
		self.player2Bat = Bat(self.displaySize, "player2")
		self.ball = Ball(self.displaySize)
		self.sprites = sprite.Group(self.player1Bat, self.player2Bat, self.ball)
        
	def run(self):
		# the main game loop
		while True:
			# this code runs every time a frame is drawn
			
			# handle the events
			self.handleEvents()
            
			# draw the background
			self.background.draw(self.display)
            
			if self.menu.draw.active:
				# draw our menu and handle key 1 and 2
				self.menu.draw(self.display)
				self.menu.handleEvents()
			else:
				# handle events
				self.handleEvents()
            
			# update and draw the sprites
			self.sprites.update()
			self.sprites.draw(self.display)
            
			# check for bat collisions
			self.ball.batCollisionTest(self.player1Bat)
			self.ball.batCollisionTest(self.player2Bat)
            
			# update the display to the screen
			display.update()
            
			# limit the game to 30 fps
			self.clock.tick(30)
            
	def handleEvents(self):
		
		# handle events
		
		# quit event
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
                
			if event.type == KEYDOWN:
				# find which key was pressed
				if event.key == K_s:
					self.player1Bat.startMove("down")
				elif event.key == K_w:
					self.player1Bat.startMove("up")
				elif event.key == K_DOWN:
					self.player2Bat.startMove("down")
				elif event.key == K_UP:
					self.player2Bat.startMove("up")
                    
			if event.type == KEYUP:
				if event.key == K_s or event.key == K_w:
					self.player1Bat.stopMove()
				elif event.key == K_DOWN or event.key == K_UP:
					self.player2Bat.stopMove()
                    
# background class
class Background:
	def __init__(self, displaySize):
		
		# set image to a new surface
		self.image = Surface(displaySize)
        
		# fill image with green colour (as RGB)
		self.image.fill((27, 210, 57))
        
		# get width proportionate to display size
		lineWidth = displaySize[0] / 80
        
		# create a rectangle to make white line
		lineRect = Rect(0, 0, lineWidth, displaySize[1])
		lineRect.centerx = displaySize[0] / 2
		draw.rect(self.image, (255, 255, 255), lineRect)
        
	def draw(self, display):
		
		# draw the background to the display that has been passed in
		display.blit(self.image, (0, 0))
        
# bat class
class Bat(sprite.Sprite):
	
	def __init__(self, displaySize, player):
		
		# init the sprite base class
		super(Bat, self).__init__()
        
		# make a player variable
		self.player = player
		
		# get width and height value proport to the display size
		width = displaySize[0] / 80
		height = displaySize[1] / 6
		
		# create image for sprite using the above
		self.image = Surface((width, height))
		
		# fill image white
		self.image.fill((255, 255, 255))
		
		# create the sprites rect from image
		self.rect = self.image.get_rect()
		
		# set the rect's location depending on player
		if player == "player1":
			# left side
			self.rect.centerx = displaySize[0] / 20
		elif player == "player2":
			# right side
			self.rect.centerx = displaySize[0] - displaySize[0] / 20


		# centre rect vertically
		self.rect.centery = displaySize[1] / 2
        
		# set direction and moving vars
		self.moving = False
		self.direction = "none"
		self.speed = 13
		
	def startMove(self, direction):
		
		# set moving flag to true
		self.direction = direction
		self.moving = True
        
	def update(self):
		
		if self.moving:
			# move the bat up or down if moving
			if self.direction == "up":
				self.rect.centery -= self.speed
			elif self.direction == "down":
				self.rect.centery += self.speed
	
	def stopMove(self):
		
		self.moving = False


# class for ball
class Ball(sprite.Sprite):

	def __init__(self, displaySize):
    
		# init base class
		super(Ball, self).__init__()
		
		# get display size for working out collisions later
        self.displaySize = displaySize
        
        # get width and height vals
        width = displaySize[0] / 30
        height = displaySize[1] / 30
        
        # create an image for the sprite
        self.image = Surface((width, height))
        
        # fill image white
        self.image.fill((27, 224, 198))
        
        # create the sprites rect from image
        self.rect = self.image.get_rect()
        
        # work out the speed
        self.speed = displaySize[0] / 110
        
        # reset the ball
        self.reset()


	def reset(self):
		
		# start the ball directly in centre of screen
		self.rect.centerx = self.displaySize[0] / 2
		self.rect.centery = self.displaySize[1] / 2
		
		# start the ball moving to left or right at vector(x,y)
		if random.randrange(1,3) == 1:
			# move left
			self.vector = (-1, 0)
		else:
			# move to the right
			self.vector = (1, 0)


	def update(self):
		
		# check if ball hit a wall
		if self.rect.midtop[1] <= 0:
			# hit top
			self.reflectVector()
		elif self.rect.midleft[0] <= 0:
			# hit left - todo: inc player2's score
			self.reset()
		elif self.rect.midright[0] >= self.displaySize[0]:
			# hit right - todo: inc player1's score
			self.reset()
		elif self.rect.midbottom[1] >= self.displaySize[1]:
			# hit bottom
			self.reflectVector()
		
		# move in direction of vector
		self.rect.centerx += (self.vector[0] * self.speed)
		self.rect.centery += (self.vector[1] * self.speed)
	
	
	def reflectVector(self):
		
		# get the current angle of ball and reflect it
		deltaX = self.vector[0]
		deltaY = - self.vector[1]
		self.vector = (deltaX, deltaY)
	
	def batCollisionTest(self, bat):
		
		# check if the ball has hit a bat
		if Rect.colliderect(bat.rect, self.rect):
			
			# work out the difference between start and end points
			deltaX = self.rect.centerx - bat.rect.centerx
			deltaY = self.rect.centery - bat.rect.centery
			
			# make the values smaller so it's not too fast
			deltaX = deltaX / 12
			deltaY = deltaY / 12
			
			# set the balls new direction
			self.vector = (deltaX, deltaY)


# class for the main menu
class Menu():
	
	def __init__(self, displaySize):
		# should we be drawing  menu/
		self.active = True
		# create the font we'll use
		self.font = font.Font(None, 30)
		# create the text surface
		self.text = self.font.render("Press 1 for CPU Opponent or 2 for two human players", True,(255,0,0))
		# get the text rectangle and center it
		self.textRect = self.text.get_rect()
		self.textRect.centerx = displaySize[0] / 2
		self.textRect.centery = displaySize[1] / 2
		
		def draw(self, display):
			# Draws our menu to the screen
			display.blit(self.text, self, textRect)
		
		def handleEvent(self):
			# handle events, starting with the quit event for event in pygame
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			
			if event.type == KEYDOWN:
				if event.key == K_1:
					# disable the menu
					game.changeBat("cpu")
					self.active = False
				elif event.key == K_2:
					game.changeBat("human")
					self.active = False


# The AI bat
class AIBat(Bat):
	def __init__(self, displaySize, player):
		# initialize the bat class
		super(AIBat, self).__init__(dispaySize, player)		
		# make our bat slower so we can't always win
		self.speed = 9
	
	
	def update(self):
		# move ourselves so we are on line with the ball
		if game.ball.rect.centrey < self.rect.centery:
			self.startMove("up")
		elif game.ball.rect.centery > self.rect.centery:
			self.startMove("down")
		else:
			self.stopMove()
		# call the bat class update method
		super(AIBat, self).update()
	
	
	def changeBat(self, batType):
		# change the player2 bat type
		self.sprites.remove(self.player2Bat)
		if batType == "cpu":
			self.player2Bat = AIBat(self.displaySize, "player2")
		elif batType == "human":
			self.player2Bat = Bat(self.displaySize, "player2")
		self.sprites.add(self.player2Bat)


if __name__ == '__main__':
	game = PiPong()
	game.run()
    