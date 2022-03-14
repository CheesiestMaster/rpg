inv=[]
invc=[]
equ=["No Armor","Fists"]
armor=[["No Armor",0],["Leather",5]]
weps=[["Fists",1],["Sword",5]]
notes=[]
hp=10
dc=0
dmg=1

def inventory():
    for i in range(len(inv)):
        if invc[i]>0:
            print(f"{invc[i]} {inv[i]}")

def shownotes():
    for i in notes:
        print(i)

def equip():
    inventory()
    i=input("What Item do you want to equip")
    if i in inv:
        if i not in equ:
            for a in armor:
                if a[0]==i:
                    equ[0]=i
                    dc=a[1]
            for w in weps:
                if w[0]==i:
                    equ[1]=i
                    dmg=w[1]
        else:
            print("That is already equipped")
    else:
        print("You don't have one of that to equip")

def removeitem(name, count):
    name=name.capitalize()
    count=int(count)
    if name in inv:
        i=inv.index(name)
        if invc[i]>=count:
            invc[i]-=count
            return True
    return False

def additem(name, count):
    name=name.capitalize()
    count=int(count)
    if name in inv:
        i=inv.index(name)
        invc[i]+=count
        return True
    else:
        inv.append(name)
        invc.append(count)
        return True

def checkitem(name, count):
    name=name.capitalize()
    count=int(count)
    if name in inv:
        i=inv.index(name)
        if invc[i]>=count:
            return True
    return False

def start():
    additem("Gold", 20)

def e011():
    if checkitem("Gold", 10):
        removeitem("Gold", 10)
        additem("Sword", 1)
    else:
        print("Insufficient Funds")
def e012():
    if checkitem("Gold", 10):
        removeitem("Gold", 10)
        additem("Leather", 1)
    else:
        print("Insufficient Funds")
def e013():
    if checkitem("Gold", 10):
        removeitem("Gold", 10)
        additem("Potion", 1)
    else:
        print("Insufficient Funds")
def e021():
    if "Defeat 10 bandits" not in notes:
        notes.append("Defeat 10 bandits")
        print("New Quest Added: Defeat 10 bandits")
