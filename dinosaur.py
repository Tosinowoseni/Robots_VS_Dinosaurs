class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 50
        self.energy = 30
    
    def attack(self, robot, dinosaur_attack):
        #lowers energy level each time the dinosaur attacks
        self.energy -= 10
        #kills the robot and prints message if the attack power is greater than the robot's health
        if self.attack_power >= robot.health:
            robot.health = 0
            print(f'{self.name} landed a blow with {dinosaur_attack}, KILLING {robot.name}.')
        #lowers robot's health by attack power and prints message about what happened
        else:
            robot.health -= self.attack_power
            print(f'{self.name} attacked {robot.name} with {dinosaur_attack} and did {self.attack_power} damage leaving {robot.name} with <<{robot.health} HEALTH>> remaining')
        #assesses if the dinosaur depleted all of their energy with the attack - if they did, it drops their health to zero and prints a message saying they were killed
        if self.energy == 0:
            self.health = 0
            print(f'{self.name} used the last of its energy, dropping health to 0 and killing {self.