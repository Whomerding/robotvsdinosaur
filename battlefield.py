from dinosaur import Dinosaur
from robot import Robot

dinosaur_one = Dinosaur ("Gigamoose", 25)

robot_one = Robot ("Randy")

class Battlefield:
    def __init__(self):
        pass
 
    def run_game(self):
        pass

    def display_welcome (self):
        print (f"Welcome to a tournament of champions!  We have the terrifying Dinosaur {dinosaur_one.name} and the equally diabolical Robot {robot_one.name} fighting for ultimate superiority!")

    def battle_phase (self):
        while dinosaur_one.health or robot_one.health > 0:

            robot_one.attack
            print (f"{robot_one.name} attacks with a {robot_one.current_weapon} causing {robot_one.current_weapon.attack_power}!\n {dinosaur_one.name} has {dinosaur_one.health} remaining!")
            
            dinosaur_one.attack
            print (f"{dinosaur_one.name} attacks causing {dinosaur_one. attack_power} points of damage !\n {robot_one.name} has {robot_one.health} remaining!")
            
      

    def display_winner (self):
        pass

  
       
