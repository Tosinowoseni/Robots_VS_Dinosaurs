from Robot import Robot
from Weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots = []
        self.armory = []
        self.create_armory()
        self.create_fleet()

    #creates an armory of weapons that the robot team can choose from    
    def create_armory(self):
        weapon_one = Weapon('Paper Cutter', 10)
        weapon_two = Weapon('Mind Control', 30)
        wepaon_three = Weapon('Broken Bottle', 20)
        self.armory.append(weapon_one)
        self.armory.append(weapon_two)
        self.armory.append(wepaon_three)
    
    #creates a fleet of robots and sets a default weapon
    def create_fleet(self):
        robo_one = Robot('R2D2', self.armory[0])
        robo_two = Robot('HAL', self.armory[1])
        robo_three = Robot('Bender', self.armory[2])
        self.robots.append(robo_one)
        self.robots.append(robo_two)
        self.robots.append(robo_three)
    
    #allows the robot to swap the weapon they are using
    def weapon_swap(self, robot_choice):
        print('****************************************')
        print('TEAM ROBOT! Pick your weapon: ')
        for i in self.armory:
            print(f'{str(self.armory.index(i))} for {i.name}. Attack Power: {i.attack_power}')
        weapon_choice = input('Enter your choice of weapon ')
        while weapon_choice != '0' and weapon_choice != '1' and weapon_choice != '2':
            weapon_choice = input('Enter your choice of weapon ')
        if weapon_choice == '0' or weapon_choice == '1' or weapon_choice == '2':
            for i in self.robots:
                if i == robot_choice:
                    i.weapon = self.armory[int(weapon_choice)]
            
