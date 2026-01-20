import pygame, sys, os, math 
from pprint import pprint
from pytmx.util_pygame import load_pygame

# Tile width is 64px by 32px!
# It seems silly to put the divide by 2 but it's just for sanity reasons
TILE_HEIGHT_HALF = 64/2
TILE_WIDTH_HALF = 32/2
GRID_WIDTH = 860
GRID_HEIGHT = 460

print_once = False

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

isometric_navigator = {}
isometric_navi = {}

ORIGIN_X = screen.get_width() / 2
ORIGIN_Y = screen.get_height() / 10
OFFSET_X = ORIGIN_X - 30
OFFSET_Y = ORIGIN_Y + 20

# I REALLY want to see if it's probable to use the tmx array, csv, or some custom data structure to keep track of the tiles.
# Using the coordinates ALL THE TIME is going to be so laboroius.  I'd rather just pass in a unique tile ID or the tile at x and y point.
# Perhaps I can make a dictionary that keeps track of the tile coordinates and their types from the tmx_data object while drawing the map for the first time?
# As of right now, it seems like I would need to create a wrapper of some sort to build ontop of the existing coordinate system that pygame wants me to use.
# cupcakke_player = cupcakke(367, 155)

tmx_data = load_pygame("defend_floptropica/levels/tiles/tilemap_level1_v2.tmx")


def draw_tiles(screen, layer_name, tmx_data):
    layer = tmx_data.get_layer_by_name(layer_name)
    navi_id = 0
    for x, y, image in layer.tiles():
        iso_x = (x - y) * (TILE_HEIGHT_HALF) + ORIGIN_X - 30
        iso_y = (x + y) * (TILE_WIDTH_HALF) + ORIGIN_Y + 20
        isometric_navigator[navi_id] = {'x': x, 'y': y, 'iso_x': iso_x, 'iso_y': iso_y, 'image': image}
        isometric_navi[(navi_id, iso_x, iso_y)] = {'id': navi_id,'x': x, 'y': y, 'image': image}
        # idgaf if += is the same as navi_id = navi_id + 1, THIS IS JUST MORE READABLE!!!!
        
        navi_id = navi_id + 1
        # if(navi_id == 67):
        #     continue
        screen.blit(image, (iso_x, iso_y))

# This conversion function ALMOST works as intended.
# The issue is that the coordinates are slightly off by 1 depending on where on the grid the mouse is clicked.
# I think it's the way the tile height and width are calculated and divided by 2 by integer division that is causing the issue.
# I'll need to revisit this later.
def mouse_to_iso(mouse_x, mouse_y):
    temp_x = mouse_x - ORIGIN_X 
    temp_y = mouse_y - ORIGIN_Y
    
    fract_x = 0.5 * ((temp_x / TILE_HEIGHT_HALF) + (temp_y / TILE_WIDTH_HALF))
    fract_y = 0.5 *((temp_y / TILE_WIDTH_HALF) - (temp_x / TILE_HEIGHT_HALF))
    
    round_x = math.floor(fract_x)
    round_y = math.floor(fract_y)
    
    tile_x = ORIGIN_X + (round_x - round_y) * TILE_HEIGHT_HALF
    tile_y = ORIGIN_Y + (round_x + round_y) * TILE_WIDTH_HALF
    
    mouse_position_x = mouse_x - tile_x
    mouse_position_y = mouse_y - tile_y
    
    d_x = mouse_position_x / TILE_WIDTH_HALF
    d_y = mouse_position_y / TILE_HEIGHT_HALF
    
    if((abs(d_x)/TILE_WIDTH_HALF) + (abs(d_y)/TILE_HEIGHT_HALF)) > 1:
        if(d_y < 0):
            if(d_x < 0):
                round_x = round_x - 1
            else:
                round_y = round_y - 1
        else:
            if(d_x < 0):
                round_y = round_y + 1
            else:
                round_x = round_x + 1
    if( 0 <= round_x < ORIGIN_X and 0 <= round_y < ORIGIN_Y):
        return (round_x, round_y)
    return None

# I think I might need to have a highlight tile..... unless I can draw an isometric square and ALSO layer it ontop of the map.
# ToDo: Add tile highlight on mouseover
# https://stackoverflow.com/questions/71592481/how-to-get-tile-selected-with-mouse


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            current_click = pygame.mouse.get_pos()
            print('Mouse button pressed at:', pygame.mouse.get_pos())
            iso_mouse = mouse_to_iso(current_click[0], current_click[1])
            print('Converted to iso coords:', iso_mouse)
            # print("Tile GID at position:", tmx_data.get_tile_image(iso_mouse[0], iso_mouse[1], 1))
            
            # try:
            #     print("Tile GID at position:", tmx_data.get_tile_gid(current_click[0], current_click[1], 1))
            # except Exception as e:
            #     print("Error getting tile GID:", e)


    mouse_x, mouse_y = pygame.mouse.get_pos()

    draw_tiles(screen, "healthy", tmx_data)
    if print_once == False:
        print('print!')
        # pprint(isometric_navigator)
        # print('split')
        pprint(isometric_navi)
        print_once = True
    # screen.blit(cupcakke_player.image, cupcakke_player.rect)
    # screen.blit(cupcakke_image, (mouse_x, mouse_y))
    
    pygame.display.update()
