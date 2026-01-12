# This snippit was supposed to be used in a tile grid context where the rest of the grid
# would be drawn as the player moves around.
# This project, atm, does not use a larger world map.
#
# class Tile(pygame.sprite.Sprite):
#     def __init__(self, pos, surf, groups):
#         super().__init__(groups)
#         self.image = surf
#         self.rect = self.image.get_rect(topleft=pos)


# This was supposed to be used to highlight the tile the mouse is hovering over.
# However, I don't think it is probable to draw isometric tiles in pygame
# def highlight_tile(screen, mouse_tile_x, mouse_tile_y, tmx_data):
#     highlight_surf = pygame.Surface((64, 32), pygame.SRCALPHA)
#     highlight_surf.fill((255, 255, 255, 100))  # White with transparency
#     print('mouse x: ', mouse_tile_x)
#     print('mouse y: ', mouse_tile_y)
#     iso_x = (mouse_tile_x - mouse_tile_y) * (TILE_HEIGHT_HALF) + s_width - 30
#     iso_y = (mouse_tile_x + mouse_tile_y) * (TILE_WIDTH_HALF) + s_height + 20
#     screen.blit(highlight_surf, (iso_x, iso_y))
#     pygame.display.update()