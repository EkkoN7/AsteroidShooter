import pygame
import sys

def laser_update(laser_list, speed = 300):
    for laser in laser_list:
        laser.y -= round(speed * dt)
        if laser.bottom < 0:
                laser_list.remove(laser)


# game init
pygame.init()
window_width, window_height = 1280, 720
display_surface = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Asteroid Shooter")
clock = pygame.time.Clock() #framerate

# ship import
ship_surf = pygame.image.load('Assets/graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center = (window_width/2, window_height/2))

# background
bg_surf = pygame.image.load('Assets/graphics/background.png').convert()

# laser import
laser_surf = pygame.image.load('Assets/graphics/laser.png').convert_alpha()
laser_list = []


# import text
font = pygame.font.Font('Assets/graphics/subatomic.ttf',50)
text_surf = font.render("Space", True, "White" )
text_rect = text_surf.get_rect(midbottom = (window_width/2, window_height - 80))

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            laser_rect = laser_surf.get_rect(midbottom=ship_rect.midtop)
            laser_list.append(laser_rect)


    # framerate limit
    dt = clock.tick(120) / 1000

    # mouse input
    ship_rect.center = pygame.mouse.get_pos()
    pygame.mouse.get_pressed()
    # update
    laser_update(laser_list)

    # drawing
    display_surface.fill((0,0,0))
    display_surface.blit(bg_surf,(0,0))

    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(display_surface, "white", text_rect.inflate(30,30), width = 8, border_radius= 10)

    display_surface.blit(ship_surf,ship_rect)
    for laser in laser_list:
        display_surface.blit(laser_surf, laser)

    # draw the final frame
    pygame.display.update()