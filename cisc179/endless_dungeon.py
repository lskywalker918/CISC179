##To test the game, keep fleeing.

#Import stuff
import tkinter as tk
import random as rng

class enemy: #Enemy stat block
    def __init__(self, enemyName, enemyHP, enemyAC, description, attackName, attackBonus, minAttackDamage, maxAttackDamage):
        self.enemyName= enemyName #String
        self.enemyHP= enemyHP #Integer
        self.enemyAC= enemyAC #Integer <= 20
        self.description= description #Less than 200 characters
        self.attackName= attackName #String
        self.attackBonus= attackBonus #Integer <=10
        self.minAttackDamage= minAttackDamage #Integer >1
        self.maxAttackDamage= maxAttackDamage #Integer

    def getEnemyName(self):
        return self.enemyName
    def getEnemyHP(self):
        return self.enemyHP
    def getEnemyAC(self):
        return self.enemyAC
    def getDescription(self):
        return self.description
    def getAttackName(self):
        return self.attackName
    def getAttackBonus(self):
        return self.attackBonus
    def getMinAttackDamage(self):
        return self.minAttackDamage
    def getMaxAttackDamage(self):
        return self.maxAttackDamage

#Create class object for currentEnemy
a1= enemy('Kobold', 10, 12, 'A reptilian creature about the size of a five-year-old human child. It holds a sling in its hand, looking more ferocious than a child.', 'Sling', 4, 3, 6)
a2= enemy('Direwolf', 22, 14, 'This is no common dog or wolf. It is larger than any canine you have ever seen. Its fur is matted and it looks very hungry.', 'Bite', 5, 5, 15)
a3= enemy('Lion', 19, 12, 'The lion is definitely not sleeping tonight.', 'Claw', 5, 4, 9)
a4= enemy('Bugbear', 24, 16, 'This is neither a bear nor a bug. It is an angry hairy goblinoid. It is holding a mean-looking morningstar.', 'Morningstar', 4, 3, 18)
a5= enemy('Flying Sword', 14, 17, "While the sword remains motionless, it is indistinguishable from normal sowrd. Don't go touching random things.", 'Longsword', 3, 1, 8)
a6= enemy('Fire Snake', 30, 14, 'Lucky for you, the fire snake does not spit fire.', 'Bite', 3, 2, 5)
a7= enemy('Intellect Devourer', 28, 13, 'A large, glistening brain with four short, clawed legs. Relieved that you escaped its notice, you are slightly offended that it does not detect your intelligence.', 'Claw', 5, 4, 9)
a8= enemy('Red Dragon', 30, 19, 'This red dragon is the largest you have ever seen. It seems to have difficulty flying and can only roll along the floor.', 'Roll over', 8, 10, 20)
a9= enemy('Killer Rabbit of Caerbannog', 72, 20, 'Anyone got the Holy Hand Grenade of Antioch?', 'Nasty, big, pointy teeth', 9, 11, 36)

##to add more monsters
##ax= Enemy.enemy('enemyName', enemyHP, enemyAC, 'description', 'attackName', attackBonus, minAttackDamage, maxAttackDamage)

class yourStat:
    def __init__(self, yourHP, yourAC, yourWeapon, yourAttackBonus, yourMinAttackDamage, yourMaxAttackDamage):
        self.yourHP= yourHP
        self.yourAC= yourAC
        self.yourWeapon= yourWeapon
        self.yourAttackBonus= yourAttackBonus
        self.yourMinAttackDamage= yourMinAttackDamage
        self.yourMaxAttackDamage= yourMaxAttackDamage

    def getYourMaxHP(self):
        return self.yourHP
    def getYourAC(self):
        return self.yourAC
    def getYourWeapon(self):
        return self.yourWeapon
    def getYourAttackBonus(self):
        return self.yourAttackBonus
    def getYourMinAttackDamage(self):
        return self.yourMinAttackDamage
    def getYourMaxAttackDamage(self):
        return self.yourMaxAttackDamage

#Create class object for currentFight from You file
player= yourStat(25, 17, 'short sword', 2, 4, 9)

#Define your global variables
roomList1= ['a dark cavernous room.', 'what looks  to be a crypt.', 'a short dark cave.', 'a long passage.', 'a grand murky cave.', 'a passageway that led to a small waterfall.']
roomList2= ['with moss and dead vermin.', 'with ash and soot, somehow untouched by time and the elements.', 'in puddles of water.', 'in dirt and grime.', 'with crawling insects, dead vermin, and broken stones.', 'with overgrown foliage.']
monsterList1= [a1,  a2, a3, a4, a5, a6]
monsterList2= [a7, a8, a9] #final boss
currentRoom= 1

##add to roomList1 and roomList2 for more room descriptions

