import pygame, sys, os
from pytmx.util_pygame import load_pygame

# Tile width is 64px by 32px!
# It seems silly to put the divide by 2 but it's just for sanity reasons
TILE_HEIGHT_HALF = 64/2
TILE_WIDTH_HALF = 32/2
GRID_WIDTH = 860
GRID_HEIGHT = 460


pygame.init()
screen = pygame.display.set_mode((GRID_WIDTH, GRID_HEIGHT))

s_width = screen.get_width() / 2
s_height = screen.get_height() / 8

tmx_data = load_pygame("defend_floptropica/levels/tiles/tilemap_level1_v2.tmx")

def draw_tiles(screen, layer_name, tmx_data):
    layer = tmx_data.get_layer_by_name(layer_name)
    for x, y, image in layer.tiles():
        iso_x = (x - y) * (TILE_HEIGHT_HALF) + s_width - 30
        iso_y = (x + y) * (TILE_WIDTH_HALF) + s_height + 20
        screen.blit(image, (iso_x, iso_y))

# I think I might need to have a highlight tile..... unless I can draw an isometric square and ALSO layer it ontop of the map.
# ToDo: Add tile highlight on mouseover
# https://stackoverflow.com/questions/71592481/how-to-get-tile-selected-with-mouse


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_tiles(screen, "healthy", tmx_data)
    mouse_x, mouse_y = pygame.mouse.get_pos()

    pygame.display.update()
