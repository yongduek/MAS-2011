"""
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/4YqIKncMJNs
 Explanation video: http://youtu.be/ONAK8VZIcI4
 Explanation video: http://youtu.be/_6c4o41BIms
"""
 
import pygame
 
# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
 
# This sets the name of the window
pygame.display.set_caption('Bitmapped Graphics & Sound')
 
clock = pygame.time.Clock()
 
# Before the loop, load the sounds:
click_sound = pygame.mixer.Sound("assets/laser5.ogg")
 
# Set positions of graphics
background_position = [0, 0]
 
# Load and set up graphics.
background_image = pygame.image.load("assets/saturn_family1.jpg").convert()

# this is how to use BLACK as alpha (transparency) given an RGB image
# player_image = pygame.image.load("assets/player_3channel.png").convert()
# player_image.set_colorkey(BLACK)

# When the image has 4th alpha channel, use this.
# https://www.pygame.org/docs/ref/image.html
player_image = pygame.image.load("assets/player.png").convert_alpha()

done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
 
    # Copy image to screen:
    screen.blit(background_image, background_position)
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
 
    # Copy image to screen:
    screen.blit(player_image, [x, y])
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()

# End.