import pygame
import sys
import pymunk

width = 500
height = 500

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 97)


def lemon_create(simulation, pos):
    body = pymunk.Body(3, 120, body_type=pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, 20)
    simulation.add(body, shape)
    return shape


def lemon_make(lemons):
    for lemon in lemons:
        posx = int(lemon.body.position.x)
        posy = int(lemon.body.position.y)
        lemon_rect = lemonimage.get_rect(center=(posx, posy))
        screen.blit(lemonimage, lemon_rect)


def staticobj(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (230, 300)
    shape = pymunk.Circle(body, 30)
    simulation.add(body, shape)
    return shape


def drawstaticobj(objects):
    for object in objects:
        posx = int(object.body.position.x)
        posy = int(object.body.position.y)
        pygame.draw.circle(screen, (white), (posx, posy), 30)


pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
simulation = pymunk.Space()
simulation.gravity = (0, 100)
lemonimage = pygame.image.load("lemon.png")
lemons = []
objects = []
objects.append(staticobj(simulation))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            lemons.append(lemon_create(simulation, event.pos))

    screen.fill((blue))
    lemon_make(lemons)
    drawstaticobj(objects)
    simulation.step(1/50)
    pygame.display.update()
    clock.tick(144)
