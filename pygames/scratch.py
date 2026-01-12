# This snippit was supposed to be used in a tile grid context where the rest of the grid
# would be drawn as the player moves around.
# This project, atm, does not use a larger world map.
#
# class Tile(pygame.sprite.Sprite):
#     def __init__(self, pos, surf, groups):
#         super().__init__(groups)
#         self.image = surf
#         self.rect = self.image.get_rect(topleft=pos)