##------------------------------------------##
class room:
    global roomList1
    global roomList2
    global currentRoom

    def determineMonster():
        global monster

        if currentRoom <=3:
            monster= rng.choice(monsterList1)
            return monster

        if currentRoom ==4: #final boss room is 1 less than endingRoom
            monster = rng.choice(monsterList2)
            return monster

        if currentRoom ==5: #endingRoom= 5
            monster= ''
            return monster

    def description():
        noun1= rng.choice(roomList1)
        noun2= rng.choice(roomList2)

        varRoom.set('You enter '+ noun1+ '\nIt is covered '+ noun2) #Display room description
        enterRoomButton.config(state='disabled')

    def goNextRoom():
        global currentRoom

        varYouAttackText.set('')
        varYouAttackResult.set('')
        varEnemyAttackText.set('')
        varEnemyAttackResult.set('')

        enterRoomButton.config(state='normal')
        attackButton.config(state='disabled')
        fleeButton.config(state='disabled')

    def endingRoom():
        global currentRoom

        # Enter epilogue here
        epilogue= 'Whether by brain or brawn, you manage to reach the end of this seemingly endless dungeon. \n\nYour reward is the joy you feel when you survive to the end!'
        startAgain= "\n\nClick 'Enter Room' to play again"

        varYourHP.set(0)
        varEnemyHP.set(0)

        varRoom.set('')
        varEnemy.set('')

        varDisplayText.set(epilogue + startAgain)

        currentRoom= 1
        room.goNextRoom()

class enemy:
    def enemyAppear(): #Starting conditions
        global enemyHP
        global playerHP
        global monster

        currentEnemy= monster.getEnemyName()
        enemyDescription= monster.getDescription()
        enemyHP = monster.getEnemyHP()

        playerHP = player.getYourMaxHP()

        varEnemy.set('\nA '+ currentEnemy.lower()+ ' appears!\n\n'+ enemyDescription) #Display enemy description
        varEnemyHP.set(enemyHP)
        varYourHP.set(playerHP)

    def enemyAttack():
        global playerHP
        global monster

        currentEnemy = monster.getEnemyName()
        enemyAttackBonus= monster.getAttackBonus()
        enemyAttackName = monster.getAttackName()
        enemyMinAttackDamage= monster.getMinAttackDamage()
        enemyMaxAttackDamage= monster.getMaxAttackDamage()

        yourCurrentAC= player.getYourAC()

        varEnemyAttackText.set('The '+ currentEnemy.lower()+ ' attacks with '+ enemyAttackName+ '!')

        enemyAttackRoll= rng.randint(1+enemyAttackBonus, 20+enemyAttackBonus)


        if enemyAttackRoll >= yourCurrentAC:
            varEnemyAttackResult.set('Enemy Attack HITS')
            print('Attack HITS')

            enemyDamage = rng.randint(enemyMinAttackDamage, enemyMaxAttackDamage)

            print(currentEnemy, 'hit you for', enemyDamage, 'points')

            playerHP -= enemyDamage
            varYourHP.set(playerHP)

            if playerHP <=0:
                you.youDead()
            else:
                gameplay.fight_prompt()
        else:
            varEnemyAttackResult.set('Enemy Attack MISSES')

            print('Attack MISSES')

            gameplay.fight_prompt()
    def enemyDead():
        global currentRoom

        victory= "You are victorious! The enemy is dead!\n\nHeal yourself then hit 'Enter Room' Button to go to next room."

        varDisplayText.set(victory)
        currentRoom += 1
        room.goNextRoom()

class you:
    def youAttack(): #Input from attackButton
        global playerHP
        global enemyHP
        global monster

        currentEnemy= monster.getEnemyName()
        enemyAC = monster.getEnemyAC()

        yourCurrentWeapon= player.getYourWeapon()
        yourCurrentAttackBonus= player.getYourAttackBonus()
        yourCurrentMinAttackDamage= player.getYourMinAttackDamage()
        yourCurrentMaxAttackDamage= player.getYourMaxAttackDamage()

        varYouAttackText.set('You attack ' +currentEnemy + ' with ' +yourCurrentWeapon)

        yourAttackRoll= rng.randint(1+yourCurrentAttackBonus, 20+yourCurrentAttackBonus)

        if yourAttackRoll >= enemyAC:
            yourDamage = rng.randint(yourCurrentMinAttackDamage, yourCurrentMaxAttackDamage)

            varYouAttackResult.set('Your Attack HITS!!!')

            print('Attack HITS')
            print('You hit', currentEnemy, 'for', yourDamage, 'points')

            enemyHP -= yourDamage
            print('Enemy HP=', enemyHP)

            varEnemyHP.set(enemyHP)

            if enemyHP <=0:
                enemy.enemyDead()
            else:
                enemy.enemyAttack()
        else:
            yourDamage= 0
            varYouAttackResult.set('Your Attack MISSES')

            enemy.enemyAttack()
    def youDead():
        global currentRoom

        varDisplayText.set("You have died a valiant death. Game Over.\n\n Press 'Enter Room' to start over from beginning.")
        currentRoom= 1

        room.goNextRoom()

    def youFlee():
        global currentRoom
        global monster

        currentEnemy = monster.getEnemyName()

        rollFlee= rng.randint(1, 20)
        if rollFlee <=15:
            varDisplayText.set('You cannot flee. The '+ currentEnemy.lower()+ ' already saw you!')
        if rollFlee >15:
            varDisplayText.set("You move stealthily passed the " + currentEnemy.lower()+ "\n\nHeal yourself then hit 'Enter Room' Button to go to next room.")

            currentRoom += 1

            room.goNextRoom()
