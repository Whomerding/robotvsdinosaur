from dinosaur import Dinosaur
from robot import Robot


class Battlefield:
    def __init__(self):
        self.dinosaur_one = Dinosaur ("Gigamoose", 15)
        self.robot_one = Robot ("Randy")
 
    def run_game (self):
        self.display_welcome ()
        self.battle_phase ()
        self.display_winner ()
    
    def display_welcome (self):
        print (f"Welcome to a tournament of champions!  We have the terrifying Dinosaur {self.dinosaur_one.name} and the equally diabolical Robot {self.robot_one.name} fighting for ultimate superiority!")

    def battle_phase (self):
        
            while self.dinosaur_one.health > 0 and self.robot_one.health > 0:
                self.robot_one.attack (self.dinosaur_one)
                print (f"{self.robot_one.name} attacks with a {self.robot_one.active_weapon.name} causing {self.robot_one.active_weapon.attack_power} points of damage!")
                self.robot_one.change_weapon ()
                if self.dinosaur_one.health > 0:
                    print (f"{self.dinosaur_one.name} has {self.dinosaur_one.health} remaining!")
                    self.dinosaur_one.attack (self.robot_one)
                    print (f"{self.dinosaur_one.name} attacks causing {self.dinosaur_one.attack_power} points of damage!\n {self.robot_one.name} has {self.robot_one.health} remaining!")
                
             
       
    def display_winner (self):
        if self.dinosaur_one.health > 0:
            print ("the dino wins!!")

        else:
            print ("The robot wins!!")
            


    

    

       
