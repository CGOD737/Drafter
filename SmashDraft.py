##Smash Draft Generator

import random 
import numpy as np

###Defining Global Variable###
character = []
playerList = []
resetList = []
firstChoice = []
secondChoice = []
player = 0

##Begining of actual Program##
def main():
    generateList()
    player = int(input("Please Enter the Number of Players: "))
    enterName(player)
    fillResetlist(player)
    
    
    random.shuffle(playerList) #determines draft order
    
    print()
    print("##### ROUND 1 ######")
    print()
    iterate(player, 1)
    print()
    print("##### ROUND 2 ######")
    print()
    iterate(player, 2)
    print()
    print("FINAL DRAFT RESULTS")
    
    printResults(player)

##Generates List of all Possible Smash Characters
def generateList():
    for i in range(74):
        character.append(i)
        
##Function to allow user to enter in each name for each player        
def enterName(i):
        for k in range(i):
            name = input("Enter name of player " + str(k+1) + ": ")
            playerList.append(name)

##Fills a list with 1s to indicate if a person has used their second choice or not
def fillResetlist(i):
    for k in range(i):
        resetList.append(1)
        
##iterate is where the main selection process happens##        
def iterate(i, itNumb):
    for k in range(i):
        choice = random.choice(character)+1
        if resetList[k] == 1:
            again = input(playerList[k] + ": Your selected character is "+ str(choice) + " Would you like to use your reroll?: Y, N : ")
            if again == "Y":
                 choice = random.choice(character)+1
                 print(playerList[k] + ": Your selected character after your reroll is "+ str(choice))
                 resetList[k] = 0
        else:
            print(playerList[k] + ": You do not have anymore rerolls")
            print(playerList[k] + ": Your selected character is "+ str(choice))
        
        
        character.remove(choice) ##removes character to prevent second selection
        
        if itNumb ==1:
            firstChoice.append(choice)
        if itNumb ==2:
            secondChoice.append(choice)
        
        continue
    
def printResults(i):
    for k in range(i):
        print(playerList[k] + ": " + str(firstChoice[k]) + ", " + str(secondChoice[k]))

main()
input('Press ENTER to exit')