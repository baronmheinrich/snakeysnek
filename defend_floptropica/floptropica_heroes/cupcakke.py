import base_character
import base_abilities

# self, name="Basic Attack", energy_cost=50, damage=100, tile_range=[(0, 0)], area_of_effect=0)
class Cupcakke(base_character.BaseCharacter):
    def __init__(self):
        super().__init__(name="Cupcakke", imagePath="./../character_assets/standees/player_cupcakke.png", movement=3, health=1000, energy=1000,
                         ability1=base_abilities.Abilities(name="Basic Attack", energy_cost=0, damage=350, tile_range=[1,1], area_of_effect=0, heal=0), #Basic attack, 1 tile away from cupcakke, single target
                         ability2=base_abilities.Abilities(name="Niagra Falls", energy_cost=600, damage=800, tile_range=[4,4], area_of_effect=0, heal=0), #ranged attack, 4x4 tiles away from cupcakke, single target
                         ability3=base_abilities.Abilities(name="Aesthetic Moan", energy_cost=400, damage=400, tile_range=[6,6], area_of_effect=1, heal=0), #ranged attack, 6x6 tiles away from cupcakke, area of effect 1 tile radius from clicked tile
                         ability4=base_abilities.Abilities(name="Slurp", energy_cost=300, damage=300, tile_range=[1,1], area_of_effect=0, heal=300)
                         ) #damage/healing ability, 1 tile away from cupcakke, single target
    
    