import pygame

BLACK = (0,0,0)

class Ball(pygame.sprite.Sprite):
    def __init__(self, colour, ball_radius):
        super().__init__()

        self.image = pygame.Surface([ball_radius*2, ball_radius*2])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.circle(self.image, colour, [ball_radius, ball_radius], ball_radius)

        self.rect = self.image.get_rect()
        