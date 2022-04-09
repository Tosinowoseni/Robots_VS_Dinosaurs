#Name: Tosin Owoseni
#Date: April 9th 2022
#File: herd.py
#Proj: Robots Vs Dinosaurs

#imports
from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaur_list = []
        self.create_herd()

    def create_herd(self):
        trex = Dinosaur("T-Rex", 100, 50)
        raptor = Dinosaur("Raptor", 80, 40)
        flyer = Dinosaur("Pterodactyl",80, 40)

        self.dinosaur_list.append(trex)
        self.dinosaur_list.append(raptor)
        self.dinosaur_list.append(flyer)