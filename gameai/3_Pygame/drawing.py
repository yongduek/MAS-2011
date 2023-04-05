import pygame
import numpy as np 

# 게임 윈도우 크기
WINDOW_WIDTH = 2600
WINDOW_HEIGHT = 1700

# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("Drawing")

# 윈도우 생성
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()


class Box:
    def __init__(self, x, y, vx=-5, vy=7, color=(128,128,128), w=45, h=30):
        self.x = x 
        self.y = y
        self.w = w 
        self.h = h 
        self.vx = vx 
        self.vy = vy
        self.color = color
        
    def update(self,):
        self.x += self.vx  # position update
        self.y += self.vy 
        
        # boundary check
        # all about x coord.
        if self.x + self.w >= WINDOW_WIDTH: # box was moving to the right
            self.x = WINDOW_WIDTH - self.w  # corrected locaton 
            self.vx *= -1 # invert the direction of motion
            sound.play()
            
        if self.x < 0:  # the box moved out to the left
            self.x = 0
            self.vx *= -1 
        
        # about y coord
        if self.y + self.h >= WINDOW_HEIGHT:
            self.vy *= -1
            self.y = WINDOW_HEIGHT - self.h
        if self.y < 0:
            self.y = 0
            self.vy *= -1  
    # end of update()
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.w, self.h])

class Circle:
    def __init__(self):
        pass 
    def update(self,):
        pass 
#

box1 = Box(10, 20, w=70, h=20, vx=7, vy=1, color=(255, 0,0)) 
box2 = Box(10, 20, w=20, h=70, vx=1, vy=8, color=(0,255,0)) 

nboxes = 100
boxlist = []
for i in range(nboxes):
    x = np.random.randint(0, 200)
    y = np.random.randint(0, 200)
    color = np.random.randint(0, 256, size=3)
    vx = np.random.uniform(-10., 10.)
    vy = np.random.uniform(-10., 10.)
    print(i, "color = ", color, vx)
    b = Box(x, y, color=color, vx=vx, vy=vy)  #, w, h, vx, vy, color)
    boxlist.append(b)
    
# 게임 종료 전까지 반복
done = False

# 게임 반복 구간
while not done:
    # 이벤트 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # 게임 로직 구간

    # 윈도우 화면 채우기
    screen.fill(WHITE)

    box1.update() 
    box2.update()
        
    box1.draw(screen)
    box2.draw(screen)
    
    for b in boxlist:
        b.update()
        b.draw(screen)
    
    # 화면 업데이트
    pygame.display.flip()

    # 초당 60 프레임으로 업데이트
    clock.tick(60)

# 게임 종료
pygame.quit()