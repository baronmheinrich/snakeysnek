import game_master
import base_character
import base_enemy

def level1_setup():
    gm = game_master.GameMaster()
    enemy_maker = base_enemy.BaseEnemy
    character_maker = base_character.BaseCharacter

    b1 = enemy_maker(name="Baddie1", health=300, movement=1, attack_power=50)
    h1 = character_maker(name="Cupcakke", movement=3, health=1000, energy=500)

# Define the level layout in matrix form here
# 10x10 grid example.  No null tiles.
    level = [
        [0,0,h1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,b1,0]]
    