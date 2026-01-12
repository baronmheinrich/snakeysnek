import pygame, sys, os
from pytmx.util_pygame import load_pygame
import pytmx

# Tile width is 64px by 32px!
# It seems silly to put the divide by 2 but it's just for sanity reasons
TILE_HEIGHT_HALF = 64/2
TILE_WIDTH_HALF = 32/2

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)

pygame.init()
screen = pygame.display.set_mode((860, 460))

s_width = screen.get_width() / 2
s_height = screen.get_height() / 8

tmx_data = load_pygame("defend_floptropica/levels/tiles/tilemap_level1_v2.tmx")

def draw_tiles(screen, layer_name, tmx_data):
    layer = tmx_data.get_layer_by_name(layer_name)
    for x, y, image in layer.tiles():
        iso_x = (x - y) * (TILE_HEIGHT_HALF) + s_width - 30
        iso_y = (x + y) * (TILE_WIDTH_HALF) + s_height + 20
        screen.blit(image, (iso_x, iso_y))

# ToDo: Add tile highlight on mouseover
# https://stackoverflow.com/questions/71592481/how-to-get-tile-selected-with-mouse


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    draw_tiles(screen, "healthy", tmx_data)    
    pygame.display.update()
