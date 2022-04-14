from Weapon import Weapon

class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 50
        self.weapon = weapon
        self.power_level = 30
    
    def attack(self, dinosaur):
        #lowers power level each time the robot attacks
        self.power_level -= 10
        #kills the dinosaur and prints message if the weapon power is greater than the dinosaur's health
        if self.weapon.attack_power >= dinosaur.health:
            dinosaur.health = 0
            print(f'{self.name} landed a blow on {dinosaur.name} with {self.weapon.name}, KILLING {dinosaur.name}')
        #lowers dinosaurs health by attack power from weapon and prints message about what happened
        else:
            dinosaur.health -= self.weapon.attack_power
            print(f'{self.name} attacked {dinosaur.name} and did {self.weapon.attack_power} damage leaving {dinosaur.name} with <<{dinosaur.health} HEALTH>> remaining')
        #assesses if the robot depleted all of their power with the attack - if they did, it drops their health to zero and prints a message saying they were killed
        if self.power_level == 0:
            self.health = 0
            print(f'{self.name} used the last of its power, dropping health to 0 and killing {self.name}')