# KidsCanCode - Game Development with Pygame video series
# Shmup game - part 1
# Video link: https://www.youtube.com/watch?v=nGufy7weyGY
# Player sprite and movement
import pygame
import numpy as np 

WIDTH = 480
HEIGHT = 600
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# initialize pygame and create window
pygame.init() 
pygame.mixer.init() #
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("서용덕")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # super().__init__()
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        # print(keystate)
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

import imageio 
im_met = imageio.imread('img/meteorBrown_big1.png')
print('im_meteor:', im_met.shape)

npim = np.ones((320, 200, 3), dtype=np.uint8) * 255
npim_surface = pygame.surfarray.make_surface(npim)

# Game loop
running = True
while running:
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill((100, 100, 100))
    
    rx = np.random.randint(0, 320)
    ry = np.random.randint(0, 200)
    npim[rx, ry,:] = np.random.randint(0, 256, size=3)
    npim_surface = pygame.surfarray.make_surface(npim)
    rect = screen.blit(npim_surface, (30, 10))
    # print(rect)

    surf = pygame.surfarray.make_surface(im_met[:,:,:3])
    screen.blit(surf, (30, 250))
    
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display

    pygame.display.flip()
    # keep loop running at the right speed
    clock.tick(FPS)

pygame.quit()
