import pygame
import numpy as np 

# 게임 윈도우 크기
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800

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

def getRegularPolygon(N, radius):
    verts = np.empty(shape=(N, 2), dtype=np.float64)
    delta_radian = np.pi * 2 / N 
    for i in range(N):
        angle = delta_radian * i
        x = np.cos(angle) * radius
        y = np.sin(angle) * radius
        verts[i] = [x, y]
    return verts 
#
class Polygon:
    def __init__(self, nvertices = 3, x=0, y=0, vx=-5, vy=7, color=(128,128,128), radius=50):
        self.nvertices = nvertices # must be >= 3
        self.radius = radius
        self.vertices = getRegularPolygon(nvertices, radius)
        self.x = x  # center of location
        self.y = y
        self.vx = vx
        self.vy = vy
        self.angle = 0 # direction
        self.vangle = 0    # angular velocity
        self.color = color
        self.current = None
        self.life = np.random.randint(300, 3000)
        
    def update(self,):
        self.life -= 1 
        
        self.x += self.vx  # position update
        self.y += self.vy 
        
        # # boundary check
        # # all about x coord.
        if self.x + self.radius >= WINDOW_WIDTH: # box was moving to the right
            self.x = WINDOW_WIDTH - self.radius  # corrected locaton 
            self.vx *= -1 # invert the direction of motion
            
        if self.x - self.radius < 0:  # the box moved out to the left
            self.x = self.radius
            self.vx *= -1
        
        # about y coord
        if self.y + self.radius >= WINDOW_HEIGHT:
            self.vy *= -1
            self.y = WINDOW_HEIGHT - self.radius
        if self.y - self.radius < 0:
            self.y = self.radius
            self.vy *= -1
            
        self.current = self.vertices + [self.x, self.y]
        # print("x,y: ", self.x, self.y, self.vx, self.vy)
        # print("vert:", self.vertices)
        # print("curr:", self.current)
    # end of update()
        
    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.current)
        pygame.draw.lines(screen, color, closed=True, points=self.current)
        pygame.draw.line(screen, RED, [self.x, self.y], self.current[0])
        pygame.draw.circle(screen, BLUE, [self.x, self.y], radius = 7)

nboxes = 10
boxlist = []
for i in range(nboxes):
    x = np.random.randint(100, 200)
    y = np.random.randint(100, 200)
    color = np.random.randint(0, 256, size=3)
    vx = np.random.uniform(-10., 10.)
    vy = np.random.uniform(-10., 10.)
    print(i, "color = ", color, vx)
    b = Polygon(x=x, y=y, vx=vx, vy=vy, color=color)
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

    for b in boxlist:
        b.update()
        b.draw(screen)
    
    # 화면 업데이트
    pygame.display.flip()

    # 초당 60 프레임으로 업데이트
    clock.tick(60)

# 게임 종료
pygame.quit()