import base_character
class Cupcakke(base_character.BaseCharacter):
    def __init__(self, name="Dummy", imagePath=None, movement=1, health=1000, energy=1000, abilityMenu=...):
        super().__init__(name, imagePath, movement, health, energy, abilityMenu):
        self.name = "Cupcakke"
        self.imagePath = "./../character_assets/player_cupakke.png"
        self.movement = 3
        self.health = 1000
        self.energy = 1000
        # ToDo: define unique abilities for Cupcakke
        # self.abilityMenu = []