import time
import random
playerbasehealth = 10
playermaxhealth = 10
playerhealth = 10
playerbasedamage = 1
playerdamage = 1
playerluck = 2
playeragility = 14

goblinbasehealth = 7
goblinhealth = 7
goblinbasedamage = 1
goblindamage = 1
goblinluck = 1
goblinagility = 16

encounter1 = input("you have encountered a goblin do you want to fight, he hasn't noticed you yet, yes or no? ")

if encounter1 == "yes":
    while True:
        playercritran = random.randint(1,20)
        playercritchance = playercritran + playerluck
        if playercritchance > goblinagility:
            playerdamage = playerdamage*2
        goblinhealth = goblinhealth-playerdamage
        playerdamage = playerbasedamage
        time.sleep(.1)
        print("goblin health is",goblinhealth)
        goblincritran = random.randint(1,20)
        goblincritchance = goblincritran+goblinluck
        if goblincritchance > playeragility:
            goblindamage=goblindamage*2
        playerhealth=playerhealth-goblindamage
        goblindamage=goblinbasedamage
        time.sleep(.1)
        print("current health is",playerhealth)
        if goblinhealth <= 0:
            print ("you win")
            playerhealth=playermaxhealth
            print ("your health is restored",playerhealth)
            break
        elif playerhealth <= 0:
            print("YOU DIED")
            break
        
elif encounter1 == "no":
    print("the goblin notices you anyway")
    time.sleep(.7)
    while True:
        goblincritran = random.randint(1,20)
        goblincritchance = goblincritran + goblinluck
        if goblincritchance > playeragility:
            goblindamage = goblindamage*2
        playerhealth=playerhealth-goblindamage
        goblindamage = goblinbasedamage
        print("current health is",playerhealth)
        time.sleep(.1)
        playercritran = random.randint(1,20)
        playercritchance = playercritran + playerluck
        if playercritchance > goblinagility:
            playerdamage = playerdamage*2
        goblinhealth = goblinhealth-playerdamage
        playerdamage = playerbasedamage
        time.sleep(.1)
        print("goblin health is",goblinhealth)
        if goblinhealth <= 0:
            print ("you win")
            playerhealth=playermaxhealth
            print ("your health is restored",playerhealth)
            break
        elif playerhealth<=0:
            print("YOU DIED")
            break
