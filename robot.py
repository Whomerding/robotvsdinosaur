from weapon import Weapon
import random
weapon_name = ["mace", "laser beam", "bull whip", "turret gun", "baby grand piano"]

weapon_damage = [10, 20, 12, 50, 5]


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon (random.choice(weapon_name), random.choice(weapon_damage))


    def attack (self, dinosaur):
        self.dinosaur = dinosaur
        dinosaur.health -= self.active_weapon.attack_power
        
    def change_weapon (self):
        self.active_weapon = Weapon (random.choice(weapon_name), random.choice(weapon_damage))