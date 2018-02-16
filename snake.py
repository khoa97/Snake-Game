
import pygame

import sys
import random


white = (255,255,255)
bg = (51,51,51)
speed = 10
food_color = (247,77,77)

clock = pygame.time.Clock()
class Snake():
	xcord = 100
	ycord = 100
	def __init__(self, screen):

		self.screen = screen
		self.color = white
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False


	def draw_rect(self):
		pygame.draw.rect(self.screen, self.color,
			pygame.Rect(self.xcord, self.ycord, 10, 10))

	def update(self):

		if self.moving_right:
			Snake.xcord+=speed
		if self.moving_left:
			Snake.xcord-=speed
		if self.moving_up:
			Snake.ycord-=speed
		if self.moving_down:
			Snake.ycord+=speed
		if (Snake.xcord<-10 or Snake.xcord>600 or
		   Snake.ycord<-10 or Snake.ycord>600):
			sys.exit()

class Food():


	def __init__(self, screen ):
		self.screen = screen
		self.color = food_color
		self.xcord = random.randrange(0,590,10)
		self.ycord = random.randrange(0,590,10)

	def draw_food(self):

		pygame.draw.rect(self.screen, self.color,
			pygame.Rect(self.xcord,self.ycord, 10, 10))
def add_tail(snakelist,screen):
	for i in snakelist:
		 pygame.draw.rect(screen, white,
	 		pygame.Rect(i[0],i[1],10, 10))


pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake by Khoa')
snake = Snake(screen)
food = Food(screen)
snakelist = []
count = 1

while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				snake.moving_right = False
				snake.moving_up = False
				snake.moving_left = False
				snake.moving_down = True

			if event.key == pygame.K_RIGHT:
				snake.moving_right = True
				snake.moving_up = False
				snake.moving_left = False
				snake.moving_down = False

			if event.key == pygame.K_LEFT:
				snake.moving_right = False
				snake.moving_up = False
				snake.moving_left = True
				snake.moving_down = False

			if event.key == pygame.K_UP:
				snake.moving_right = False
				snake.moving_up = True
				snake.moving_left = False
				snake.moving_down = False
	head = []
	head.append(snake.xcord)
	head.append(snake.ycord)
	snakelist.append(head)



	screen.fill(bg)
	# add tails
	if len(snakelist)>count:
		del(snakelist[0])
	add_tail(snakelist, screen)

	#collision detect
	for i in range(len(snakelist)-1):
		if [snake.xcord, snake.ycord] == snakelist[i]:
			sys.exit()

	snake.draw_rect()
	snake.update()

	#check if food is eaten
	if (food.xcord == Snake.xcord and
		    food.ycord == Snake.ycord):
			food = Food(screen)
			count+=1
	food.draw_food()
	pygame.display.flip()

	clock.tick(60)
