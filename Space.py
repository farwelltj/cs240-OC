# pygame1.py
# A simple pygame program

import random
import pygame

width, height = 800, 600
def init():
    pygame.init() # Initialized pygame module

    # Screen
    return pygame.display.set_mode((width, height))

def draw_space(surface, stars):
    surface.fill((0, 0, 0)) # Draw the vacuum of space
    for s in stars:
        if s[2] == 3:
            star = pygame.Color(255, 255, 255)
        elif s[2] == 2:
            star = pygame.Color(200, 200, 255)
            # star = pygame.Color(0, 0, 200)
        elif s[2] == 1:
            star = pygame.Color(255, 170, 170)
            # star = pygame.Color(200, 0, 0)
        pygame.draw.circle(surface, star, s[:2], s[2])

def build_space(screen):
    # Get a new surface and its parameters
    space = screen.copy()
    width, height = screen.get_size()

    stars = []
    for star in range(60):
        x = random.randint(0, width)
        y = random.randint(0, height)
        rand = random.randint(1, 10)
        if rand <= 6:
            r = 1
        elif rand <= 9:
            r = 2
        else:
            r = 3
        stars.append((x, y, r))
    # print stars

    draw_space(space, stars)
    return space

def load_ship():
    ship = pygame.image.load('ship.png').convert()
    raw_size = ship.get_size()

    ship = ship.subsurface((0, 0, raw_size[0] / 2, raw_size[1] / 2))
    new_size = ship.get_size()

    ship = ship.subsurface((new_size[0] / 2 - 10, new_size[1] / 2, new_size[0] / 2 + 10, new_size[1] / 2))
    ship.set_colorkey((191, 220, 191))
    return ship

def load_bubble():
    bubble = pygame.image.load('bubble.bmp').convert()
    raw_size = bubble.get_size()

    bubble = bubble.subsurface((0,0, raw_size[0] / 2, raw_size[1] / 2))
    new_size = bubble.get_size()

    bubble = bubble.subsurface((new_size[0] / 2 - 10, new_size[1] / 2, new_size[0] / 2 + 10, new_size[1] / 2))
    bubble.set_colorkey((191, 220, 191))
    
    return bubble


def main(screen):
    running = True


    
    bubble = load_bubble()
    ship = load_ship()
    space = build_space(screen)
    while running:
        screen.blit(space, (0, 0))
        screen.blit(ship, (100, 100))
        screen.blit(bubble, (205, 300))
        pygame.display.flip() # Display screen in window

        x, y = (100,100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                # exit()
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                y-=1
            
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                x-=1
            
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                y+=1

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                x+=1



screen = init()
main(screen)
