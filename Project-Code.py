import random
import os 
import sys
import time

#Validation for the players name
valid_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
#All the valid characters the player is allowed to use for their name

while True:
    playername = input("Adventurer, what is your name: ")
    if all(char in valid_characters for char in playername):
        break
    print("That is not a valid character name.Please only use the alphabet!")


#The players class and all the attributes 
class Player():
    def __init__(self, name=playername, potions=0, weapon=None, health=10, maxhealth=10, gold=0):
        self.name = name
        self.potions = potions
        self.weapon = weapon
        self.health = health
        self.maxhealth = maxhealth
        self.gold = gold
        
player = Player()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#randomising attack
Grandomattack = random.randint(1,4)
#randomising gold
Grandomgoldloot = random.randint(8,15)


#goblin attributes
class Goblin():
    def __init__(self, health=10, goldloot=Grandomgoldloot, attack=Grandomattack):
        self.health = health
        self.goldloot = goldloot
        self.attack = attack

goblin = Goblin()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#randomising attack
GKrandomattack = random.randint(5,9)
#randomising gold
GKrandomgoldloot = random.randint(16,29)


#GoblinKing attributes
class GoblinKing():
    def __init__(self, health=30, goldloot=GKrandomgoldloot, attack=GKrandomattack):
        self.health = health
        self.goldloot = goldloot
        self.attack = attack

goblinking = GoblinKing()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#randomising attack
Drandomattack = random.randint(10,18)
#randomising gold
Drandomgoldloot = random.randint(20,30)



#Demon attributes
class Demon():
    def __init__(self, health=40, goldloot=Drandomgoldloot, attack=Drandomattack):
        self.health = health
        self.goldloot = goldloot
        self.attack = attack

demon = Demon()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#randomising attack
DKrandomattack = random.randint(14,20)
#randomising gold
DKrandomgoldloot = random.randint(24,36)


#Demon King attributes
class DemonKing():
    def __init__(self, health=50, goldloot=DKrandomgoldloot, attack=DKrandomattack):
        self.health = health
        self.goldloot = goldloot
        self.attack = attack

demonking = DemonKing()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
MDrandomattack = random.randint(20,30)


class MowensDragon():
    def __init__(self,health=100, prize="DemonSlayer", attack=MDrandomattack):
        self.health= health
        self.prize = prize
        self.attack = attack

mowensdragon = MowensDragon()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Mrandomattack = random.randint(30,40)


class Mowen():
    def __init__(self,health=150, prize="Nichirin Blades",attack=Mrandomattack):
        self.health= health
        self.prize = prize
        self.attack = attack


mowen = Mowen()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


