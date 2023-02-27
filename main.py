import pygame, sys
from pygame.locals import QUIT
import random

SIZE = 10
WIDTH = 35
HEIGHT = 25

pygame.init()
size = (WIDTH * SIZE, HEIGHT * SIZE)
screen = pygame.display.set_mode(size)
background = (20, 20, 200)

snake = [(22, 20), (21, 20), (20, 20)]

clock = pygame.time.Clock()

def game_to_screen(x, y):
    return x * SIZE, y * SIZE

def move():
    x, y = snake[0]
    dx, dy = step
    new_x = (x + dx + WIDTH) % WIDTH
    new_y = (y + dy + HEIGHT) % HEIGHT
    snake.insert(0, (new_x, new_y))  
    global grow
    if grow == False:
        snake.pop()
    else:
        grow = False

    

def  draw():
    screen.fill(background)
    x, y = food
    (screen_x, screen_y) = game_to_screen(x, y)
    color = (255, 0, 0)
    rect = ((screen_x, screen_y), (SIZE, SIZE))
    pygame.draw.rect(screen, color, rect)
    for part in snake:
        x, y = part
        (screen_x, screen_y) = game_to_screen(x, y)
        color = (0, 200, 200)
        rect = ((screen_x, screen_y), (SIZE, SIZE))
        pygame.draw.rect(screen, color, rect)
    pygame.display.update()

def new_food():
    global food
    x = random.randrange(SIZE)
    y = random.randrange(SIZE)
    food = (x, y)

gameover = False
paused = False
step = (1, 0)
speed = 1 
grow = False
new_food()

def touch():
    global gameover
    for field in snake [1:]: 
        if field == snake [0]:
            gameover = True 
        
def eat():
    global grow
    if snake[0] == food:
        new_food()
        grow = True
        global speed
        speed = speed + 1 

pygame.display.set_caption('Snake')
while not gameover:
    if not paused:
        move()
        eat()
        touch()
        draw()
    clock.tick(7 + speed)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                step = (0, -1)
            if event.key == pygame.K_s:
                step = (0, 1)
            if event.key == pygame.K_a:
                step = (-1, 0)
            if event.key == pygame.K_d:
                step = (1, 0)
            if event.key == pygame.K_SPACE:
                paused = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                paused = False
        if event.type == QUIT:
            pygame.quit()
            sys.exit()