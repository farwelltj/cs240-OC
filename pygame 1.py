#Ture Farwell
#oc-cs240 Advance Computer Science
#Pygame part 1 - Create a screen with a pale blue back round and a olympic flag
#pygame part 2 - Add a backround and have it spin

import pygame

pygame.init()

# Screen size
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

pie = pygame.image.load("pie.jpg").convert_alpha()
pie_rect = pie.get_rect()

horizontal = 1
vertical = 3

running = True
while running:

    screen.fill((186,203,240))
    screen.blit(pie, pie_rect)
    pygame.draw.rect(screen,(255, 255, 255),(160,100,300,250))
    pygame.draw.circle(screen, (0,0,255),(220,180), 50, 6)#blue
    pygame.draw.circle(screen,(0,0,0),(310,180),50,6) #black ring
    pygame.draw.circle(screen,(255,0,0),(400,180),50,6) #red ring
    pygame.draw.circle(screen,(255,255,0),(255,250),50,6) #yellow ring
    pygame.draw.circle(screen,(0,255,0),(360,250),50,6) #green ring
    pygame.display.flip() #

    pie_rect[0] += horizontal
    pie_rect[1] += vertical

    if pie_rect.right >= width:
        horizontal = -1
    elif pie_rect.left <= 0:
        horizontal = 1
    if pie_rect.bottom >= height:
        vertical = -3
    elif pie_rect.top <= 0:
        vertical = 3
    
    for event in pygame.event.get(): #code to exit program
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):#if you press the red x button or press q it will close the program.
            running = False
    
