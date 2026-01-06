# defining a base ENEMY class to use for inheritance.
# this class will contain common attributes and methods for all ENEMIES in the game.

class BaseEnemy:
    def __init__(self, name="DummyBaddie", health=1000, movement=1, attack_power=100):
        self.name = name
        self.health = health
        self.movement = movement
        self.attack_power = attack_power

    def attack(self, target):
        damage = self.attack_power
        target.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name}: Health={self.health}, Energy={self.energy}, Attack Power={self.attack_power}"
