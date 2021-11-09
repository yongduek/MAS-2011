# src: http://programarcadegames.com/index.php?chapter=introduction_to_animation&lang=en

"""
 Animating multiple objects using a list.
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/Gkhz3FuhGoI
"""
 
# Import a library of functions called 'pygame'
import pygame
import random
 
# Initialize the game engine
pygame.init()
 
FPS = 60  # frames per second
speed = 1000 / FPS # 50 mili seconds per frame rendering
print('ani speed', speed)

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
 
# Set the height and width of the screen
SIZE = [800, 800]
swidth, sheight = SIZE
 
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snow Animation 서용덕")
 
# Create an empty array
snow_list = []
snow_radius = []
# Loop 50 times and add a snow flake in a random x,y position
for i in range(5):
    x = random.randrange(0, swidth)
    y = random.randrange(0, sheight)
    snow_list.append([x, y])
    snow_radius.append( random.randrange(2, 20))
    # snow_color.append()
    

clock = pygame.time.Clock() # frame rate control

x_speed, y_speed = 1, 1

print(pygame.key.get_repeat())
pygame.key.set_repeat(100, 100)
print(pygame.key.get_repeat())

# Loop until the user clicks the close button.
done = False
while not done:
 
    for event in pygame.event.get():   # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True   # Flag that we are done so we exit this loop
    # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
            elif event.key == pygame.K_ESCAPE:
                quit()
            elif event.key == pygame.K_SPACE:
                snow_list.append( [random.randrange(0, swidth), random.randrange(0, sheight)] )
                snow_radius.append( random.randrange(2, 10) )
        # elif event.type == pygame.KEY
            #
        #
    # for event ...

    # Set the screen background
    screen.fill(BLACK)
 
    # Process each snow flake in the list
    for i in range(len(snow_list)):
 
        # Draw the snow flake
        # pygame.draw.circle(screen, WHITE, snow_list[i], 2)
        pygame.draw.circle(screen, 
                            WHITE, 
                            snow_list[i], 
                            snow_radius[i])
 
        # Move the snow flake down one pixel
        snow_list[i][1] += random.randrange(1, 3)
        snow_list[i][0] += random.randrange(-3, 4)
 
        # If the snow flake has moved off the bottom of the screen
        if snow_list[i][1] > sheight:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, swidth)
            snow_list[i][0] = x
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(FPS)  #
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()