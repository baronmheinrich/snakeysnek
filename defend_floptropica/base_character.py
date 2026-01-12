# defining a base character class to use for inheritance.
# this class will contain common attributes and methods for all characters in the game.
import base_abilities

class BaseCharacter:
    def __init__(self, name="Dummy", imagePath=None, movement=1, health=1000, energy=1000,
                ability1=base_abilities.Abilities(), ability2=base_abilities.Abilities(),
                ability3=base_abilities.Abilities(), ability4=base_abilities.Abilities()):
        self.name = name
        self.imagePath = imagePath
        self.movement = movement
        self.health = health
        self.energy = energy
        self.abilityMenu = [ability1, ability2, ability3, ability4]

    def attack(self, target):
        damage = self.energy - target.energy
        damage = max(damage, 0)  # Ensure damage is not negative
        target.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0
    
    def has_energy(self, ability):
        return self.energy >= ability.energy_cost

    def __str__(self):
        return f"{self.name}: Health={self.health}, Energy={self.energy}, Abilities={self.abilityMenu}"