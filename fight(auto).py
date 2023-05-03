import time
import random

monsterlist=["goblin", "kobolt"]
monsterchoice=(monsterlist[random.randint(0, 1)])
print (monsterchoice)
#statuses
#alive=playerhealth*1
#dead=*0
#player stat block
playerbasehealth = 10
playermaxhealth = 10
playerhealth = 10
playerbasedamage = 1
playerdamage = 1
playerluck = 2
playerbaseagility = 16
playeragility = 15
playerequiped=[]
playerstatus="alive"
#goblin stat block
if monsterchoice == "goblin":
    monsterbasehealth = 7
    monsterhealth = 7
    monsterbasedamage = 1
    monsterdamage = 1
    monsterluck = 1
    monsterbaseagility = 16
    monsteragility = 16
    monsterstatus="alive"
    monsterdroplist=["Scimitar","Pair of Hide Shoes"]
#koblot stat block
elif monsterchoice == "kobolt":
    monsterbasehealth = 9
    monsterhealth = 9
    monsterbasedamage = 1
    monsterdamage = 1
    monsterluck = 1
    monsterbaseagility = 16
    monsteragility = 14
    monsterstatus="alive"
    monsterdroplist=["Spear","Pair of Hide Bracelet"]
#encounter beginning
print("you have encountered a ",monsterchoice," do you want to fight, he hasn't noticed you yet.")
encounter1 = input("yes or no? ")

if encounter1 == "yes":
    print("you catch the ",monsterchoice," by suprise")
    while True:
#player turn
        playercritran = random.randint(1,20)
        playercritchance = playercritran + playerluck
        if playercritchance > monsteragility:
            playerdamage = playerdamage*2
        monsterhealth = monsterhealth-playerdamage
        playerdamage = playerbasedamage
        time.sleep(.1)
        print("goblin health is",monsterhealth)
#player turn end
        if monsterhealth <= 0:
            monsterstatus="dead"
            print ("you win")
            playerhealth=playermaxhealth
            print ("your health is restored",playerhealth)
            if monsterstatus=="dead":
                monsterdrop=(monsterdroplist[random.randint(0, 1)])
                print("after slaying it you've aquired a",monsterdrop)
            break
#monster turn
        monstercritran = random.randint(1,20)
        monstercritchance = monstercritran+monsterluck
        if monstercritchance > playeragility:
            monsterdamage=monsterdamage*2
        playerhealth=playerhealth-monsterdamage
        monsterdamage=monsterbasedamage
        time.sleep(.1)
        print("current health is",playerhealth)
#monster turn end
        if playerhealth <= 0:
            playerstatus="dead"
            print("YOU DIED")
            break
        
elif encounter1 == "no":
    print("the ",monsterchoice," notices you anyway")
    time.sleep(.7)
    while True:
#monster turn
        monstercritran = random.randint(1,20)
        monstercritchance = monstercritran + monsterluck
        if monstercritchance > playeragility:
            monsterdamage = monsterdamage*2
        playerhealth=playerhealth-monsterdamage
        monsterdamage = monsterbasedamage
        print("current health is",playerhealth)
#monster turn end
        if playerhealth<=0:
            playerstatus="dead"
            print("YOU DIED")
            break
#player turn
        time.sleep(.1)
        playercritran = random.randint(1,20)
        playercritchance = playercritran + playerluck
        if playercritchance > monsteragility:
            playerdamage = playerdamage*2
        monsterhealth = monsterhealth-playerdamage
        playerdamage = playerbasedamage
        time.sleep(.1)
        print("goblin health is",monsterhealth)
#player turn end
        if monsterhealth <= 0:
            monsterstatus="dead"
            print ("you win")
            playerhealth=playermaxhealth
            print ("your health is restored",playerhealth)
            if monsterstatus=="dead":
                monsterdrop=(monsterdroplist[random.randint(0, 1)])
                print("after slaying it you've aquired a",monsterdrop)
            break









