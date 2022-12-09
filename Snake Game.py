import pygame
import random
from pygame import mixer

pygame.init()

# Background music.
mixer.music.load('Suffer With Me.mp3')
mixer.music.play(-1)

# Colors.
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

screen = pygame.display.set_mode((800, 650))

# Snake parameters.
snake_x = 400
snake_y = 200
snake_size = 15

# Snake movements.
velocity_x = 0
velocity_y = 0

def snake_func(surface, color, snake_body, snake_wow):
    for x, y in snake_body:
        pygame.draw.rect(surface, color, [x, y, snake_wow, snake_wow])

# Other snake parameters.
snake_list = []
snake_length = 1

# Food parameters.
food_x = random.randint(50, 650)
food_y = random.randint(50, 550)
food_radius = 5

# Score variable and its parameters.
score = 0
score_font = pygame.font.Font('consolab.ttf', 35)
score_x = 10
score_y = 10

def score_func():
    score_text = score_font.render("SCORE: {}".format(score), True,
                                   white)
    screen.blit(score_text, (score_x, score_y))
    
# Game over parameters.
game_over_font = pygame.font.Font('consolab.ttf', 50)
game_over_x = 270
game_over_y = 290

def game_over_func():
    global snake_y, snake_size, food_y, score_y
    snake_y, snake_size, food_y, score_y = 900, 0, 999999, 900
    game_over_text = game_over_font.render("Game Over!", True, white)
    display_score = game_over_font.render("Your score is: {}".
                                          format(score), True,
                                          white)
    screen.blit(game_over_text, (game_over_x, game_over_y))
    screen.blit(display_score, (game_over_x-90,
                                                    game_over_y+50))

while True:
    screen.fill(black)
    
    head = []
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if velocity_x != 0.6:
                    velocity_y = 0
                    velocity_x = -0.6
            elif event.key == pygame.K_RIGHT:
                if velocity_x != -0.6:
                    velocity_y = 0
                    velocity_x = 0.6
            elif event.key == pygame.K_UP:
                if velocity_y != 0.6:
                    velocity_x = 0
                    velocity_y = -0.6
            elif event.key == pygame.K_DOWN:
                if velocity_y != -0.6:
                    velocity_x = 0
                    velocity_y = 0.6
                
    snake_x += velocity_x
    snake_y += velocity_y
    
    # If the snake collides with the food.
    if abs(snake_x-food_x) < 12 and abs(snake_y-food_y) < 12:
        food_x = random.randint(50, 650)
        food_y = random.randint(50, 550)
        snake_length += 20
        score += 1
    
    # So that python knows that the head is also the part of the
    # snake's body.
    head.append(snake_x)
    head.append(snake_y)
    snake_list.append(head)
    
    # Otherwise the snake will keep increasing its length, without
    # even eating the food.
    if len(snake_list) > snake_length:
        del snake_list[0]
        
    # If snake collides with the horizontal boundaries of our
    # pygame screen, then the game is over.
    if snake_x <= 0 or snake_x >= 800:
        game_over_func()

    # If snake collides with the vertical boundaries of our
    # pygame screen, then the game is over.
    elif snake_y <= 0 or snake_y >= 650:
        game_over_func()
    
    # If snake collides with its own body, then game is over.
    for body in snake_list[:-1]:
        if body == head:
            game_over_func()
    
    # Creating the snake.
    snake_func(screen, green, snake_list, snake_size)
    
    # Creating the food.
    pygame.draw.circle(screen, red, [food_x, food_y], food_radius)
    
    # Displaying the score on the screen.
    score_func()
    
    pygame.display.update()
