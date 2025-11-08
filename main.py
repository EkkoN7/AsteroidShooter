import pygame
import sys

pygame.init()

window_width, window_height = 1280, 720
display_surface = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Asteroid Shooter")
clock = pygame.time.Clock() #framerate

#importing images
ship_surf = pygame.image.load('Assets/graphics/ship.png').convert_alpha()
bg_surf = pygame.image.load('Assets/graphics/background.png').convert()
font = pygame.font.Font('Assets/graphics/subatomic.ttf',50)
text_surf = font.render("Space", True, "White" )

#rect
ship_rect = ship_surf.get_rect(center = (window_width/2, window_height/2))
text_rect = text_surf.get_rect(midbottom = (window_width/2, window_height - 80))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(120) #framerate limit

    ship_rect.center = pygame.mouse.get_pos()
    pygame.mouse.get_pressed()

    display_surface.fill((0,0,0))
    display_surface.blit(bg_surf,(0,0))
    display_surface.blit(ship_surf,ship_rect)
    display_surface.blit(text_surf,text_rect)

    pygame.display.update()