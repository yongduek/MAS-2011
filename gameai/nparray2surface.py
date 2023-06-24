#
#

import pygame
import numpy as np
import imageio 


pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 1000

# 색 정의
GREEN = (100, 200, 100)

pygame.init()  # 1! initialize the whole pygame system!
pygame.display.set_caption("Mouse")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

img15 = imageio.imread("image-15.png")
# img15 = img15.transpose((1,0,2))      #
img = img15.copy()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse Button Pressed!")
        #
    # screen.fill(GREEN)
    for _ in range(1000):
        r, c = np.random.randint(0,img.shape[0]), np.random.randint(0,img.shape[1])
        img[r, c] = 255 - img[r, c]
        
    imgswap = img.swapaxes(0, 1)
    img_surf = pygame.surfarray.make_surface(imgswap)
    screen.blit(img_surf, (0,0))
    
    # update screen
    pygame.display.flip()
    clock.tick(60)

# 게임 종료
pygame.quit()