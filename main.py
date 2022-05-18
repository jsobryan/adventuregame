import random


newline = '\n'

def randstat():
    return random.randint(0,10) + 10
def randnum():
    return random.randint(0,10)
class Player:
    def __init__(self,combatskill,endurance):
        self.combatskill = combatskill
        self.endurance = endurance
        self.crowns = 0
        self.equipment = []

disciplinelist = [
    "Camouflage",
    "Hunting",
    "Sixth Sense",
    "Tracking",
    "Healing",
    "Mindshield",
    "Mindblast",
    "Animal Kinship",
    "Mind Over Matter",
    "Weaponskill",
]

weaponlist = [
    "Dagger",
    "Spear",
    "Mace",
    "Short Sword",
    "Warhammer",
    "Sword",
    "Axe",
    "Quarterstaff",
    "Broadsword",
]

def randweapon():
    x = randnum()
    if x == 0:
        weapon = weaponlist[0]
    elif x == 1:
        weapon = weaponlist[1]
    elif x == 2:
        weapon = weaponlist[2]
    elif x == 3:
        weapon = weaponlist[3]
    elif x == 4: 
        weapon = weaponlist[4]
    elif x == 5 or x == 7:
        weapon = weaponlist[5]
    elif x == 6:
        weapon = weaponlist[6] 
    elif x == 8:
        weapon = weaponlist[7]
    elif x == 9:
        weapon = weaponlist[8]
    print(f'You have chosen the discipline "weaponskill".  You will recieve 2 bonus combat points when carrying the {weapon}.')

def randitem():
    x = randnum()
    if x == 1:
        item = weaponlist[5]
    elif x == 2:
        item = "Helmet (Special Items).  This adds 2 ENDURANCE points to your total."
    elif x == 3:
        item = "Two Meals"
    elif x == 4:
        item = "Chainmail Waistcoat (Special Items).  This adds 4 ENDURANCE points to your total."
    elif x == 5:
        item = weaponlist[2]
    elif x == 6:
        item = "Healing Potion (Backpack Item). This can restore 4 ENDURANCE points to your total, when swallowed after combat. You only have enough for one dose."
        self.equipment.append("Healing Potion")
    elif x == 7:
        item = weaponlist[7]
    elif x == 8:
        item = weaponlist[1]
    elif x == 9:
        item = "12 Gold Crowns"
        #player.crowns = crowns + 12
    elif x == 0:
        item = weaponlist[8]
    print(f'You also find the following item:\n{item}')












