#taking references from geek for geeks on pygame and making this game
#not complete
import pygame
import time
import random


snake_speed = 10
 
win_x = 640
win_y = 400
 
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
 
pygame.init()
 
pygame.display.set_caption('Snakes Game')
game_window = pygame.display.set_mode((win_x, win_y))
 
# FPS (frames per second) controller
fps = pygame.time.Clock()

score = 0
snake_position = [120, 60]
 
snake_body = [[120, 60], [110, 60], [100, 60],[90, 60]]

fruit_position = [random.randrange(1, (win_x//10)) * 10, random.randrange(1, (win_y//10)) * 10]
 
fruit_spawn = True
 

dir = 'RIGHT'
change_to = dir


def game_over():
   
    my_font = pygame.font.SysFont('times new roman', 50)
     
    game_over_score = my_font.render(
        'Your Score was : ' + str(score), True, red)
     
    game_over_msg = game_over_score.get_rect()
    game_over_msg.midtop = (win_x/2, win_y/4)
     
    game_window.blit(game_over_score, game_over_msg)
    pygame.display.flip()
     
    time.sleep(4)
     
    pygame.quit()

    quit()

while True:
     
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    if dir == 'UP':
        snake_position[1] -= 10
    if dir == 'DOWN':
        snake_position[1] += 10
    if dir == 'LEFT':
        snake_position[0] -= 10
    if dir == 'RIGHT':
        snake_position[0] += 10

    if snake_position[0] < 0 or snake_position[0] > win_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > win_y-10:
        game_over()