import random
import time
# import os

# Creating the tank class
class Tank(object):
    def __init__(self, name):
        self.name = name
        self.alive=True
        self.ammo=5
        self.armor=60

    def __str__(self):
        if self.alive:
            return "%s (%i armor, %i shells)" % (self.name, self.armor, self.ammo)
        else:
            return "%s (DEADE)" % self.name

    def fire_at(self, enemy):
        if self.ammo >=1:
            self.ammo -=1
            print(self.name, "fires on", enemy.name)
            enemy.hit()
        else:
            print(self.name, "has no shells!")

    def hit(self):
        self.armor -=20
        print(self.name, "is hit")
        if self.armor <=0:
            self.explode()

    def explode(self):
        self.alive = False
        print(self.name, "explodes!")


# Function to print the tank's keys and their respective stats
def print_tanks(tanks):

    for tank in tanks:

        print(("Tank Key: " + tank + " -"), end =" ")
        print(tanks[tank])

# Sorts a char (tank key in this case) between a given String
def sort_tank(string):

    return (random.choice(string))

# Returns a string (For example: "abd") that is used to control the available tanks on the dictionary
def get_available_tanks(tanks):

    remaining_tanks = ""

    for tank in tanks:

        remaining_tanks += tank

    return remaining_tanks

# "Clears the screen", basically prints 40 lines
def clear_screen():

    print("\n" * 40)

    # OS function that cleans the screen when the file is executed from windows terminal
    # _=os.system('cls')

# Starts the game (duuh)
def start_game(tanks):

    print("\nGame started!\n")

    # Round counter
    round = 0

    # Keeps executing the game process until there is only one tank on the tanks array
    while(len(tanks) > 1):

        clear_screen()

        # Increments each round        
        round += 1

        # Restart the remaining attackers controler on each round, based on the existent tanks' keys on the tank array
        remaining_attackers = get_available_tanks(tanks)

        print("\nRound " + str(round) + "\n")

        # Keeps executing until all the players have played once on the current round
        while(len(remaining_attackers) > 0):

            # Sorts the current attacker
            current_attacker = sort_tank(remaining_attackers)
        
            # Remove the current attacker from the remaining attackers controller string
            remaining_attackers = remaining_attackers.replace(current_attacker, "")

            print(tanks[current_attacker].name + " tank has been selected to attack\n")

            # Prints the available tanks and asks the user to select one of the showed tanks keys
            print("Please select one of the available enemies:\n")
            print_tanks(tanks)
            current_enemy = input("\nKey of your enemy: ")

            # A tank can't attack himself (duuh²)
            while(current_attacker == current_enemy):
                clear_screen()
                print("You can't attack yourself.\n")
                print("Please select one of the available enemies:\n")
                print_tanks(tanks)
                current_enemy = input("\nKey of your enemy: ")

            clear_screen()

            # Finally firering at the enemy tank
            tanks[current_attacker].fire_at(tanks[current_enemy])
            
            time.sleep(2)
            clear_screen()

            # Checking if the attacked enemy is now dead
            if (not tanks[current_enemy].alive):
                # Removing the dead enemy from the tanks dictionary
                tanks.pop(current_enemy)
                # Removing the dead enemy from the remaining attackers of this round
                remaining_attackers = remaining_attackers.replace(current_enemy, "")

        # Priting the end round info, and the current live players statistics
        print("End of round!\n")
        print("Current stats:\n")
        print_tanks(tanks)
        time.sleep(5)

    # Prints the winner of the game
    clear_screen()
    for winner in tanks:
        print(tanks[winner].name + " won the game!!!")

# Gets the inputs and returns an array with each tank name
def get_input():

    names = []
    tanks_amount = int(input("How many tanks you want to create? (2~10): "))

    while (tanks_amount < 2 or tanks_amount > 10):

        print("Invalid tanks amount, please add a value between 2 and 10.")
        tanks_amount = int(input("How many tanks you want to create? (2~10): "))

    # Asking for each tank name
    for i in range(tanks_amount):
        names.append(input("Please add the name for the tank number " + str(i+1) + ": "))

    return names

# Returns to the next character based on the ASCII table   
def next_char(ch):

    return(chr(ord(ch) + 1))

# Creates the tank objects, based on the length of the given 'names' array
def create_tanks(names):

    tanks = {}
    current_char = "`"

    for i in range(len(names)):

        current_char = next_char(current_char)
        tanks[current_char] = Tank(names[i])

    return tanks

def init(): 

    # Getting the inputs
    names = get_input()
    # Creating the tanks
    tanks = create_tanks(names)
    # Starting the game
    start_game(tanks)

# Calling the init function (duuh³)
init()