import pygame
from paddle import Paddle
# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_w,
    K_s,
    KEYDOWN,
    QUIT,
)

# Sizes
SCREEN_SIZE = [500,500]
SIDE_MARGIN = 30
PADDLE_SIZE = (15, 100)

# Colours
BACKGROUND_COLOUR = (200,0,90)
BALL_COLOUR = (0,0,255)
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

# Add paddles to list of all sprites
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddle_A)
all_sprites_list.add(paddle_B)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

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

    pygame.draw.circle(screen, BALL_COLOUR, (250, 250),30 )
    
    all_sprites_list.update()
    all_sprites_list.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print('bye!')

    # --- Limit to 60 frames per second
    clock.tick(60)
    
    pygame.display.flip()
