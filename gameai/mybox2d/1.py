#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
An attempt at some simple, self-contained pygame-based examples.

Example 01

In short:
One static body: a big polygon to represent the ground
One dynamic body: a rotated big polygon
And some drawing code to get you going.

kne
"""
import pygame
import numpy as np
from pygame.locals import (QUIT, KEYDOWN, K_ESCAPE)

import Box2D  # The main library
# Box2D.b2 maps Box2D.b2Vec2 to vec2 (and so on)
from Box2D.b2 import (world, polygonShape, staticBody, dynamicBody)

# --- constants ---
# Box2D deals with meters, but we want to display pixels,
# so define a conversion factor:
PPM = 20.0  # pixels per meter
TARGET_FPS = 60
TIME_STEP = 1.0 / TARGET_FPS
SCREEN_WIDTH, SCREEN_HEIGHT = 1640, 1480

# --- pygame setup ---
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('Simple pygame example')
clock = pygame.time.Clock()

# --- pybox2d world setup ---
# Create the world
world = world(gravity=(0, -10), doSleep=True)

# And a static body to hold the ground shape
ground_body = world.CreateStaticBody(
    position=(41, .1),
    shapes=polygonShape(box=(40, 2)),
)

# Create a dynamic body
dynamic_body = world.CreateDynamicBody(position=(10, 15), angle=15)

# And add a box fixture onto it (with a nonzero density, so it will move)
box = dynamic_body.CreatePolygonFixture(box=(2, 1), density=1, friction=0.3, restitution=.9)

colors = {
    staticBody: (255, 255, 255, 255),
    dynamicBody: (127, 127, 127, 255),
}

bodylist = [dynamic_body, ground_body]

# --- main game loop ---
running = True
tick = 0
while running:
    tick += 1
    # Check the event queue
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            # The user closed the window or pressed escape
            running = False



    removelist = []
    for i, body in enumerate(world.bodies):
        # print(i, body.position)
        if body.position[1] < 0:
            removelist.append(body)
    for b in removelist:
        world.DestroyBody(b)
    
    if tick % 5 == 0:
        # print(f"tick: {tick} : create a new body")
        # Create a dynamic body
        _x = np.random.uniform(43,48)
        _y = np.random.uniform(70, 72)
        _dynamic_body = world.CreateDynamicBody(position=(_x, _y), angle=np.random.uniform(0, 90))
        _dynamic_body.linearVelocity = (np.random.uniform(-10, 10), np.random.uniform(-50, 5))
        # And add a box fixture onto it (with a nonzero density, so it will move)
        _density = np.random.uniform(0.5, 10)
        _friction = np.random.uniform(.1, .9)
        _restitution = np.random.uniform(.8, .99)
        
        _w = np.random.uniform(.5, 2)
        _h = np.random.uniform(.1,1)
        _box = _dynamic_body.CreatePolygonFixture(box=(_w, _h), 
                                                  density=_density, 
                                                  friction=_friction, 
                                                  restitution=_restitution)
        
        
        
                # Create a dynamic body
        # _dynamic_body = world.CreateDynamicBody(position=(10, 15), angle=15)

        # # And add a box fixture onto it (with a nonzero density, so it will move)
        # box = _dynamic_body.CreatePolygonFixture(box=(2, 1), density=1, friction=0.3, restitution=.9)

        bodylist.append(_dynamic_body)


    screen.fill((0, 0, 0, 0))
    # Draw the world
    for body in bodylist: # (ground_body, dynamic_body):  # or: world.bodies
        # The body gives us the position and angle of its shapes
        for fixture in body.fixtures:
            # The fixture holds information like density and friction,
            # and also the shape.
            shape = fixture.shape

            # Naively assume that this is a polygon shape. (not good normally!)
            # We take the body's transform and multiply it with each
            # vertex, and then convert from meters to pixels with the scale
            # factor.
            vertices = [(body.transform * v) * PPM for v in shape.vertices]

            # But wait! It's upside-down! Pygame and Box2D orient their
            # axes in different ways. Box2D is just like how you learned
            # in high school, with positive x and y directions going
            # right and up. Pygame, on the other hand, increases in the
            # right and downward directions. This means we must flip
            # the y components.
            vertices = [(v[0], SCREEN_HEIGHT - v[1]) for v in vertices]

            # print(colors[body.type], " @ ", vertices)
            pygame.draw.polygon(screen, colors[body.type], vertices)
    # print(" --------------- ")
    # Make Box2D simulate the physics of our world for one step.
    # Instruct the world to perform a single step of simulation. It is
    # generally best to keep the time step and iterations fixed.
    # See the manual (Section "Simulating the World") for further discussion
    # on these parameters and their implications.
    world.Step(TIME_STEP, 10, 10)

    # Flip the screen and try to keep at the target FPS
    pygame.display.flip()
    clock.tick(TARGET_FPS)

pygame.quit()
print('Done!')