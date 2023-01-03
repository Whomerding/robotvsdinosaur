from weapon import Weapon
import random
weapon_name = ["mace", "laser beam", "bull whip", "turret gun", "baby grand piano"]

weapon_damage = [10, 20, 12, 50, 5]

current_weapon = Weapon ((random.choice (weapon_name), random.choice (weapon_damage)))

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon: Weapon
    
    def choose_weapon (self):
        self.current_weapon = Weapon (random.choice (weapon_name), random.choice (weapon_damage))
        self.current_weapon = current_weapon

    def attack (self, dinosaur):
        self.dinosaur = dinosaur
        dinosaur.health -= current_weapon.attack_power

