import pygame, sys, os
from pytmx.util_pygame import load_pygame

# Tile width is 64px by 32px!
# It seems silly to put the divide by 2 but it's just for sanity reasons
TILE_HEIGHT_HALF = 64/2
TILE_WIDTH_HALF = 32/2
GRID_WIDTH = 860
GRID_HEIGHT = 460

class cupcakke(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        cupcakke_image = pygame.image.load(os.path.join("defend_floptropica/character_assets/standees/player_cupcakke.png")).convert_alpha()
        cupcakke_image = pygame.transform.scale(cupcakke_image, (64, 128))
        self.image = cupcakke_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)


pygame.init()
screen = pygame.display.set_mode((GRID_WIDTH, GRID_HEIGHT))

s_width = screen.get_width() / 2
s_height = screen.get_height() / 8

# I REALLY want to see if it's probable to use the tmx array, csv, or some custom data structure to keep track of the tiles.
# Using the coordinates ALL THE TIME is going to be so laboroius.  I'd rather just pass in a unique tile ID or the tile at x and y point.
# Perhaps I can make a dictionary that keeps track of the tile coordinates and their types from the tmx_data object while drawing the map for the first time?
# As of right now, it seems like I would need to create a wrapper of some sort to build ontop of the existing coordinate system that pygame wants me to use.
cupcakke_player = cupcakke(367, 155)

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

    mouse_x, mouse_y = pygame.mouse.get_pos()

    draw_tiles(screen, "healthy", tmx_data)
    
    screen.blit(cupcakke_player.image, cupcakke_player.rect)
    # screen.blit(cupcakke_image, (mouse_x, mouse_y))
    
    pygame.display.update()
