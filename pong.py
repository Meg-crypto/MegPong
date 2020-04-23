import pygame
from pygame.locals import K_UP, K_DOWN, K_w, K_s, K_v, QUIT
from random import randint

from paddle import Paddle
from ball import Ball

# Sizes
SCREEN_SIZE = [500,500]
SIDE_MARGIN = 30
PADDLE_SIZE = (15, 100)
BALL_SIZE = 10
# Colours
BACKGROUND_COLOUR = (200,0,90)
BALL_COLOUR = (255,255,255)
PADDLE_COLOUR = (255,255,255)
# Other settings
PADDLE_SPEED = 4

# Create the paddles
paddle_A = Paddle(PADDLE_COLOUR, PADDLE_SIZE)
paddle_A.rect.x = SIDE_MARGIN
paddle_A.rect.y = 20

paddle_B = Paddle(PADDLE_COLOUR, PADDLE_SIZE)
paddle_B.rect.x = SCREEN_SIZE[0] - PADDLE_SIZE[0] - SIDE_MARGIN
paddle_B.rect.y = 300

# Create the ball
ball = Ball(BALL_COLOUR, BALL_SIZE)
def reset_ball():
    ball.rect.x = SCREEN_SIZE[0]/2
    ball.rect.y = SCREEN_SIZE[1]/2
    ball.velocity = [randint(-8,8),randint(-4,4)] # TODO ony set direction, with constant speed
reset_ball()

# Add paddles and ball to list of all sprites
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddle_A)
all_sprites_list.add(paddle_B)
all_sprites_list.add(ball)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock() # The clock will be used to control how fast the screen updates


# Runthe main loop of the game until window is closed
running = True

while running:
    screen.fill(BACKGROUND_COLOUR)
    pressed_keys = pygame.key.get_pressed()

    # Move the paddles
    if pressed_keys[K_w]:
        paddle_A.up(PADDLE_SPEED)
    if pressed_keys[K_s]:
        paddle_A.down(PADDLE_SPEED)
    if pressed_keys[K_UP]:
        paddle_B.up(PADDLE_SPEED)
    if pressed_keys[K_DOWN]:
        paddle_B.down(PADDLE_SPEED)

    if pressed_keys[K_v]:
        reset_ball()

    # Move the ball
    ball.rect.x += ball.velocity[0]
    ball.rect.y += ball.velocity[1]
    # Bounce the ball
    if ball.rect.y <= 0 or ball.rect.y + (2*BALL_SIZE) >= SCREEN_SIZE[1]:
        ball.velocity[1] = -1 * ball.velocity[1]
    if ball.rect.x <= SIDE_MARGIN + PADDLE_SIZE[0] \
    or ball.rect.x >= SCREEN_SIZE[0] - PADDLE_SIZE[0] - SIDE_MARGIN - BALL_SIZE:
        ball.velocity[0] = -1 * ball.velocity[0]
    
    # Update all the sprites and draw them
    all_sprites_list.update()

    for entity in all_sprites_list:
        screen.blit(entity.image, entity.rect)
    
    pygame.display.flip()


    for event in pygame.event.get():
        # Quit if user closes the window
        if event.type == pygame.QUIT:
            running = False
            print('bye!')

    # Limit to 60 frames per second
    clock.tick(60)
