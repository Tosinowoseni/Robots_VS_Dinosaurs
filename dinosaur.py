#Name: Tosin Owoseni
#Date: April 9th 2022
#File: dinosaur.py
#Proj: Robots vs. Dinosaurs

#imports
#from robot import Robot

class Dinosaur:
    def __init__(self,name,health, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = health

    def attack(self, robot):
        robot.health -= self.attack_power
