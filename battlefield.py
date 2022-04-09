#Name: Tosin Owoseni
#Date: April 9th 2022
#File: battlefield.py
#Proj: Robots vs. Dinosaurs

# imports
from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.battle()

    # 1995-esque Intro
    def display_welcome(self):
        print("**************************************")
        print("ROBOTS VS. DINOSAURS")
        print("**************************************")
        print("A battle of the future vs. the past")
        print("Robotics vs. Dinosaur land") 
        print("Let's Get Down To BUISNESSSSSSSSS")
        print("**************************************\n")

    def battle(self):
        while len(self.herd.dinosaur_list) > 0 and  len(self.fleet.robots_list) > 0:
            battle_choice = input("Who is attacking: dinosaurs or robots? ")

            if(battle_choice == 'dinosaurs'):
                Battlefield.dino_turn(self)
            elif(battle_choice == 'robots'):
                Battlefield.robo_turn(self)

            #Check list length to see if > 0, then return winner
            if len(self.herd.dinosaur_list) == 0:
                self.display_winners("Robots")
            elif len(self.fleet.robots_list) == 0:
                self.display_winners("Dinosaurs")

    def dino_turn(self):
        self.herd.dinosaur_list[0].attack(self.fleet.robots_list[0])
        print(self.herd.dinosaur_list[0].name + " attacked " + self.fleet.robots_list[0].name + " for " + str(self.herd.dinosaur_list[0].attack_power) + " damage!")
        print(self.fleet.robots_list[0].name + " has " + str(self.fleet.robots_list[0].health) + " health remaining.\n")

        if(self.fleet.robots_list[0].health <= 0):
            print(self.fleet.robots_list[0].name + " got the blue screen of death!\n")
            self.fleet.robots_list.pop(0)

    def robo_turn(self):
        self.fleet.robots_list[0].attack(self.herd.dinosaur_list[0])
        print(self.fleet.robots_list[0].name + " attacked " + self.herd.dinosaur_list[0].name + " for " + str(self.fleet.robots_list[0].weapon.attack_power) + " damage!")
        print(self.herd.dinosaur_list[0].name + " has " + str(self.herd.dinosaur_list[0].health) + " health remaining.\n")
        
        if(self.herd.dinosaur_list[0].health <= 0):
            print(self.herd.dinosaur_list[0].name + " has gone extinct!\n")
            self.herd.dinosaur_list.pop(0)

    def display_winners(self, victor):
        print("*********************************")       
        print("And the " + victor + " are victorious!")
        