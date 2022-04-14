from Fleet import Fleet
from Herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        #display a welcome message
        self.display_welcome() 

        #pick fighters and battle while both teams have health above zero. this will alternate between battle_dino_start and battle_robot_start 
        # to dictate who attacks first in the round (this is just based off of who started first last time, each game Dino starts first)
        dino_start = True
        while self.health_calculation() == True:
            if dino_start == True:
                self.battle_dino_start()
                dino_start = False
            else:
                self.battle_robot_start()
                dino_start = True
            
        #display winner
        if self.health_calculation() == False:
            self.display_winners()

    def display_welcome(self):
        print('Welcome to ROBOTS vs DINOSAURS!!')

    # This is where the battle starts when its the dinosaur's turn to start
    #1. Player chooses dino and dino attack
    #2. Player chooses robot and robot weapon
    #3. calls the dino turn method
    #2. If the dino kills the robot, it prints a message saying the robot died, which ends the round
    #3. If the robot doesn't die, then it calls the robot's turn method
    def battle_dino_start(self):
        dinosaur_choice = self.show_dino_fighter_options()
        dinosaur_attack = self.choose_attack()
        robot_choice = self.show_robo_fighter_options()
        self.change_weapon(robot_choice)
        print('****************************************')
        print('READY...SET...BATTLE!!!')
        print('****************************************')
        self.dino_turn(dinosaur_choice, robot_choice, dinosaur_attack)
        if robot_choice.health == 0:
            print(f'{robot_choice.name} died, ending the round.')
        elif dinosaur_choice.health == 0:
            print(f'{dinosaur_choice.name} died, ending the round.')
        else: 
            self.robo_turn(robot_choice, dinosaur_choice)

    # This runs the attacks when the dino attacks first
    #1. Calls the attack method from the Dinosaur class
    def dino_turn(self, dinosaur_choice, robot_choice, dinosaur_attack):
        print('DINOSAUR\'S TURN')
        dinosaur_choice.attack(robot_choice, dinosaur_attack)
        
        
    # Same as battle_dino_start, but with Robot going first
    def battle_robot_start(self):
        robot_choice = self.show_robo_fighter_options()
        self.change_weapon(robot_choice)
        dinosaur_choice = self.show_dino_fighter_options()
        dinosaur_attack = self.choose_attack()
        print('****************************************')
        print('READY...SET...BATTLE!!!')
        print('****************************************')
        self.robo_turn(robot_choice, dinosaur_choice)
        if dinosaur_choice.health == 0:
            print(f'{dinosaur_choice.name} died, ending the round.')
        elif robot_choice.health == 0:
            print(f'{robot_choice.name} died, ending the round.')
        else:
            self.dino_turn(dinosaur_choice, robot_choice, dinosaur_attack)
        
    # This runs the attacks when the dino attacks first
    #1. Calls the attack method from the Robot class
    def robo_turn(self, robot_choice, dinosaur_choice):
        print('ROBOT\'S TURN')
        robot_choice.attack(dinosaur_choice)
        
    
    # Prints dinosaur options and prompts user to pick their dinosaur for the round
    def show_dino_fighter_options(self):
        print('****************************************')
        print('TEAM DINOSAUR! Pick your dinosaur: ')
        for i in self.herd.dinosaurs:
            if i.health > 0:
                print(f'{str(self.herd.dinosaurs.index(i))} for {i.name}. || Remaining Health: {i.health} || Energy Level: {i.energy} || Attack Power: {i.attack_power}')
        dinosaur_choice = input('Enter your choice of dinosaur ')
        while dinosaur_choice != '0' and dinosaur_choice != '1' and dinosaur_choice != '2':
            dinosaur_choice = input('Enter your choice of dinosaur ')
        if dinosaur_choice == '0' or dinosaur_choice == '1' or dinosaur_choice == '2':
            for i in self.herd.dinosaurs:
                while self.herd.dinosaurs.index(i) == int(dinosaur_choice) and i.health == 0:
                    dinosaur_choice = input(f'{i.name} is dead! Pick a dinosaur from the list above! Enter your choice of dinosaur: ')
            dinosaur_choice = self.herd.dinosaurs[int(dinosaur_choice)]  
        return dinosaur_choice

    # Prints robot options and prompts user to pick their robot for the round
    def show_robo_fighter_options(self):
        print('****************************************')
        print('TEAM ROBOT! Pick your robot: ')
        for i in self.fleet.robots:
            if i.health > 0:
                print(f'{str(self.fleet.robots.index(i))} for {i.name}. || Remaining Health: {i.health} || Power Level: {i.power_level}')
        robot_choice = input('Enter your choice of robot ')
        while robot_choice != '0' and robot_choice != '1' and robot_choice != '2':
            robot_choice = input('Enter your choice of robot ')
        if robot_choice == '0' or robot_choice == '1' or robot_choice == '2':
            for i in self.fleet.robots:
                while self.fleet.robots.index(i) == int(robot_choice) and i.health == 0:
                    robot_choice = input(f'{i.name} is dead! Pick a robot from the list above! Enter your choice of robot: ')
            robot_choice = self.fleet.robots[int(robot_choice)]
        return robot_choice

    # Asks user if they want to change their robot's weapon, if they do, it calls the weapon_swap method from the fleet class
    def change_weapon(self, robot_choice):
        print(f'TEAM ROBOT, {robot_choice.name}\'s current weapon is {robot_choice.weapon.name} - do you want to change it?')
        weapon_change = input('Change weapon? Y/N ').upper()
        while weapon_change != 'Y' and weapon_change != 'N':
            weapon_change = input('Change weapon? Y/N ')
        if weapon_change == 'Y':
            self.fleet.weapon_swap(robot_choice)
    
    # Prints dinosaur attack options and prompts user to pick one for the round
    def choose_attack(self):
        print('****************************************')
        attack_tuple = ("Eye Scratch", "Dive Bomb", "Bite")
        print(f'TEAM DINOSAUR, choose your attack!')
        count = 0
        for i in attack_tuple:
            print(f'{str(count)} for {i}.')
            count += 1
        attack_choice = input('Choose your attack ')
        while attack_choice != '0' and attack_choice != '1' and attack_choice != '2':
            attack_choice = input('Choose your attack ')
        if attack_choice == '0' or attack_choice == '1' or attack_choice == '2':
            attack_choice = attack_tuple[int(attack_choice)]
        return attack_choice
         
    # Calculates total health to determine whether the battle should continue or if there is a winner
    def health_calculation(self):
        total_health_dino = 0
        total_health_robot = 0
        keep_playing = True
        for i in self.fleet.robots:
            if i.health > 0:
                total_health_robot += i.health
        for i in self.herd.dinosaurs:
            if i.health > 0:
                total_health_dino += i.health
        if total_health_dino <= 0 or total_health_robot <= 0:
            keep_playing = False
        return keep_playing

    # Prints final game stats and prints the winner of the game
    def display_winners(self):
        print('****************************************')
        print('WE HAVE A WINNER.....')
        total_health_dino = 0
        total_health_robot = 0
        winner = ''
        print('STATS:')
        for i in self.fleet.robots:
            print(f'Robot: {i.name} Remaining Health: {i.health}')
            total_health_robot += i.health
        for i in self.herd.dinosaurs:
            print(f'Dinosaur: {i.name} Remaining Health: {i.health}')
            total_health_dino += i.health
        if total_health_dino == total_health_robot:
            winner = 'IT\'S A TIE!!!!'
        elif total_health_dino > 0:
            winner = 'TEAM DINOSAUR'
        else:
            winner = 'TEAM ROBOT'
        print('****************************************')
        print(f'THE WINNER IS {winner}!!!!')
        print('****************************************')