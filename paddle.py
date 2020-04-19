import pygame

BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, colour, paddle_size):
        super().__init__()
        self.width, self.height = paddle_size[0], paddle_size[1]
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, colour, [0,0,self.width,self.height])
        self.rect = self.image.get_rect()

    def up(self, distance):
        self.rect.y -= distance 
        if self.rect.y < 0:
            self.rect.y = 0  

    def down(self, distance):
        self.rect.y += distance 
        if self.rect.y > 500 - self.height:
            self.rect.y = 500 - self.height          