class gameplay():
    def sequence():
        global monster

        if currentRoom ==5:
            room.endingRoom()
        else:
            room.description()
            monster= room.determineMonster()
            enemy.enemyAppear()
            gameplay.fight_prompt()

    def fight_prompt():
        varDisplayText.set('\n\nWhat do you want to do?\n [A]ttack or [F]lee')
        attackButton.config(state='normal')
        fleeButton.config(state='normal')

####-----------------------GUI----------------------------------####
window= tk.Tk()
window.title('Endless Dungeon Crawl Version 1.0')
window.geometry('500x430')

#create frames
top_frame= tk.Frame(window)
bottom_frame= tk.Frame(window)
right_frame= tk.Frame(window)
left_frame= tk.Frame(window)

#create objects
myHPtext= tk.Label(top_frame, text= 'My HP:')
varYourHP= tk.IntVar()
myHPnumber= tk.Label(top_frame, textvariable= varYourHP)
enemyHPtext= tk.Label(top_frame, text= 'Enemy HP:')
varEnemyHP= tk.IntVar()
enemyHPnumber= tk.Label(top_frame, textvariable= varEnemyHP)


varRoom= tk.StringVar()
roomDescription= tk.Label(left_frame, wraplength= 150, justify= 'left', textvariable= varRoom)
varEnemy= tk.StringVar()
enemyDescription= tk.Label(left_frame, wraplength= 150, justify= 'left', textvariable= varEnemy)

varYouAttackText= tk.StringVar()
youAttackText= tk.Label(right_frame, wraplength= 150, justify= 'left', textvariable= varYouAttackText)
varYouAttackResult= tk.StringVar()
youAttackResult= tk.Label(right_frame, justify= 'left', textvariable= varYouAttackResult)
varEnemyAttackText= tk.StringVar()
enemyAttackText= tk.Label(right_frame, wraplength= 150, justify= 'left', textvariable= varEnemyAttackText)
varEnemyAttackResult= tk.StringVar()
enemyAttackResult= tk.Label(right_frame, justify= 'left', textvariable= varEnemyAttackResult)
varDisplayText= tk.StringVar()

enterRoomButton= tk.Button(bottom_frame, text= 'Enter Room', command= gameplay.sequence) #turn off button during fight sequence
attackButton= tk.Button(bottom_frame, text= 'Attack', state= 'disabled', command= you.youAttack) #function youAttack() in TestGame
fleeButton= tk.Button(bottom_frame, text= 'Flee', state='disabled', command= you.youFlee) #function youFlee() in TestGame
displayText= tk.Label(bottom_frame, wraplength= 150, justify= 'left', textvariable= varDisplayText)

#place widgets into grids
top_frame.grid(row=0, column= 0, sticky= 'N')
left_frame.grid(row=1, column= 0, padx=15, columnspan=3, sticky= 'W')
right_frame.grid(row=1, column=1, padx= 15, columnspan=3, sticky= 'E')
bottom_frame.grid(row= 2, column= 0, padx= 15, pady= 5)

#top_frame
myHPtext.grid(row= 0, column= 0, sticky= 'W')
myHPnumber.grid(row= 0, column= 1, sticky= 'E')
enemyHPtext.grid(row= 4, column= 0, sticky= 'W')
enemyHPnumber.grid(row= 4, column= 1, sticky= 'E')

#left_frame
roomDescription.grid(row=0, column= 0, ipadx= 1, columnspan=1, sticky= 'W')
enemyDescription.grid(row=1, column= 0, ipadx=1, columnspan=1, sticky= 'W')

#right_frame
youAttackText.grid(row= 0, column= 0, sticky= 'N')
youAttackResult.grid(row= 1, column=0, sticky= 'N')
enemyAttackText.grid(row= 2, column= 0, stick= 'N')
enemyAttackResult.grid(row=3, column= 0, stick= 'N')

#bottom_frame
enterRoomButton.grid(row=1, ipady= 1, ipadx=1, column= 0)
attackButton.grid(row= 1, ipady= 1, ipadx= 1, column=1)
fleeButton.grid(row= 1, ipady= 1, ipadx= 1, column= 2)
displayText.grid(row= 2, column= 0, columnspan=2, sticky= 'W')

#open window
window.mainloop()