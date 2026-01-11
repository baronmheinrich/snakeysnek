import pygame, sys, os
from pytmx.util_pygame import load_pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topright=pos)

#Tile width is 64px!
pygame.init()
screen = pygame.display.set_mode((800, 400))


tmx_data = load_pygame("defend_floptropica/levels/tiles/tilemap_level1_v2.tmx")

healthy_layer = tmx_data.get_layer_by_name('healthy')
polluted_layer = tmx_data.get_layer_by_name('polluted')

print("healthy layer:")
for layer in healthy_layer:
    print(layer)

print("polluted layer:")
for layer in polluted_layer:
    print(layer)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill('black')
    pygame.display.update()
