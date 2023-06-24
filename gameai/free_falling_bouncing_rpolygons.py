#
# Move it!
#
#

import pygame
import numpy as np

def getRegularPolygon(N, radius=1):
    v = np.zeros((N,2), dtype=np.float32)
    for i in range(N):
        deg = i * 360. / N
        rad = deg * np.pi / 180.
        x = radius * np.cos(rad)
        y = radius * np.sin(rad)
        v[i, 0] = x 
        v[i, 1] = y 
    return v


# 색 정의
GREEN = (100, 200, 100)

WINDOW_WIDTH = 1800
WINDOW_HEIGHT = 1000

pygame.init()  # 1! initialize the whole pygame system!
pygame.display.set_caption("Mouse")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()


class Polygon:
    def __init__(self, nvertices):
        self.color = np.random.randint(0, 256, size=3)
        self.radius = 35
        self.line_width = np.random.choice([0, 2, 4])
        # self.nvertices = np.random.randint(3, 10)
        self.polygon = getRegularPolygon(nvertices, radius=self.radius)

        xinit = WINDOW_WIDTH / 2. # np.random.uniform(0, WINDOW_WIDTH) # uniform probability distribution
        yinit = 100. # np.random.uniform(0, WINDOW_HEIGHT/3) 
        vx_init = np.random.uniform(4., 8.) # uniform probability distribution
        if np.random.uniform(0,1) < 0.5:
            vx_init *= -1 
        vy_init = 0 #np.random.uniform(10, 20)

        self.txy = np.array([xinit, yinit]) # translation of the polygon
        self.vxy = np.array([vx_init, vy_init])
        self.axy = np.array([0, .421])
        
    def update(self,):
        self.vxy += self.axy 
        self.txy += self.vxy  # [tx, ty] is the ceter location of the polgyon
        self.q = self.polygon + self.txy  # current position
        
        # if txy[1] - radius >= WINDOW_HEIGHT: # the center is now outside the screen
            #  txy[1] = 0  # circulating
        if self.txy[1] + self.radius >= WINDOW_HEIGHT: # object bottom touched the screen height
            self.vxy[1] *= -1.  # reverse the moving direction
            # self.txy[1] = WINDOW_HEIGHT - self.radius
            # sound.play()
            delta = self.txy[1] + self.radius - WINDOW_HEIGHT # overshoot
            self.txy[1] = self.txy[1] - delta
            
        if self.txy[0] + self.radius >= WINDOW_WIDTH:
            self.vxy[0] *= -1.
            self.txy[0] = WINDOW_WIDTH - self.radius
        
        if self.txy[0] - self.radius < 0:
            self.vxy[0] *= -1.
            self.txy[0] = self.radius

        
        # if self.txy[1] - self.radius < 0:
        #     self.vxy[1] *= -1.
        #     self.txy[1] = self.radius

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.q, width=self.line_width)
#


polygon1 = Polygon(nvertices=3)
polygon2 = Polygon(nvertices=5)

polygon_list = []
for i in range(100):
    p = Polygon(nvertices=np.random.randint(3, 15))
    polygon_list.append(p)
    

done = False
f = 0
while not done:
    f += 1
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse Button Pressed!")
        #
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
    #
    # game state handling/processing
    
    for p in polygon_list:
        p.update()
    
    # draw!
    screen.fill( ( 100, 200, 100)) # 1
    
    for p in polygon_list:
        p.draw(screen)

    # update screen
    pygame.display.flip()
    clock.tick(60)

# 게임 종료
pygame.quit()